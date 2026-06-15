import { createContext, useState, useContext } from 'react'

const AuthContext = createContext()

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null)
  const [token, setToken] = useState(localStorage.getItem('access_token'))
  const [institute, setInstitute] = useState(localStorage.getItem('institute_id'))

  const login = (token, username, instituteId) => {
    setToken(token)
    setUser({ username })
    setInstitute(instituteId)
    localStorage.setItem('access_token', token)
    localStorage.setItem('institute_id', instituteId)
  }

  const logout = () => {
    setToken(null)
    setUser(null)
    setInstitute(null)
    localStorage.removeItem('access_token')
    localStorage.removeItem('institute_id')
  }

  return (
    <AuthContext.Provider value={{ user, token, institute, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const context = useContext(AuthContext)
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider')
  }
  return context
}
