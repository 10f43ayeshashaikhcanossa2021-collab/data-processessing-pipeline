import { useState } from "react";

function UploadSection({ onProcessed }) {
  const [file, setFile] = useState(null);
  const [apiUrl, setApiUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const processFile = async () => {
    if (!file) {
      setError("Please select a CSV or JSON file.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await fetch(
        "https://data-processessing-pipeline.onrender.com/process/file",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to process file.");
      }

      onProcessed(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const processApi = async () => {
    if (!apiUrl.trim()) {
      setError("Please enter an API URL.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await fetch(
        "https://data-processessing-pipeline.onrender.com/process/api",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: apiUrl,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Failed to process API data.");
      }

      onProcessed(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="upload-section">
      <div className="upload-card">
        <div className="section-title">
          <h2>Process Dataset</h2>
          <p>
            Upload a CSV/JSON file or provide an API endpoint.
          </p>
        </div>

        <div className="upload-grid">

          {/* File Upload */}
          <div className="input-card">
            <h3>Upload File</h3>

            <input
              type="file"
              accept=".csv,.json"
              onChange={(event) => {
                setFile(event.target.files[0]);
                setError("");
              }}
            />

            {file && (
              <p className="selected-file">
                Selected: {file.name}
              </p>
            )}

            <button
              onClick={processFile}
              disabled={loading}
              className="process-button"
            >
              {loading ? "Processing..." : "Process File"}
            </button>
          </div>

          {/* API */}
          <div className="input-card">
            <h3>Process API</h3>

            <input
              type="text"
              placeholder="https://api.example.com/data"
              value={apiUrl}
              onChange={(event) => {
                setApiUrl(event.target.value);
                setError("");
              }}
            />

            <button
              onClick={processApi}
              disabled={loading}
              className="process-button"
            >
              {loading ? "Processing..." : "Process API"}
            </button>
          </div>

        </div>

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}
      </div>
    </section>
  );
}

export default UploadSection;