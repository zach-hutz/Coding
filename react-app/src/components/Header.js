import React from "react";
import Table from "./Table";

const Header = () => {
  return (
    <header>
      <Table id={1} caliber={"7.62"} count={5} />
      <Table id={2} caliber={"7.62"} count={10} />
    </header>
  );
};

export default Header;
