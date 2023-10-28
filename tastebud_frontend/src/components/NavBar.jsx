import './css/NavBar.css'
import { Link, Navigate } from 'react-router-dom'
import Logout from './Logout'
import logo from '../assets/logo-no-background.svg'






export default function NavBar({setRecipes}) {

    const handleRecipes = () => {
        setRecipes('')
    }

    return (
        <div className="navBar">
        <Logout />
        {/* <h1>TasteBud</h1> */}
        <img src={logo} className='navLogo'></img>
        {/* <Link to='/home'>Search</Link> */}
        <button className='searchButton' onClick={handleRecipes}>Back to Search</button>
        </div>
        )
}