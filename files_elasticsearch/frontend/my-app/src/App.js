import React, { useState } from 'react';
import Table from './table.js'
import axios from "axios";

import "./App.css";
import SearchBar from './searchbar';


const App = () => {
  const [searchResult, setsearchResult] = useState({});

  const sendQuery = (query) =>{
      axios.get("http://localhost:8080/files_search/search?q=".concat(query), {
      headers: {
          "Authorization": 'Token 3947b3db170dba89803816b39e5ae5d1c970d4d5'
      }
      })
      .then((res) => {
      setsearchResult(res.data);
      })
      .catch((error) => {
          console.error(error)
        })
  }

  return (
   
      <center>
      <h1>Files content search</h1>    
      <SearchBar sendQuery={sendQuery} />
      <br></br>
      <Table searchResult={searchResult} />
      </center>

  );
}

export default App;
