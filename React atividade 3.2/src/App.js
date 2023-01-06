import './App.css';
import {useState, useEffect} from 'react';

function App() {

  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Tivemos ${count} clicks`; 
  })

  return (
    <div className="App">
      <p>Tivemos {count} clicks</p>
      <button onClick={() => setCount(count + 1)}> aumente o click </button>
      <button onClick={() => setCount(count - 1)}> diminua o click </button>
    </div>
  );
}

export default App;
