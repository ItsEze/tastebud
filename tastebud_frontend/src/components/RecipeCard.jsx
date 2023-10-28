import './css/RecipeCard.css'


import React from 'react';

const RecipeCard = ({ recipe, onClick }) => {
  const recipeCardStyle = {
  }

  return (
    <div className="recipeCard" onClick={() => onClick(recipe)}>
      <img className='background' src={recipe.recipe.image} alt={recipe.recipe.label} />
      <h1 className='label'>{recipe.recipe.label}</h1>
      <p>{`Servings: ${recipe.recipe.yield}`}</p>
      <p>{`Calories per Serving: ${Math.round(recipe.recipe.calories / recipe.recipe.yield)}`}</p>
      <p>{`Total Time: ${Math.round(recipe.recipe.totalTime)}`}</p>
    </div>
  )
}

export default RecipeCard