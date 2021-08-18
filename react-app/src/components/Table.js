import React from "react";
import PropTypes from "prop-types";

const Table = ({ id, count, caliber }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Caliber</th>
          <th>Count</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{id}</td>
          <td>{caliber}</td>
          <td>{count}</td>
        </tr>
      </tbody>
    </table>
  );
};

export default Table;
