import React, { useEffect, useState } from 'react'
import { dashboardAPI } from '../api/client'
import { useAuth } from '../context/AuthContext'
import { Layout } from '../components/Layout'
import { Card } from '../components/UI'

export const Dashboard = () => {
  const { institute } = useAuth()
  const [stats, setStats] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await dashboardAPI.getStats(institute || 1)
        setStats(response.data)
      } catch (err) {
        console.error('Failed to fetch stats:', err)
      } finally {
        setLoading(false)
      }
    }

    fetchStats()
  }, [institute])

  if (loading) return <div className="flex items-center justify-center h-screen">Loading...</div>

  return (
    <Layout>
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-primary-950">Dashboard</h1>
        <p className="text-gray-600">Welcome to SIMS</p>
      </div>

      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <Card>
            <div className="text-center">
              <div className="text-4xl font-bold text-primary-600">{stats.total_students}</div>
              <div className="text-gray-600 mt-2">Total Students</div>
            </div>
          </Card>

          <Card>
            <div className="text-center">
              <div className="text-4xl font-bold text-green-600">{stats.total_photos_uploaded}</div>
              <div className="text-gray-600 mt-2">Photos Uploaded</div>
            </div>
          </Card>

          <Card>
            <div className="text-center">
              <div className="text-4xl font-bold text-red-600">{stats.missing_photos}</div>
              <div className="text-gray-600 mt-2">Missing Photos</div>
            </div>
          </Card>

          <Card>
            <div className="text-center">
              <div className="text-4xl font-bold text-blue-600">{stats.total_cards_generated}</div>
              <div className="text-gray-600 mt-2">Generated Cards</div>
            </div>
          </Card>
        </div>
      )}
    </Layout>
  )
}
