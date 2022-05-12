import logo from './logo.svg';
import './App.css';
import Header from './header';
import Button from './Button';
import './ytlogo.jpg';
import SearchBar from './searchbar';


const App = () => {
  return(
    <div className="Container">
      <tr>
        <td><Header></Header></td>
        <td style={{marginLeft:470, width:200}}><SearchBar></SearchBar></td>
        <td style={{marginLeft:470}}><Button></Button></td>
      </tr>
    </div>
  );
}


export default App;
