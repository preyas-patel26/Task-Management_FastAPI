import React, { useState } from 'react'
import { ENDPOINTS, instance } from './api'
import {useNavigate} from 'react-router-dom'

const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const navigate =useNavigate()

    const handleOnSubmit=async(e)=>{
        e.preventDefault();
        try{
            const formData = new URLSearchParams();

            formData.append("username", username);
            formData.append("password", password);

            const res = await instance.post(
                ENDPOINTS.LOGIN(),
                formData,
                {
                    headers:{
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                }
            );
            localStorage.setItem("token", res.data.access_token);
            navigate("/tasks");
        }
        catch(error){
            console.log("Login error:", error.response?.status);
            console.log("Error details:", error.response?.data);
        }
    };

    return (
        <>
            <div className='container'>
                <form onSubmit={handleOnSubmit} className='login-form'>
                    <h2>Login</h2>
                    <input type="text"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        placeholder='Username'>
                        </input>
                    <input type="password"
                        value={password}
                        onChange={(e)=>setPassword(e.target.value)}
                        placeholder='Password'>
                        </input>
                    <button>Login</button>
                </form>
            </div>
        </>
    )
}

export default Login