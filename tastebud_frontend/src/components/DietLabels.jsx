import './css/DetailedRecipe.css'



export default function DietLabels({recipe}) {

    return (
        <div className='list'>
            <h1>Diets</h1>
            <ul>
                {recipe.recipe.dietLabels.map((diet, index) => 
                <li key={index}>{diet}</li>
                )}
            </ul>
        </div>
    )
}