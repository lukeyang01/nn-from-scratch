import { Canvas } from "../../components/canvas/Canvas.tsx";
import React, { useState } from "react";
import { Chart, CategoryScale, registerables } from "chart.js";
import { BarChart } from "../../components/BarChart.tsx";
import "./mnist.css";
import { api_url } from "../../API-URL.tsx";

Chart.register(...registerables, CategoryScale);

const url = api_url;

const nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
export const MNIST = () => {
  const [chartData, setChartData] = useState({
    labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    datasets: [
      {
        data: nums.map(() => 0),
      },
    ],
  });

  const handleDraw = (svg) => {
    // Fetch data
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
        setChartData({
          labels: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
          datasets: [
            {
              data: nums.map((n) => Number(data[n])),
            },
          ],
        });
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div className="mnist-body">
      <div className="canvas">
        <Canvas handleDraw={handleDraw} />
      </div>
      <div className="mnist-block">
        <h1>MNIST</h1>
        <p>
          Trained on Modified National Institute of Standards and Technology
          (MNIST) database to achieve over 98% accuracy on training data.
        </p>
      </div>
      <div className="output">
        <BarChart chartData={chartData}></BarChart>
      </div>
    </div>
  );
};
