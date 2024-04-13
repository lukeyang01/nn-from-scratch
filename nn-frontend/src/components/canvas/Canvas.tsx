import * as React from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import "./Canvas.css";

const styles = {
  border: "0.0625rem solid #9c9c9c",
  borderRadius: "0.25rem",
};

export const Canvas = class extends React.Component<CanvasProps, {}> {
  canvas: LegacyRef<ReactSketchCanvasRef> | undefined;
  constructor(props) {
    super(props);
    this.canvas = React.createRef();
  }

  render() {
    return (
      <div className="canvas-container">
        <ReactSketchCanvas
          ref={this.canvas}
          strokeWidth={50}
          strokeColor="black"
          onStroke={() => {
            this.canvas.current
              .exportSvg()
              .then((data) => {
                this.props.handleDraw(data);
              })
              .catch((e) => {
                console.log(e);
              });
          }}
        />
        <button
          onClick={() => {
            this.canvas.current.clearCanvas();
          }}
        >
          Clear
        </button>
      </div>
    );
  }
};

export interface CanvasProps {
  handleDraw: any;
}
