import React from 'react'

export const Notification = ({ message, type, onClose }) => {
  if (!message) return null

  const bgColor = {
    success: 'bg-green-100',
    error: 'bg-red-100',
    warning: 'bg-yellow-100',
    info: 'bg-blue-100',
  }[type] || 'bg-blue-100'

  const textColor = {
    success: 'text-green-700',
    error: 'text-red-700',
    warning: 'text-yellow-700',
    info: 'text-blue-700',
  }[type] || 'text-blue-700'

  const borderColor = {
    success: 'border-green-300',
    error: 'border-red-300',
    warning: 'border-yellow-300',
    info: 'border-blue-300',
  }[type] || 'border-blue-300'

  return (
    <div className={`fixed top-4 right-4 ${bgColor} ${textColor} px-6 py-3 rounded-lg border ${borderColor} shadow-lg z-50`}>
      <div className="flex items-center justify-between gap-4">
        <p>{message}</p>
        <button onClick={onClose} className="font-bold cursor-pointer">
          ×
        </button>
      </div>
    </div>
  )
}

export const Loading = () => {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-40">
      <div className="spinner"></div>
    </div>
  )
}

export const Card = ({ children, className = '' }) => {
  return <div className={`card ${className}`}>{children}</div>
}

export const Button = ({ children, onClick, className = '', variant = 'primary', disabled = false, ...props }) => {
  const variants = {
    primary: 'btn-primary',
    secondary: 'btn-secondary',
    danger: 'btn-danger',
  }

  return (
    <button
      onClick={onClick}
      className={`${variants[variant]} ${className} disabled:opacity-50 disabled:cursor-not-allowed`}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  )
}

export const Input = ({ label, error, ...props }) => {
  return (
    <div className="mb-4">
      {label && <label className="block text-sm font-semibold mb-2">{label}</label>}
      <input {...props} />
      {error && <p className="text-red-600 text-sm mt-1">{error}</p>}
    </div>
  )
}

export const Select = ({ label, options, error, ...props }) => {
  return (
    <div className="mb-4">
      {label && <label className="block text-sm font-semibold mb-2">{label}</label>}
      <select {...props}>
        <option value="">Select...</option>
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
      {error && <p className="text-red-600 text-sm mt-1">{error}</p>}
    </div>
  )
}
