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


export default function Home() {

    const sharedState = useContext(AuthContext)
    const { authToken } = sharedState

    const [recipes, setRecipes] = useState(null)
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
            

        {/* this Page will have a Search Bar at the top of the page, This search bar accepts a custom search parameter and has a search button at the right end.
        Bottom of page will also have search button and a clear button.
        4 Filters: health, cuisineType, mealType, dishType - all filters are pre loaded lists. 
        You can select on multiple filters, these will be loaded into a "filter list" with a little x to delete them. */}
        {/* <NavBar /> */}
        </>
    )
}