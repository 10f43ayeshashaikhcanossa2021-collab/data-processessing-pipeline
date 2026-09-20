import { useState } from "react";


function DataPreview({
  columns,
  rows
}) {

  const [search, setSearch] =
    useState("");


  const filteredRows =
    rows.filter(row => {

      if (!search.trim()) {
        return true;
      }


      return columns.some(
        column =>
          String(
            row[column] ?? ""
          )
            .toLowerCase()
            .includes(
              search.toLowerCase()
            )
      );

    });


  return (

    <div className="data-card">

      <div className="data-header">

        <div>

          <h3>
            Data Preview
          </h3>

          <span>
            Showing {
              Math.min(
                filteredRows.length,
                100
              )
            } of {
              filteredRows.length
            } rows
          </span>

        </div>


        <input
          className="search-input"
          placeholder="Search data..."
          value={search}
          onChange={
            e =>
              setSearch(
                e.target.value
              )
          }
        />

      </div>


      <div className="table-container">

        <table>

          <thead>

            <tr>

              {columns.map(
                column => (

                  <th key={column}>
                    {column}
                  </th>

                )
              )}

            </tr>

          </thead>


          <tbody>

            {filteredRows
              .slice(0, 100)
              .map(
                (row, index) => (

                  <tr key={index}>

                    {columns.map(
                      column => (

                        <td
                          key={column}
                        >
                          {
                            row[column] ??
                            "—"
                          }
                        </td>

                      )
                    )}

                  </tr>

                )
              )}

          </tbody>

        </table>


        {filteredRows.length === 0 && (

          <div className="empty-state">

            No matching records found.

          </div>

        )}

      </div>

    </div>

  );

}


export default DataPreview;