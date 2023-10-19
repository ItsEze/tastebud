import { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";
import Login from "./Login";
import SearchFilterList from "../components/SearchFilterAccordian";
import SearchFilters from "../components/SearchBar";
import SearchFilterAccordian from "../components/SearchFilterAccordian";

export default function Home() {

    const sharedState = useContext(AuthContext);
    const { authToken } = sharedState;

    const [selectedFilters, setSelectedFilters] = useState([])
    const [queryParams, setQueryParams] = useState({
        q: [],
        health: [],
        cuisineType: [],
        mealType: [],
        dishType: []
    })
    console.log(queryParams)



    return (
        <>
        <div className="recipeSearchContainer">
            <SearchFilterAccordian queryParams={queryParams} setQueryParams={setQueryParams} selectedFilters={selectedFilters} setSelectedFilters={setSelectedFilters}/>
            {/* <SearchFilterList />
            <SearchSubmitButton /> */}
        </div>

        {/* this Page will have a Search Bar at the top of the page, This search bar accepts a custom search parameter and has a search button at the right end.
        Bottom of page will also have search button and a clear button.
        4 Filters: health, cuisineType, mealType, dishType - all filters are pre loaded lists. 
        You can select on multiple filters, these will be loaded into a "filter list" with a little x to delete them. */}
        {/* <NavBar /> */}
        </>
    )
}