import logo from './logo.svg';
import './App.css';
import { Home } from './Components/Home';
import { Aboutus } from './Components/Aboutus';
import { Contactus } from './Components/Contactus';
import { Header } from "./Components/Header";
import { Slider } from "./Components/Slider";
import { Footer } from "./Components/Footer";
import { Products } from "./Components/Products";
import { Singleproduct } from "./Components/Singleproduct";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<><Slider /><Home /></>}> </Route>
        <Route path="/about" element={<Aboutus />}> </Route>
        <Route path="/products" element={<Products />}> </Route>
        <Route path="/singleproduct/:id" element={<Singleproduct />}> </Route>
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
