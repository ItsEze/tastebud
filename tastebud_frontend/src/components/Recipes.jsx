import React, { useState } from 'react';
import RecipeCard from './RecipeCard';
import DetailedRecipe from './DetailedRecipe';

export default function Recipes({ recipes }) {
  const [selectedRecipe, setSelectedRecipe] = useState(null)

  const handleRecipeCardClick = (recipe) => {
    setSelectedRecipe(recipe)
  };

  const handleCloseDetailedRecipe = () => {
    setSelectedRecipe(null)
  };

  return (
    <div>
      {selectedRecipe ? (
        <DetailedRecipe recipe={selectedRecipe} onClose={handleCloseDetailedRecipe} />
      ) : (
        recipes.hits.map((recipe, index) => (
          <RecipeCard key={index} recipe={recipe} onClick={handleRecipeCardClick} />
        ))
      )}
    </div>
  )
}