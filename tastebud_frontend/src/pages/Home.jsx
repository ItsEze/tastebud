import { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import Login from "./Login";
import SearchFilterList from "../components/SearchContainer";
import SearchFilters from "../components/SearchBar";
import SearchContainer from "../components/SearchContainer";
import SearchBar from "../components/SearchBar";
import SearchSubmitButton from "../components/SearchControlButtons";
import { recipeSearch } from "../api/authApi";
import Recipes from "../components/Recipes";
import '../components/css/SearchContainer.css'


export default function Home({recipes, setRecipes}) {

    const sharedState = useContext(AuthContext)
    const { authToken } = sharedState

    const [queryParams, setQueryParams] = useState({
        q: '',
        health: [],
        cuisineType: '',
        mealType: '',
        dishType: ''
    })




    return (
        <>
            {recipes ? (
                <Recipes recipes={recipes}/>
            ) : (
                <div className="SearchContainer">
                <SearchContainer classname='SearchContainer' queryParams={queryParams} setQueryParams={setQueryParams} setRecipes={setRecipes}/>
                </div>
            )}
            
        </>
    )
}