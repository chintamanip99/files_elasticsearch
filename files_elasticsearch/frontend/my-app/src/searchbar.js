import "./searchbar.css";
import React, { useState } from 'react';
import Button from './Button';

const SearchBar = ({ sendQuery }) => {

    const [query,setQuery] = useState('');

    return(
        <>
        <input type="text" name="search"  onKeyDown={({key})=> { if(key == 'Enter') sendQuery(query) }} onChange={({target:{value}})=>setQuery(value)} placeholder="Search files by entering content here..."/>
        <Button  sendQuery={()=>sendQuery(query)}/>
        </>
    )
}

export default SearchBar;