import { useState, useCallback } from 'react'

export const useNotification = () => {
  const [notification, setNotification] = useState(null)

  const showNotification = useCallback((message, type = 'success', duration = 3000) => {
    setNotification({ message, type })
    if (duration > 0) {
      setTimeout(() => setNotification(null), duration)
    }
  }, [])

  const clearNotification = useCallback(() => {
    setNotification(null)
  }, [])

  return { notification, showNotification, clearNotification }
}

export const useLoading = (initialState = false) => {
  const [isLoading, setIsLoading] = useState(initialState)

  const startLoading = () => setIsLoading(true)
  const stopLoading = () => setIsLoading(false)

  return { isLoading, startLoading, stopLoading }
}
