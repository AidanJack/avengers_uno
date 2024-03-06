import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1 className="text-center font-cinzel text-white text-6xl h-50 p-20">Avengers Uno</h1>
      <button className="btn-gray">PLAY</button>
    </div>
  );
}

export default App;
