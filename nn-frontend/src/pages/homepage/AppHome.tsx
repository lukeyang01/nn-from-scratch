import { Canvas } from "../../components/canvas/Canvas.tsx";
import React, { useEffect, useState } from "react";
import "./AppHome.css";

const url = "http://127.0.0.1:5000/api/";

export const AppHome = () => {
  const [output_value, setOutput] = useState(0);
  // fetch('/query_mnist', methods={'POST'});

  return (
    <div className="apphome-container flex-center">
      <div className="apphome-body flex-center">
        <div className="app-intro-body flex-center">
          <h1>Neural Networks From Scratch</h1>
          <p>
            This site represents the final deliverable for the Neural Networks
            From Scratch project group for{" "}
            <a href="https://mdst.club/">MDST </a>
            (Michigan Data Science Team) Winter 2024 semester, lead by Luke Yang
            and Nathan Kawamoto. Through the 8-week span of this project, we
            designed and built our own fully connected MLP networks from
            scratch, utilizing mathematical calculations along with numpy and
            pandas libraries to code our own models.
          </p>
          <p>
            Features of our custom model include the following:
            <li>
              Fully customizable model parameters (num layers, layer sizes,
              etc.)
            </li>
            <li>
              Random weight and bias initialization (customizable mean and
              stdev)
            </li>
            <li>Sigmoid activation function between layers</li>
            <li>Squared loss function</li>
            <li>
              Stochastic Gradient Descent and Gradient Descent training
              algorithms
            </li>
            <li>Accuracy evalution between epochs</li>
            <li>One-hot encoding for classification datasets</li>
          </p>
          <div className="app-links">
            <a href="https://github.com/lukeyang01/nn-from-scratch">
              GITHUB LINK
            </a>
            <a href="https://docs.google.com/document/d/14p24xY2IEECJEBSNc3BOQzWLuyjkiHHXijRg9ZXmemY/edit?usp=sharing">
              Overview
            </a>
          </div>

          <p>
            With this design, we managed to achieve above 95% training accuracy
            on all three of our datasets. The following sections will detail our
            training process and parameters we used to reach that mark.
          </p>
        </div>
        <div className="app-mnist-body flex-center">
          <h2>MNIST</h2>
          <p>
            For the MNIST dataset, we managed to achieve an accuracy of 96.29%
            on testing data. To do this, we utilized the following parameters:
            <li>Layers: [784, 700, 500, 300, 10]</li>
            <li>Number of epochs: 100</li>
            <li>Learning rate: 0.15</li>
            <li>Batch size: 2056</li>
            <li>
              Weights/biases initialized with standard dev = 0.3 and mean = 0
            </li>
            <li>Normalized input vector by factor of 255</li>
          </p>
        </div>
        <div className="app-cc-body flex-center">
          <h2>Credit Card Fraud Detection</h2>
          <p>
            For the MNIST dataset, we managed to achieve an accuracy of 96.29%
            on testing data. To do this, we utilized the following parameters:
            <li>Layers: [784, 700, 500, 300, 10]</li>
            <li>Minibatch SGD</li>
            <li>Number of epochs: 100</li>
            <li>Learning rate: 0.15</li>
            <li>Batch size: 2056</li>
            <li>
              Weights/biases initialized with standard dev = 0.3 and mean = 0
            </li>
            <li>Normalized input vector by factor of 255</li>
          </p>
        </div>
        <div className="app-nid-body flex-center">
          <h2>Network Intrusion Detection</h2>
          <p>
            For the Network Intrusion Detection dataset, we managed to achieve
            an accuracy of 98.08% on testing data. To do this, we utilized the
            following parameters:
            <li>Layers: [41, 32, 23]</li>
            <li>Minibatch SGD</li>
            <li>Number of epochs: 16</li>
            <li>Learning rate: 0.8</li>
            <li>Batch size: 512</li>
            <li>
              Weights/biases initialized with standard dev = 0.5 and mean = 0
            </li>
            <li>Normalized input vector using sklearn.normalize</li>
          </p>
        </div>
      </div>
    </div>
  );
};
