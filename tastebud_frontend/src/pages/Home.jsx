import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";
import Login from "./Login";

export default function Home() {

    const sharedState = useContext(AuthContext);
    const { authToken } = sharedState;

    return (
        <>
        <h1>Home</h1>
        </>
    )
}