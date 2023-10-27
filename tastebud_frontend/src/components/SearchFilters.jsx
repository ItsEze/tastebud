import { filterOptions } from "../assets/filterList"
import './css/SearchContainer.css'
import { HiPlus } from 'react-icons/hi'
import { FcCheckmark } from 'react-icons/fc'


export default function SearchFilters({queryParams, setQueryParams, openFilter, setOpenFilter}) {
    
    const handleButtonClick  = (event) => {
        const buttonId = event.target.id
        if (openFilter === buttonId) {
            setOpenFilter(null)
        } else {
            setOpenFilter(buttonId)
        }
    }

    const isActive = (filterOption) => {
        if (openFilter === 'health') {
            return queryParams['health'] && queryParams['health'].includes(filterOption) ? 'active' : ''
        } else {
            return queryParams[openFilter] === filterOption ? 'active' : ''
        }
    }

    const toggleFilter = (filter) => {
        const tempqueryParams = { ...queryParams }
        if (openFilter === 'health') {
          if (!tempqueryParams['health']) {
            tempqueryParams['health'] = [filter]
          } else {
            const index = tempqueryParams['health'].indexOf(filter)
            if (index !== -1) {
              tempqueryParams['health'].splice(index, 1)
            } else {
              tempqueryParams['health'].push(filter)
            }
          }
        } else if (tempqueryParams[openFilter] === filter) {  
            tempqueryParams[openFilter] = ''
        } else {
          tempqueryParams[openFilter] = filter
        }
        setQueryParams(tempqueryParams)
      }

    return (
      <>
        <div className="searchFilters">
        <p>Choose from multiple filters to help refine your search!</p>
        <button id='health' onClick={handleButtonClick} className={openFilter === 'health' ? 'active' : ''}>Health</button>
        <button id='cuisineType' onClick={handleButtonClick} className={openFilter === 'cuisineType' ? 'active' : ''}>Cuisine Type</button>
        <button id='mealType' onClick={handleButtonClick} className={openFilter === 'mealType' ? 'active' : ''}>Meal Type</button>
        <button id='dishType' onClick={handleButtonClick} className={openFilter === 'dishType' ? 'active' : ''}>Dish Type</button>
        </div>
        <div className="filterOptions">
            {openFilter &&
            filterOptions[openFilter].map((option, index) => (
              <button
              key={index}
              className={`toggle-button ${isActive(option)}`}
              onClick={() => toggleFilter(option)}
              >
                <span className='buttonText'>{option}</span>
                {isActive(option) ? <FcCheckmark className="FcCheckmark" /> : <HiPlus className="HiPlus"/>}
              </button>
            ))  
          }
        </div>
        </>
        
    )
}