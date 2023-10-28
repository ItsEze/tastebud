import React from 'react';

const DetailedRecipe = ({ recipe, onClose }) => {
  return (
    <div className="detailedRecipe">
      <h1>{recipe.recipe.label}</h1>
      <img src={recipe.recipe.image} alt={recipe.recipe.label} />
      {/* Display more detailed information here */}
      <button onClick={onClose}>Close</button>
    </div>
  );
};

export default DetailedRecipe;