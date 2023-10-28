import React from 'react';

const RecipeCard = ({ recipe, onClick }) => {
  const recipeCardStyle = {
    border: '2px solid black',
  }

  return (
    <div className="contentBox" style={recipeCardStyle} onClick={() => onClick(recipe)}>
      <h1>{recipe.recipe.label}</h1>
      <img src={recipe.recipe.image} alt={recipe.recipe.label} />
      <p>{`Servings: ${recipe.recipe.yield}`}</p>
      <p>{`Calories per Serving: ${Math.round(recipe.recipe.calories / recipe.recipe.yield)}`}</p>
      <p>{`Total Time: ${Math.round(recipe.recipe.totalTime)}`}</p>
    </div>
  )
}

export default RecipeCard