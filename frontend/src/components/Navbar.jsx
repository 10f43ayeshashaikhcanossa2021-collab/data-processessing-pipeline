function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-brand">
        <div className="brand-icon">D</div>

        <div>
          <h2>DataFlow</h2>
          <span>Data Processing Pipeline</span>
        </div>
      </div>

      <div className="pipeline-status">
        <span className="status-dot"></span>
        Pipeline Online
      </div>
    </nav>
  );
}

export default Navbar;