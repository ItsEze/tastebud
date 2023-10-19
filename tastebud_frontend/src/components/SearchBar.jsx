import { useEffect, useState } from "react"


export default function SearchBar({selectedFilters, setSelectedFilters, queryParams, setQueryParams}) {


    
      const handleInputChange = (event) => {
        const text = event.target.value;
        const tempQueryParams = {...queryParams}
        console.log('log', tempQueryParams)
        tempQueryParams['q'] = text
        setQueryParams(tempQueryParams)
        
      };


    return (
        <>
        <input 
        type="text"
        value={queryParams['q']}
        onChange={handleInputChange}
        placeholder="Search for a recipe..." />
        </>
    )
}


{/* <div className="autocomplete">
      <input
        type="text"
        value={inputText}
        onChange={handleInputChange}
        placeholder="Type to search..."
      />
      {showSuggestions && (
        inputText !== '' && (
        <div className="suggestions">
          {filteredSuggestions.map((suggestion, index) => (
            <p
              key={index}
              onClick={() => handleSuggestionClick(suggestion)}
            >   
              {suggestion}
            </p>
          ))}
        </div>
      ))}
    </div> */}