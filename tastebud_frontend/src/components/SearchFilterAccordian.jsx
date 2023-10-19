import { useEffect, useState } from "react"
import { filterOptions } from "../assets/filterList"


export default function SearchFilterAccordian({selectedFilters, setSelectedFilters}) {
    const [openFilter, setOpenFilter] = useState(null)
    console.log(filterOptions)
    console.log(openFilter)


    const handleButtonClick  = (event) => {
        const buttonId = event.target.id
        if (openFilter === buttonId) {
            setOpenFilter(null)
        } else {
            setOpenFilter(buttonId)
        }
    }

    const isActive = (filterName) => selectedFilters[openFilter] === filterName ? 'active' : '';


    const toggleFilter = (filter) => {
        const tempSelectedFilters = {...selectedFilters}
        if (tempSelectedFilters[openFilter] === filter) {
            tempSelectedFilters[openFilter] = null
        } else {
            tempSelectedFilters[openFilter] = filter
        }
        setSelectedFilters(tempSelectedFilters)

    }

    return (
        <>
        <button id='health' onClick={handleButtonClick}>Health</button>
        <button id='cuisineType' onClick={handleButtonClick}>Cuisine Type</button>
        <button id='mealType' onClick={handleButtonClick}>Meal Type</button>
        <button id='dishType' onClick={handleButtonClick}>Dish Type</button>
        <div>
            {openFilter &&
            filterOptions[openFilter].map((option, index) => (
                <button
                key={index}
                className={`toggle-button ${isActive(option)}`}
                onClick={() => toggleFilter(option)}
                >
                    {option}
                    </button>
            ))
                
            }
        </div>
        </>
    )
}