import { useEffect, useState } from "react"
import SearchControlButtons from './SearchControlButtons'
import './css/SearchContainer.css'
import { MdOutlineClear } from 'react-icons/md'

export default function SearchFilterDisplay({ queryParams, setQueryParams, setRecipes, setDanger }) {
  const [selectedFilters, setSelectedFilters] = useState([])
  
  useEffect(() => {
    const handleFilterDisplay = () => {
        const chosenFilters = []
        for (const key in queryParams) {
            if (Array.isArray(queryParams[key])) {
                chosenFilters.push(...queryParams[key])
            } else if (queryParams[key]) {
                chosenFilters.push(queryParams[key])
            }
        }
        setSelectedFilters(chosenFilters) 
    }
    handleFilterDisplay()
}, [queryParams])

  const deleteFilter = (filterOption) => {
    const tempQueryParams = { ...queryParams }
    for (const key in tempQueryParams) {
      if (Array.isArray(tempQueryParams[key])) {
        const index = tempQueryParams[key].indexOf(filterOption)
        if (index !== -1) {
          tempQueryParams[key].splice(index, 1)
        }
      } else if (tempQueryParams[key] === filterOption) {
        tempQueryParams[key] = ''
      }
    }

    setQueryParams(tempQueryParams)
  };

  return (
    <div className="searchFilterDisplayContainer">
        <ul className="displayedFilters">
          {selectedFilters.map((filterOption, index) => (
            <li key={index} className="displayedFilter">
              {filterOption}
              <MdOutlineClear className='MdOutlineClear' onClick={() => deleteFilter(filterOption)}/>
            </li>
          ))}
        </ul>
        <SearchControlButtons queryParams={queryParams} setQueryParams={setQueryParams} setRecipes={setRecipes} setDanger={setDanger}/>
    </div>
  );
}