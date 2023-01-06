import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Empresa from "./pages/Empresa";
import Contato from "./pages/Contato";
import Navbar from "./components/layout/Navbar";
import Footer from "./components/layout/Footer";

function App() {

  return (
    <Router>
      <Navbar/>
      <Switch>
        <Route exact path="/">
          <Home/>
        </Route>
        <Route path="/empresa">
          <Empresa/>
        </Route>
        <Route path="/conatato">
          <Contato/>
        </Route>
      </Switch>
      <Footer/>
    </Router>
  );
}

export default App;
