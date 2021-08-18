import Button from "./components/Button";
import Header from "./components/Header";
function App() {
  const onAdd = (e) => {
    console.log(e);
  };

  return (
    <div className="App">
      <Button color={"green"} text={"Test"} onClick={onAdd} />
      <Header />
    </div>
  );
}

export default App;
