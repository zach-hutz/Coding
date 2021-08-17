import PropTypes from "prop-types";
import Button from "./Button";
import { useLocation } from "react-router-dom";

const Header = ({ title, onAdd, showAdd }) => {
  const location = useLocation();
  return (
    <header className="header">
      <h1>{title}</h1>
      {location.pathname === "/" && (
        <Button
          color={showAdd ? "steelblue" : "green"}
          text={showAdd ? "Close" : "Add"}
          onClick={onAdd}
        />
      )}
      {/* <Button color="red" text="Red Button" />
      <Button color="yellow" text="Yellow Button" /> */}
    </header>
  );
};

Header.defaultProps = {
  title: "Task List",
};

Header.propTypes = {
  title: PropTypes.string.isRequired,
};

export default Header;
