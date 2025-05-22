import { useEffect, useState } from "react";
import { useSelector } from "react-redux";

const AnomaliesComponent = () => {
  const anomalies = useSelector((state) => state.posts.anomalies);
  const [filterUserId, setFilterUserId] = useState("");
  const [sortOrder, setSortOrder] = useState("asc");
  const [filteredRows, setFilteredRows] = useState([]);

  useEffect(() => {
    let rows = [...anomalies];

    if (filterUserId.trim() !== "") {
      rows = rows.filter((row) =>
        row.userId.toString().includes(filterUserId.trim())
      );
    }

    rows.sort((a, b) => {
      return sortOrder === "asc"
        ? a.userId - b.userId
        : b.userId - a.userId;
    });

    setFilteredRows(rows);
  }, [filterUserId, sortOrder, anomalies]);

  return (
    <div className="container mt-4 text-light">
      <h3>Anomalies</h3>

      <div className="row mb-3">
        <div className="col-md-6">
          <input
            type="text"
            className="form-control form-control-dark"
            placeholder="Filter by User ID"
            value={filterUserId}
            onChange={(e) => setFilterUserId(e.target.value)}
          />
        </div>
        <div className="col-md-6">
          <select
            className="form-control form-control-dark"
            value={sortOrder}
            onChange={(e) => setSortOrder(e.target.value)}
          >
            <option value="asc">Sort by ID ▲</option>
            <option value="desc">Sort by ID ▼</option>
          </select>
        </div>
      </div>

      <table className="table table-dark table-striped table-bordered table-hover">
        <thead>
          <tr>
            <th>User ID</th>
            <th>Username</th>
            <th>ID</th>
            <th>Title</th>
            <th>Reason</th>
          </tr>
        </thead>
        <tbody>
          {filteredRows.length === 0 ? (
            <tr>
              <td colSpan="5" className="text-center">
                No anomalies found.
              </td>
            </tr>
          ) : (
            filteredRows.map((row, index) => (
              <tr key={index}>
                <td>{row.userId}</td>
                <td>{row.username}</td>
                <td>{row.id}</td>
                <td>{row.title}</td>
                <td>{row.reason}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};
export default AnomaliesComponent;