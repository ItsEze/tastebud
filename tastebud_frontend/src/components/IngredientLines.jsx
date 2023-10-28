import './css/DetailedRecipe.css'



export default function IngredientLines({recipe}) {

    return (
        <div className='list'>
        <h1>Ingredients</h1>
        <ul>
            {recipe.recipe.ingredientLines.map((ingredient, index) => 
            <li key={index}>{ingredient}</li>
            )}
        </ul>
        </div>
    )
}