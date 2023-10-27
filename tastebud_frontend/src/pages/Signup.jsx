import Form from "../components/Forms";
import { useState, useContext } from 'react';
import { signup } from "../api/authApi";
import {Navigate} from 'react-router-dom';
import { AuthContext } from "../context/AuthContext";



export default function Signup({handleInputChange}) {
  const sharedState = useContext(AuthContext)
  const { formData } = sharedState

  const [responseMsg, setResponseMsg] = useState("")
  const [shouldRedirect, setShouldRedirect] = useState(false)


  const handleSubmit = async (e) => {
    e.preventDefault()
    const context = {email: formData.email, username: formData.email, password: formData.password}
    const response = await signup(context)
    if(response.password) {
      setShouldRedirect(true)
    } else {
      setResponseMsg(response.email)
    }
  }

  if (shouldRedirect) {
    return <Navigate to="/"/>
  } else {
    return <Form formType={"Signup"} handleInputChange={handleInputChange} handleSubmit={handleSubmit} responseMsg={responseMsg}/>
  }

}