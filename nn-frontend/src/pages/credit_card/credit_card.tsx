import React, { useEffect, useState } from "react";

import "./credit_card.css";
import { PieChart } from "../../components/PieChart.tsx";
import { Chart, ArcElement } from "chart.js";
import { api_url } from "../../API-URL.tsx";

Chart.register(ArcElement);

const url = api_url;

interface cc_data_type {
  name: String;
  date: String;
  amount: Number;
  fraud: String;
}

export const CCARD = () => {
  const [raw_data, setRawData] = useState<cc_data_type[]>([]);
  const [table_data, setTableData] = useState<Element>();
  const [num_fraud, setFraud] = useState(0);
  const [num_valid, setValid] = useState(0);
  const [chart_data, setChartData] = useState({
    labels: ["Valid", "Fraud"],
    datasets: [
      {
        data: [0, 0],
      },
    ],
  });

  const generateData = () => {
    fetch(url + "query_cc", {
      method: "get",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    })
      .then((resp) => resp.json())
      .then((data) => {
        setRawData([...raw_data, data]);
        console.log(raw_data);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  useEffect(() => {
    setTableData(
      <tbody className="cc-table-body">
        {raw_data?.map((data) => (
          <tr className="cc-table-row">
            <td>{data.name}</td>
            <td>{data.date}</td>
            <td>${String(data.amount)}</td>
            <td>{data.fraud}</td>
          </tr>
        ))}
      </tbody>
    );
    let fraud_count = 0;
    let valid_count = 0;
    raw_data?.map((data) => {
      if (data.fraud === "Fraud") fraud_count++;
      else valid_count++;
    });
    setFraud(fraud_count);
    setValid(valid_count);
    setChartData({
      labels: ["Valid", "Fraud"],
      datasets: [
        {
          data: [num_valid, num_fraud],
        },
      ],
    });
  }, [raw_data]);

  return (
    <div className="cc-container">
      <div className="cc-body">
        <div className="cc-header cc-block">
          <h1>Credit Card Fraud Detection</h1>
          <button onClick={generateData}>Generate Data</button>
        </div>
        <table className="cc-table cc-block">
          <thead className="cc-table-head">
            <tr>
              <th>Name</th>
              <th>Transaction Date::Time</th>
              <th>Amount</th>
              <th>Fraud?</th>
            </tr>
          </thead>
          {table_data}
        </table>
        <div className="cc-sidebar">
          <div className="cc-sidebar-top cc-block">
            <PieChart chartData={chart_data} />
          </div>
          <div className="cc-sidebar-bottom cc-block">
            <h2>Statistics:</h2>
            <p>Total Reports: {String(num_valid + num_fraud)}</p>
            <p>Fraudulent Transactions: {String(num_fraud)}</p>
            <p>Valid Transactions: {String(num_valid)}</p>
            <p>
              Percentage Fraudulent:{" "}
              {String((100 * num_fraud) / (num_fraud + num_valid) || 0)} %
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
