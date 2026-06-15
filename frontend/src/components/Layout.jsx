import React, { useState } from 'react'
import { Menu, X } from 'lucide-react'
import { useAuth } from '../context/AuthContext'
import { Link } from 'react-router-dom'

export const Sidebar = ({ isOpen, onClose }) => {
  const { logout } = useAuth()

  const menuItems = [
    { label: '🏠 Dashboard', path: '/dashboard' },
    { label: '👨‍🎓 Students', path: '/students' },
    { label: '🪪 ID Cards', path: '/id-cards' },
    { label: '⚙️ Institute Settings', path: '/institute-settings' },
  ]

  return (
    <>
      {isOpen && <div className="fixed inset-0 bg-black bg-opacity-50 lg:hidden" onClick={onClose}></div>}

      <aside
        className={`fixed left-0 top-0 h-full w-64 bg-primary-950 text-white transform transition-transform duration-300 ${
          isOpen ? 'translate-x-0' : '-translate-x-full lg:translate-x-0'
        }`}
      >
        <div className="p-6">
          <h1 className="text-2xl font-bold">📋 SIMS</h1>
          <p className="text-sm text-gray-400">Student ID Management</p>
        </div>

        <nav className="mt-8">
          {menuItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className="block px-6 py-3 hover:bg-primary-900 transition-colors"
              onClick={onClose}
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="absolute bottom-0 left-0 right-0 p-6 border-t border-primary-800">
          <button
            onClick={() => {
              logout()
              onClose()
            }}
            className="w-full bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg transition-colors"
          >
            Logout
          </button>
        </div>
      </aside>
    </>
  )
}

export const Header = ({ onMenuClick }) => {
  return (
    <header className="bg-white shadow-sm sticky top-0 z-30">
      <div className="flex items-center justify-between p-4">
        <button onClick={onMenuClick} className="lg:hidden">
          <Menu size={24} />
        </button>
        <h1 className="text-xl font-bold text-primary-950">Student ID Card Generator</h1>
        <div className="w-10 h-10 rounded-full bg-primary-100"></div>
      </div>
    </header>
  )
}

export const Layout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(false)

  return (
    <div className="flex h-screen">
      <Sidebar isOpen={sidebarOpen} onClose={() => setSidebarOpen(false)} />

      <div className="flex-1 flex flex-col lg:ml-64">
        <Header onMenuClick={() => setSidebarOpen(!sidebarOpen)} />
        <main className="flex-1 overflow-auto p-4 lg:p-6">{children}</main>
      </div>
    </div>
  )
}
