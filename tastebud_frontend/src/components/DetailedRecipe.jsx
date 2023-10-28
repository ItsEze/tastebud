import React from 'react';
import NutritionFacts from './NutritionFacts';
import DietLabels from './DietLabels';
import HealthLabels from './HealthLabels';
import Cautions from './Cautions';
import IngredientLines from './IngredientLines';
import './css/DetailedRecipe.css'

const DetailedRecipe = ({ recipe, onClose }) => {
  return (
    <div className="detailedRecipe">
      <div className='column'>
        {recipe.recipe.images['LARGE'] && recipe.recipe.images['LARGE'].url && (
          <img src={recipe.recipe.images['LARGE'].url} alt={recipe.recipe.label} />
          )}
        {!recipe.recipe.images['LARGE'] || !recipe.recipe.images['LARGE'].url ? (
          <img src={recipe.recipe.image} alt={recipe.recipe.label} />
          ) : null}
          <NutritionFacts recipe={recipe}/>
      </div>
      <div className='content'>
        <div className='title'>
          <h1>{recipe.recipe.label}</h1>
          <h1>Author: {recipe.recipe.source}</h1>
          <h1>Instructions:<a href={recipe.recipe.url}>{recipe.recipe.url}</a></h1>
        </div>
        <div className='info'>
          <IngredientLines recipe={recipe}/>
          <DietLabels recipe={recipe}/>
          <HealthLabels recipe={recipe}/>
          <Cautions recipe={recipe}/>
        </div>
        </div>
        <button className='close' onClick={onClose}>Close</button>
    </div>
  );
};

export default DetailedRecipe;