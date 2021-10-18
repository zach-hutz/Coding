import Head from "next/head";
import axios from "axios";
export default function Home() {
  axios.defaults.headers.get["Access-Control-Allow-Origin"] = "*";
  axios.defaults.headers.get["Content-Type"] =
    "application/x-www-form-urlencoded";
  axios.defaults.headers.get["Access-Control-Allow-Headers"] = "Content-Type";
  axios({
    method: "get",
    url: `https://ammoseek.com/ammo/9mm-luger`,
    withCredentials: false,
    crossdomain: true,
  });
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-2">
      <h1>Test</h1>
    </div>
  );
}
