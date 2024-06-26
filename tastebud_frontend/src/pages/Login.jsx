import { useState, useContext } from 'react'
import { Navigate } from 'react-router-dom';
import { login } from '../api/authApi';
import { AuthContext } from '../context/AuthContext';
import Form from '../components/Forms'; 

export default function Login({ handleInputChange, handleToken }) {
  const sharedState = useContext(AuthContext);
  const { formData } = sharedState

  const [responseMsg, setResponseMsg] = useState("")
  const [shouldRedirect, setShouldRedirect] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    const context = { email: formData.email, username: formData.email, password: formData.password }
    const token = await login(context)
    if (!token) {
      setResponseMsg("Error logging in")
    } else {
      localStorage.setItem("authToken", token)
      handleToken(token)
      setShouldRedirect(true)
    }
  }

  if (shouldRedirect) {
    return <Navigate to="/home"/>
  } else {
    return <Form key={'Login'} formType="Login" handleInputChange={handleInputChange} formData={formData} handleToken={handleToken} handleSubmit={handleSubmit} responseMsg={responseMsg}/>
  }
}