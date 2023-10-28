import { Navigate } from "react-router-dom"
import { AuthContext } from '../context/AuthContext';
import { useContext } from 'react'
import './css/NavBar.css'



export default function Logout() {
    const sharedState = useContext(AuthContext);
    const { setAuthToken, authToken } = sharedState

  const handleLogout = (e) => {
    e.preventDefault()
    setAuthToken(null)
  }

  if(!authToken) {
    return <Navigate to="/"/>
  } else {
    return(
      <>
        <button className='logout' onClick={handleLogout}>Logout</button>
      </>
    )
  }

}