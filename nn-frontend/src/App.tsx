// Filename - App.js

import React from "react";
import Navbar from "./components/Navbar.tsx";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./pages/homepage/AppHome.tsx";
import { MNIST } from "./pages/mnist/mnist.tsx";
import { CCARD } from "./pages/credit_card/credit_card.tsx";
import { NID } from "./pages/network_intrusion/nid.tsx";
import "./App.css";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<AppHome />}></Route>
        {/* <Route path="/mnist_draw" element={<MNIST />} /> */}
        <Route path="/credit_card" element={<CCARD />} />
        {/* <Route path="/network_intrusion" element={<NID />} /> */}
        {/* <Route path="/settings" element={<Settings />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
