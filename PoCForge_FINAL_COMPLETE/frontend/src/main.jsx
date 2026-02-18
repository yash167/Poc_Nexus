
import React from "react";
import ReactDOM from "react-dom/client";
import axios from "axios";

function App() {
  const [risk, setRisk] = React.useState(null);

  React.useEffect(() => {
    axios.get("http://localhost:8000/risk/demo")
      .then(res => setRisk(res.data));
  }, []);

  return (
    <div style={{padding:20}}>
      <h1>PoCForge Dashboard</h1>
      {risk && <pre>{JSON.stringify(risk, null, 2)}</pre>}
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
