import './css/DetailedRecipe.css'



export default function Cautions({recipe}) {

    return (
        <div className='list'>
        <h1>Caution!</h1>
        <ul>
            {recipe.recipe.cautions.map((caution, index) => 
            <li key={index}>{caution}</li>
            )}
        </ul>
        </div>
    )
}