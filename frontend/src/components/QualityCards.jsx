function QualityCards({ report }) {

  if (!report) {
    return null;
  }


  const cards = [

    {
      label: "ROWS",
      value: report.rows,
      icon: "▤"
    },

    {
      label: "COLUMNS",
      value: report.columns,
      icon: "▥"
    },

    {
      label: "MISSING VALUES",
      value: report.missing_values,
      icon: "!"
    },

    {
      label: "DUPLICATES",
      value: report.duplicate_rows,
      icon: "⧉"
    }

  ];


  return (

    <div className="quality-grid">

      {cards.map(card => (

        <div
          className="quality-card"
          key={card.label}
        >

          <div className="quality-icon">
            {card.icon}
          </div>

          <div>

            <div className="quality-label">
              {card.label}
            </div>

            <div className="quality-value">
              {card.value}
            </div>

          </div>

        </div>

      ))}

    </div>

  );

}


export default QualityCards;