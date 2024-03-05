import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1 className="text-center font-mono text-gray-200 text-4xl font-bold h-50 p-6 bg-gradient-to-r from-black via-red-700 to-black">
        Avengers Uno
      </h1>
    </div>
  );
}

export default App;
