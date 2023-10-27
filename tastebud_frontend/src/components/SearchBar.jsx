import { useEffect, useState } from "react"
import './css/SearchContainer.css'



export default function SearchBar({queryParams, setQueryParams}) {


    
      const handleInputChange = (event) => {
        const text = event.target.value;
        const tempQueryParams = {...queryParams}
        tempQueryParams['q'] = text
        setQueryParams(tempQueryParams)
      };


    return (
        <>
        <p className="searchText">Search for a recipe using a single or multiple keywords!</p>
        <div className="searchBarContainer">
        <input 
        type="text"   
        value={queryParams['q']}
        onChange={handleInputChange}
        placeholder="Search here..." />
        </div>
        </>
    )
}


