import React from 'react';
import './App.css';
import Products from './admin/Products';
import NavBar from './components/Nav';

import {BrowserRouter,Route,Routes} from 'react-router-dom'
import Main from './main/Main';

function App() {
  return (
    <div className="App">
      <NavBar/>
      <BrowserRouter>
        <Routes>
          <Route path='/' Component={Main}/>
          <Route path='/admin/products' Component={Products}/>
        </Routes>
      </BrowserRouter>
     {/* <Main/> */}
    </div>
  );
}

export default App;
