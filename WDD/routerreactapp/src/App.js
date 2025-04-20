import './App.css';

import { Header } from './Components/Header';
import { Footer } from './Components/Footer';
import { Home } from './Components/Home';
import { Slider } from './Components/Slider';
import { AboutUs } from './Components/AboutUs';
import { Shop } from './Components/Shop';
import { ContactUs } from './Components/ContactUs';
import { Singleproduct } from './Components/Singleproduct';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<><Slider/><Home/></>}> </Route>
        <Route path="/AboutUs" element={<AboutUs />}></Route>
        <Route path="/Shop" element={<Shop />}></Route>
        <Route path="/ContactUs" element={<ContactUs />}></Route>
        <Route path="/SingleProduct/:id" element={<Singleproduct />}> </Route>
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
