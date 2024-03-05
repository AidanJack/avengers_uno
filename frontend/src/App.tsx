import { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1 className="text-center font-cinzel  text-white text-5xl h-50 p-5 bg-gradient-to-r from-red-800 via-black to-red-800">
        Avengers Uno
      </h1>
    </div>
  );
}

export default App;
