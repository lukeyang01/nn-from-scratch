import { Canvas } from "../../components/canvas/Canvas.tsx";
import React, { useEffect, useState } from "react";
import "./credit_card.css";

const url = "http://127.0.0.1:5000/api/";

export const CCARD = () => {
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
    <div className="content">
      <div className="canvas"></div>
      <div className="output">
        <h1>{output_value}</h1>
      </div>
    </div>
  );
};
