import { useState } from "react";

import Navbar from "./components/Navbar";
import UploadSection from "./components/UploadSection";
import QualityCards from "./components/QualityCards";
import DataPreview from "./components/DataPreview";

function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="app">
      <Navbar />

      <main className="container">

        <UploadSection
          onProcessed={(data) => setResult(data)}
        />

        {result && (
          <>
            <QualityCards
              beforeReport={result.before_report}
              afterReport={result.after_report}
            />

            <DataPreview
              columns={result.columns}
              rows={result.rows}
            />
          </>
        )}

      </main>
    </div>
  );
}

export default App;