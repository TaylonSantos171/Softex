import './App.css';
import HelloWorld from './components/HelloWorld';
import Frase from './components/Frase';
import SayMyName from './components/SayMyName';
import Pessoa from './components/Pessoa';

function App() {

  const nome = "Íkaro Santana"
  
  return (
    <div className="App">
      <h1>Ola React
        meu nome é Tiago Taylon e estou cursando na Softex
      </h1>
      <HelloWorld/>
      <Frase/>
      <SayMyName nome="Íkaro"/>
      <Pessoa nome={nome} idade = "27" profissao = "Instrutor pela Softex" foto = "https://via.placeholder.com/150"/>
    </div>
  );
}

export default App;
