import { Canvas } from "./Canvas.tsx";
import React, { useEffect, useState } from "react";
import "./App.css";

const url = "http://127.0.0.1:5000/api/";

export const App = () => {
  const [output_value, setOutput] = useState(0);
  // fetch('/query_mnist', methods={'POST'});

  const handleDraw = (svg) => {
    fetch(url + "query_mnist", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
      body: JSON.stringify({ mnist_svg: svg }),
    })
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        setOutput(data["pred"]);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div className="main">
      <header>
        <div className="header-left">
          <li>MNIST</li>
          <li>Credit card fraud</li>
          <li>Network Intrusion</li>
        </div>

        <li>Settings</li>
      </header>

      <div className="content">
        <div className="canvas">
          <Canvas handleDraw={handleDraw} />
        </div>
        <div className="output">
          <h1>{output_value}</h1>
        </div>
      </div>

      <footer></footer>
    </div>
  );
};
