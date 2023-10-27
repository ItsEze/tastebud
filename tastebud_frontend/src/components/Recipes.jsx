


export default function Recipes({recipes}) {

    const recipeCardStyle = {
        border: '2px solid black',
    }


    return(
        <>
        {/* <div className="recipeCard" style={recipeCardStyle}> */}
        <div className="recipeCard">
            <></>
            <div className="contentBox">
            <h1>{recipes.hits[0].recipe.label}</h1>
            <img src={recipes.hits[0].recipe.image}></img>
            <p1 style={recipeCardStyle}>{`Servings: ${recipes.hits[0].recipe.yield}`}</p1>
            <p1 style={recipeCardStyle}>{`Calories per Serving: ${Math.round(recipes.hits[0].recipe.calories / recipes.hits[0].recipe.yield)}`}</p1>
            <p1 style={recipeCardStyle}>{`Total Time: ${Math.round(recipes.hits[0].recipe.calories / recipes.hits[0].recipe.yield)}`}</p1>

            </div>
        </div>
        
        </>
    )
}