// Filename - App.js

import React from "react";
import { NavLink as Link } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <header>
      <div className="header-left">
        <Link className={"header-button"} to="/">
          HOME
        </Link>
        <Link className={"header-button"} to="/mnist_draw">
          MNIST
        </Link>
        <Link className={"header-button"} to="/credit_card">
          CREDIT CARD FRAUD
        </Link>
        <Link className={"header-button"} to="/network_intrusion">
          NETWORK INTRUSION
        </Link>
      </div>
      <div className="header-right">
        <Link className={"header-button"} to="/settings">
          Settings
        </Link>
      </div>
    </header>
  );
}

export default Navbar;
