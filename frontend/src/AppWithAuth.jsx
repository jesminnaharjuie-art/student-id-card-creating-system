import React from 'react'
import App from './App'
import { AuthProvider } from './context/AuthContext'

export default () => (
  <AuthProvider>
    <App />
  </AuthProvider>
)
