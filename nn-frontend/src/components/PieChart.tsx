import React from "react";
import { Pie } from "react-chartjs-2";
import "./PieChart.css";

export const PieChart = ({ chartData }) => {
  if (!chartData.datasets) return "no dataset";
  if (!Array.isArray(chartData.datasets)) return "data not an array";

  return (
    <div className="pie-chart-container">
      <Pie
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
