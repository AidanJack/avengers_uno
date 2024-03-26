import { useState } from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      <h1 className="text-center font-cinzel text-white bg-black text-5xl h-30 p-4">
        Avengers Uno
      </h1>

    <div className="box flex flex-col items-center h-screen justify-center">
        <h1 className="text-center font-cinzel text-white text-7xl h-50">Avengers Uno</h1>
        <button className="text-white bg-black hover:bg-gray-900 font-medium font-cinzel py-2 px-20 mt-20 rounded text-center">
          PLAY
        </button> 
      </div>
    </div>
  );
}

export default App;
