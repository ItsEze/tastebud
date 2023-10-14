// src/App.js
import React, { useState } from 'react';
import './Testing.css';

function Testing() {
  const [showPopup, setShowPopup] = useState(false);

  const togglePopup = () => {
    setShowPopup(!showPopup);
  };

  return (
    <div className="App">
      <header>
        <nav>
          <div className="navbar">
            <div className="logo">Your Website</div>
            <input type="text" placeholder="Search" />
            <button>Button 1</button>
            <button>Button 2</button>
            <button>Button 3</button>
          </div>
        </nav>
      </header>
      <main>
        <div className="card">
          <p>Card 1</p>
        </div>
        <div className="card">
          <p>Card 2</p>
        </div>
        <div className="card">
          <p>Card 3</p>
        </div>
        <button className="hover-button" onClick={togglePopup}>
          Hover Button
        </button>
        {showPopup && <div className="popup">Popup Content</div>}
      </main>
    </div>
  );
}

export default Testing;
