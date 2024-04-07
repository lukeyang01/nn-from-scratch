import React from "react";
import { Bar } from "react-chartjs-2";
import "./BarChart.css";

export const BarChart = ({ chartData }) => {
  if (!chartData.datasets) return "no dataset";
  if (!Array.isArray(chartData.datasets)) return "data not an array";

  return (
    <div className="chart-container">
      <Bar
        redraw
        data={chartData}
        options={{
          plugins: {
            title: {
              display: false,
            },
            legend: {
              display: false,
            },
          },
        }}
      />
    </div>
  );
};
