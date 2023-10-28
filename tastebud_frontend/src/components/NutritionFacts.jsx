import './css/NutritionFacts.css'


export default function NutritionFacts({recipe}) {
    console.log(recipe)


    return (
        <div className="nutrition-table">
      <h2>Nutrition Facts</h2>
      <div className="table-header">
        <div className="label">Servings per Recipe</div>
        <div className="value">{recipe.recipe.yield}</div>
      </div>
      <div className="table-row">
        <div className="label">Amount of Calories per Serving</div>
        <div className="value">{Math.round(recipe.recipe.calories / recipe.recipe.yield)}</div>
      </div>
      <div className="table-row">
        <div className="label">Total Calories</div>
        <div className="value">{Math.floor(recipe.recipe.calories)}</div>
      </div>
      <div className="table-row">
        <div className="label"></div>
        <div className="value">% Daily Value</div>
      </div>
      <div className="table-row">
        <div className="label">Total Fat</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['FAT'].quantity / recipe.recipe.yield)}g ({Math.floor(recipe.recipe.totalNutrients['FAT'].quantity / recipe.recipe.yield / 65 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Saturated Fat</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['FASAT'].quantity / recipe.recipe.yield)}g ({Math.floor(recipe.recipe.totalNutrients['FASAT'].quantity / recipe.recipe.yield / 20 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Trans Fat</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['FATRN'].quantity / recipe.recipe.yield)}g </div>
      </div>
      <div className="table-row">
        <div className="label">Cholesterol</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['CHOLE'].quantity / recipe.recipe.yield)}mg ({Math.floor(recipe.recipe.totalNutrients['CHOLE'].quantity / recipe.recipe.yield / 300 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Sodium</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['NA'].quantity / recipe.recipe.yield)}mg ({Math.floor(recipe.recipe.totalNutrients['NA'].quantity / recipe.recipe.yield / 2400 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Total Carbohydrates</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['CHOCDF'].quantity / recipe.recipe.yield)}g ({Math.floor(recipe.recipe.totalNutrients['CHOCDF'].quantity / recipe.recipe.yield / 300 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Dietary Fiber</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['FIBTG'].quantity / recipe.recipe.yield)}g ({Math.floor(recipe.recipe.totalNutrients['FIBTG'].quantity / recipe.recipe.yield / 25 * 100)}%)</div>
      </div>
      <div className="table-row">
        <div className="label">Sugars</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['SUGAR'].quantity / recipe.recipe.yield)}g</div>
      </div>
      <div className="table-row">
        <div className="label">Proteins</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['PROCNT'].quantity / recipe.recipe.yield)}g</div>
      </div>
      <div className="table-row">
        <div className="label">Vitamin A</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['VITA_RAE'].quantity / recipe.recipe.yield / 5000 * 100)}%</div>
      </div>
      <div className="table-row">
        <div className="label">Vitamin C</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['VITC'].quantity / recipe.recipe.yield / 60 * 100)}%</div>
      </div>
      <div className="table-row">
        <div className="label">Calcium</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['CA'].quantity / recipe.recipe.yield / 1000 * 100)}%</div>
      </div>
      <div className="table-row">
        <div className="label">Iron</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['FE'].quantity / recipe.recipe.yield / 18 * 100)}%</div>
      </div>
      <div className="table-row">
        <div className="label">Potassium</div>
        <div className="value">{Math.floor(recipe.recipe.totalNutrients['K'].quantity / recipe.recipe.yield / 3500 * 100)}%</div>
      </div>
    </div>
  )
    
}