import { useEffect, useState, useContext } from "react"
import { recipeSearch } from "../api/authApi"
import { FaHackerNewsSquare } from "react-icons/fa"
import { AuthContext } from "../context/AuthContext";
import './css/SearchContainer.css'

export default function SearchControlButtons({queryParams, setQueryParams, setRecipes, setDanger}) {

    const sharedState = useContext(AuthContext)
    const { authToken } = sharedState

    const handleClear = () => {
        setQueryParams({
            q: '',
            health: [],
            cuisineType: '',
            mealType: '',
            dishType: ''
        })
    }

    async function handleSearch() {
        if (queryParams.q || queryParams.health.length > 0 || queryParams.cuisineType || queryParams.mealType || queryParams.dishType) {
        const recipes = await recipeSearch(queryParams, authToken)
        setRecipes(recipes)
        console.log(recipes)
    } else {
        setDanger('Please specify atleast one keyword or filter before search!')
    }
}

    return (
        <div className="searchControlButtonsContainer">
        <button onClick={handleClear}>Clear</button>
        <button onClick={handleSearch}>Search</button>
        </div>
    )
}