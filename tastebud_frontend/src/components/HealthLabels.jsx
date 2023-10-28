import './css/DetailedRecipe.css'



export default function HealthLabels({recipe}) {

    return (
        <div className='list'>
        <h1>Health</h1>
        <ul>
            {recipe.recipe.healthLabels.map((health, index) => 
            <li key={index}>{health}</li>
            )}
        </ul>
        </div>
    )
}