import React, { useState } from 'react'
import { authAPI } from '../api/client'
import { useAuth } from '../context/AuthContext'
import { useNavigate } from 'react-router-dom'
import { Button, Input, Notification } from './UI'

export const Login = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [isFirstTime, setIsFirstTime] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')
  const [success, setSuccess] = useState('')
  const { login } = useAuth()
  const navigate = useNavigate()

  const handleLogin = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')

    try {
      const response = await authAPI.login(username, password)
      login(response.data.access_token, username, 1) // Default institute ID = 1
      navigate('/dashboard')
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed')
    } finally {
      setIsLoading(false)
    }
  }

  const handleRegister = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    setError('')

    try {
      await authAPI.register(username, password)
      setSuccess('Admin registered! Logging in...')
      setTimeout(() => {
        setIsFirstTime(false)
        handleLogin(e)
      }, 1500)
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed')
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-950 to-primary-900 flex items-center justify-center p-4">
      <Notification message={error} type="error" onClose={() => setError('')} />
      <Notification message={success} type="success" onClose={() => setSuccess('')} />

      <div className="bg-white rounded-lg shadow-xl p-8 w-full max-w-md">
        <h1 className="text-3xl font-bold text-primary-950 mb-2 text-center">📋 SIMS</h1>
        <p className="text-gray-600 text-center mb-8">Student ID Management System</p>

        <form onSubmit={isFirstTime ? handleRegister : handleLogin} className="space-y-4">
          <Input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />

          <Input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <Button
            type="submit"
            disabled={isLoading}
            className="w-full"
          >
            {isLoading ? 'Processing...' : isFirstTime ? 'Register Admin' : 'Login'}
          </Button>
        </form>

        {!isFirstTime && (
          <button
            type="button"
            onClick={() => setIsFirstTime(true)}
            className="w-full mt-4 text-primary-600 hover:text-primary-700 text-sm"
          >
            First time? Register admin account
          </button>
        )}

        {isFirstTime && (
          <button
            type="button"
            onClick={() => setIsFirstTime(false)}
            className="w-full mt-4 text-primary-600 hover:text-primary-700 text-sm"
          >
            Back to login
          </button>
        )}
      </div>
    </div>
  )
}
