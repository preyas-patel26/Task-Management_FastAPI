import React from 'react'
import Login from './components/Login'
import './App.css'
import Navbar from './components/Navbar'
import Task from './components/Task'
import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom'
import {ToastContainer} from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

const ProtectedRoute = ({children}) => {
  const token = localStorage.getItem("token")
  return token ? children : <Navigate to="/"/>
}

const App = () => {
  return (
    <>
      <ToastContainer autoClose={1500}/>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login/>}></Route>
          <Route path="/tasks" element={<ProtectedRoute><Navbar/><Task/></ProtectedRoute>}></Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
