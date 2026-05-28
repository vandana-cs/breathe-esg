import { useEffect, useState } from "react";
import axios from "axios";

export default function App() {

  const [records, setRecords] = useState([]);

  const load = async () => {
    const res = await axios.get("https://breathe-esg-lvrb.onrender.com/api/records/");
    setRecords(res.data);
  };

  useEffect(() => {
    load();
  }, []);

  const upload = async (e, type) => {
    const formData = new FormData();
    formData.append("file", e.target.files[0]);

    await axios.post(`https://breathe-esg-lvrb.onrender.com/api/upload/${type}/`, formData);

    load();
  };

  const travel = async () => {
    await axios.post("https://breathe-esg-lvrb.onrender.com/api/travel/sync/");
    load();
  };

  const approve = async (id) => {
    await axios.post(`render started/api/approve/${id}/`);
    load();
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>

      <h1>🌱 Breathe ESG Dashboard</h1>

      <hr />

      <h3>SAP Upload</h3>
      <input type="file" onChange={(e) => upload(e, "sap")} />

      <h3>Utility Upload</h3>
      <input type="file" onChange={(e) => upload(e, "utility")} />

      <h3>Travel</h3>
      <button onClick={travel}>Sync Travel</button>

      <hr />

      <h2>Records</h2>

      <table border="1" cellPadding="8">

        <thead>
          <tr>
            <th>Source</th>
            <th>Type</th>
            <th>Quantity</th>
            <th>Emissions</th>
            <th>Status</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {records.map((r) => (
            <tr key={r.id}>
              <td>{r.source}</td>
              <td>{r.activity_type}</td>
              <td>{r.quantity}</td>
              <td>{r.emissions}</td>
              <td>{r.review_status}</td>
              <td>
                <button onClick={() => approve(r.id)}>
                  Approve
                </button>
              </td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  );
}