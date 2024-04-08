import { Canvas } from "../../components/canvas/Canvas.tsx";
import React, { CSSProperties, useEffect, useRef, useState } from "react";
import { Chart, CategoryScale, registerables } from "chart.js";
import { nid_data, prot_type, service_type, flag_types } from "./nid_helper.tsx";
import "./nid.css";

Chart.register(...registerables, CategoryScale);

const url = "http://127.0.0.1:5000/api/";

export const NID = () => {
  const [data, setPred] = useState<nid_data>();

  const genNID = () => {
    // Fetch data
    fetch(url + "query_nid", {
      method: "get",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    })
      .then((resp) => resp.json())
      .then((data) => {
        console.log(data);
        setPred(data);
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div className="main">
      <div className="nid-interface">
        <button className="nid-generate" onClick={genNID}>
          <h1 className="nid-button-text">GENERATE DATA</h1>
        </button>
        <div className="data-block">
          <h1>Network Intrusion Detection</h1>
          <p> &#8592; Click to (re)generate sample data</p>
        </div>
        {/* WHY DID I DO THIS TO MYSELF LOL*/}
        <div className="data-block main_data">
          <div className="data-disp-header">GENERAL INFO</div>
          <div className="data-disp-body">
            <div className="data-disp-line">
              duration:
              <p>{String(data?.duration || "0")} ms</p>
            </div>
            <div className="data-disp-line">
              protocal_type:
              <p>
                {
                  prot_type[
                    (data?.protocol_type as keyof typeof prot_type) || 0
                  ]
                }
              </p>
            </div>
            <div className="data-disp-line">
              service:
              <p>
                {
                  service_type[
                    (data?.service as keyof typeof service_type) || 0
                  ]
                }
              </p>
            </div>
            <div className="data-disp-line">
              flag:
              <p>{flag_types[(data?.flag as keyof typeof flag_types) || 0]}</p>
            </div>
            <div className="data-disp-line">
              src_bytes:
              <p>{String(data?.src_bytes || "0")}</p>
            </div>
            <div className="data-disp-line">
              dst_bytes:
              <p>{String(data?.dst_bytes || "0")}</p>
            </div>
            <div className="data-disp-line">
              land:
              <p>{String(data?.land || "0")}</p>
            </div>
            <div className="data-disp-line">
              wrong_fragment:
              <p>{String(data?.wrong_fragment || "0")}</p>
            </div>
            <div className="data-disp-line">
              urgent:
              <p>{String(data?.urgent || "0")}</p>
            </div>
            <div className="data-disp-line">
              hot:
              <p>{String(data?.hot || "0")}</p>
            </div>
          </div>
        </div>
        <div className="data-block login_data">
          <div className="data-disp-header">LOGIN DATA</div>
          <div className="data-disp-body">
            <div className="data-disp-line">
              num_failed_logins: <p>{String(data?.num_failed_logins || "0")}</p>
            </div>
            <div className="data-disp-line">
              logged_in:
              <p>{String(data?.logged_in || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_compromised:
              <p>{String(data?.num_compromised || "0")}</p>
            </div>
            <div className="data-disp-line">
              su_attempted:
              <p>{String(data?.su_attempted || "0")}</p>
            </div>
            <div className="data-disp-line">
              root_shell:
              <p>{String(data?.root_shell || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_root:
              <p>{String(data?.num_root || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_file_creations:
              <p>{String(data?.num_file_creations || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_shells:
              <p>{String(data?.num_shells || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_access_files:
              <p>{String(data?.num_access_files || "0")}</p>
            </div>
            <div className="data-disp-line">
              num_outbound_cmds:
              <p>{String(data?.num_outbound_cmds || "0")}</p>
            </div>
            <div className="data-disp-line">
              is_host_login:
              <p>{String(data?.is_host_login || "0")}</p>
            </div>
            <div className="data-disp-line">
              is_guest_login:
              <p>{String(data?.is_guest_login || "0")}</p>
            </div>
          </div>
        </div>
        <div className="data-block dest_data">
          <div className="data-disp-header">DEST SERVER DATA</div>
          <div className="data-disp-body">
            <div className="data-disp-line">
              {" "}
              dst_host_srv_count:
              <p>{String(data?.dst_host_srv_count || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_same_srv_rate:{" "}
              <p>{String(data?.dst_host_same_srv_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_diff_srv_rate:{" "}
              <p>{String(data?.dst_host_diff_srv_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_same_src_port_rate:{" "}
              <p>{String(data?.dst_host_same_src_port_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_srv_diff_host_rate:{" "}
              <p>{String(data?.dst_host_srv_diff_host_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_serror_rate:{" "}
              <p>{String(data?.dst_host_serror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_srv_serror_rate:{" "}
              <p>{String(data?.dst_host_srv_serror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_rerror_rate:{" "}
              <p>{String(data?.dst_host_rerror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              dst_host_srv_rerror_rate:{" "}
              <p>{String(data?.dst_host_srv_rerror_rate || "0")}</p>
            </div>
          </div>
        </div>
        <div className="data-block server_data">
          <div className="data-disp-header">SERVER DATA</div>
          <div className="data-disp-body">
            <div className="data-disp-line">
              {" "}
              count: <p>{String(data?.count || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              srv_count: <p>{String(data?.srv_count || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              serror_rate: <p>{String(data?.serror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              srv_serror_rate: <p>{String(data?.srv_serror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              rerror_rate: <p>{String(data?.rerror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              srv_rerror_rate: <p>{String(data?.srv_rerror_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              same_srv_rate: <p>{String(data?.same_srv_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              diff_srv_rate: <p>{String(data?.diff_srv_rate || "0")}</p>
            </div>
            <div className="data-disp-line">
              {" "}
              srv_diff_host_rate:{" "}
              <p>{String(data?.srv_diff_host_rate || "0")}</p>
            </div>
          </div>
        </div>

        <div className="data-block nid-output">
          <div className="data-disp-header">PREDICTED ATTACK TYPE</div>
          <h1>{data?.pred}</h1>
        </div>
      </div>

      <footer></footer>
    </div>
  );
};
