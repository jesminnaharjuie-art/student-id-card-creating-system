import React, { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider, useAuth } from './context/AuthContext'
import { Login } from './pages/Login'
import { Dashboard } from './pages/Dashboard'
import { Students } from './pages/Students'
import { IDCards } from './pages/IDCards'
import { InstituteSettings } from './pages/InstituteSettings'

const ProtectedRoute = ({ children }) => {
  const { token } = useAuth()
  return token ? children : <Navigate to="/login" />
}

const App = () => {
  const [isReady, setIsReady] = useState(false)
  const { token } = useAuth()

  useEffect(() => {
    setIsReady(true)
  }, [])

  if (!isReady) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>
  }

  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route
          path="/students"
          element={
            <ProtectedRoute>
              <Students />
            </ProtectedRoute>
          }
        />
        <Route
          path="/id-cards"
          element={
            <ProtectedRoute>
              <IDCards />
            </ProtectedRoute>
          }
        />
        <Route
          path="/institute-settings"
          element={
            <ProtectedRoute>
              <InstituteSettings />
            </ProtectedRoute>
          }
        />
        <Route path="/" element={<Navigate to={token ? '/dashboard' : '/login'} />} />
      </Routes>
    </Router>
  )
}

export default App
