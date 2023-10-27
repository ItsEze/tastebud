import { useEffect, useState } from "react"
import './css/SearchContainer.css'
import SearchSubmitButton from "./SearchControlButtons"
import SearchFilterDisplay from "./SearchFilterDisplay"
import SearchBar from "./SearchBar"
import SearchFilters from "./SearchFilters"
import logo from '../assets/Edamam_Badge_Transparent.svg'

export default function SearchContainer({queryParams, setQueryParams, setRecipes}) {
    const [openFilter, setOpenFilter] = useState(null)
    const [selectedElements, setSelectedElements] = useState([])
    const [danger, setDanger] = useState('')
    


    



    useEffect(() => {
        const setElements = () => {
            const chosenElements = []
            for (const key in queryParams) {
                if (Array.isArray(queryParams[key])) {
                    chosenElements.push(...queryParams[key])
                } else if (queryParams[key]) {
                    chosenElements.push(queryParams[key])
                }
            }
            setSelectedElements(chosenElements) 
        }
        setElements()
    }, [queryParams])

    return (
        <div className="container">
                <img className='logo' src={logo}></img>
                <SearchFilters queryParams={queryParams} setQueryParams={setQueryParams} openFilter={openFilter} setOpenFilter={setOpenFilter}/>        
                <SearchBar queryParams={queryParams} setQueryParams={setQueryParams}/>         
                <SearchFilterDisplay queryParams={queryParams} setQueryParams={setQueryParams} setRecipes={setRecipes} setDanger={setDanger}/>          
                <p className="danger">{danger}</p>
                <p className="spacer"></p>
                <p className="spacer2"></p>
        </div>
    )
}