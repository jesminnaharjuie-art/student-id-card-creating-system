import React, { useState, useEffect } from 'react'
import { idCardAPI, studentAPI } from '../api/client'
import { useAuth } from '../context/AuthContext'
import { Layout } from '../components/Layout'
import { Card, Button, Notification, Select } from '../components/UI'
import { Download } from 'lucide-react'

export const IDCards = () => {
  const { institute } = useAuth()
  const [students, setStudents] = useState([])
  const [classes, setClasses] = useState([])
  const [selectedClass, setSelectedClass] = useState('')
  const [selectedStudent, setSelectedStudent] = useState('')
  const [format, setFormat] = useState('both')
  const [loading, setLoading] = useState(false)
  const [notification, setNotification] = useState(null)
  const [generatedCards, setGeneratedCards] = useState([])

  useEffect(() => {
    fetchStudents()
  }, [])

  const fetchStudents = async () => {
    try {
      const response = await studentAPI.list(institute || 1)
      setStudents(response.data)

      const uniqueClasses = [...new Set(response.data.map((s) => s.class_name))]
      setClasses(uniqueClasses.map((c) => ({ label: `Class ${c}`, value: c })))

      const response2 = await idCardAPI.list(institute || 1)
      setGeneratedCards(response2.data.cards || [])
    } catch (err) {
      setNotification({ message: 'Failed to fetch data', type: 'error' })
    }
  }

  const handleGenerateSingle = async () => {
    if (!selectedStudent) {
      setNotification({ message: 'Please select a student', type: 'warning' })
      return
    }

    setLoading(true)
    try {
      const response = await idCardAPI.generateSingle(selectedStudent, format)
      setNotification({ message: 'Card generated successfully', type: 'success' })
      await fetchStudents()
    } catch (err) {
      setNotification({ message: 'Failed to generate card', type: 'error' })
    } finally {
      setLoading(false)
    }
  }

  const handleGenerateClass = async () => {
    if (!selectedClass) {
      setNotification({ message: 'Please select a class', type: 'warning' })
      return
    }

    setLoading(true)
    try {
      const response = await idCardAPI.generateClass(selectedClass, institute || 1, format)
      setNotification({
        message: `Generated ${response.data.generated} cards for class ${selectedClass}`,
        type: 'success',
      })
      await fetchStudents()
    } catch (err) {
      setNotification({ message: 'Failed to generate cards', type: 'error' })
    } finally {
      setLoading(false)
    }
  }

  const handleGenerateAll = async () => {
    setLoading(true)
    try {
      const response = await idCardAPI.generateAll(institute || 1, format)
      setNotification({
        message: `Generated ${response.data.generated} cards for all students`,
        type: 'success',
      })
      await fetchStudents()
    } catch (err) {
      setNotification({ message: 'Failed to generate cards', type: 'error' })
    } finally {
      setLoading(false)
    }
  }

  const handleDownload = async (filePath) => {
    try {
      const fileName = filePath.split('/').pop()
      const response = await idCardAPI.download(fileName)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', fileName)
      document.body.appendChild(link)
      link.click()
      link.parentElement.removeChild(link)
    } catch (err) {
      setNotification({ message: 'Failed to download file', type: 'error' })
    }
  }

  return (
    <Layout>
      {notification && (
        <Notification
          message={notification.message}
          type={notification.type}
          onClose={() => setNotification(null)}
        />
      )}

      <div className="mb-8">
        <h1 className="text-3xl font-bold text-primary-950">ID Card Generator</h1>
        <p className="text-gray-600">Generate and export ID cards</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Generate Section */}
        <Card>
          <h2 className="text-xl font-bold mb-4">Generate ID Cards</h2>

          <div className="mb-4">
            <label className="block text-sm font-semibold mb-2">Format</label>
            <select
              value={format}
              onChange={(e) => setFormat(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 rounded-lg"
            >
              <option value="both">PNG & PDF</option>
              <option value="png">PNG Only</option>
              <option value="pdf">PDF Only</option>
            </select>
          </div>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-semibold mb-2">Single Student</label>
              <select
                value={selectedStudent}
                onChange={(e) => setSelectedStudent(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg mb-2"
              >
                <option value="">Select a student...</option>
                {students.map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.name} ({s.student_id})
                  </option>
                ))}
              </select>
              <Button onClick={handleGenerateSingle} disabled={loading} className="w-full">
                Generate Single Card
              </Button>
            </div>

            <div>
              <label className="block text-sm font-semibold mb-2">By Class</label>
              <select
                value={selectedClass}
                onChange={(e) => setSelectedClass(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 rounded-lg mb-2"
              >
                <option value="">Select a class...</option>
                {classes.map((c) => (
                  <option key={c.value} value={c.value}>
                    {c.label}
                  </option>
                ))}
              </select>
              <Button onClick={handleGenerateClass} disabled={loading} className="w-full">
                Generate Class Cards
              </Button>
            </div>

            <Button onClick={handleGenerateAll} disabled={loading} className="w-full">
              Generate All Cards
            </Button>
          </div>
        </Card>

        {/* Generated Cards List */}
        <Card>
          <h2 className="text-xl font-bold mb-4">Generated Cards</h2>

          <div className="space-y-2 max-h-96 overflow-y-auto">
            {generatedCards.length === 0 ? (
              <p className="text-gray-600 text-center py-8">No cards generated yet</p>
            ) : (
              generatedCards.map((card) => (
                <div key={card.id} className="border rounded-lg p-3 flex justify-between items-center">
                  <div className="text-sm">
                    <p className="font-semibold">{card.student_name}</p>
                    <p className="text-gray-600 text-xs">{card.student_id}</p>
                  </div>
                  <div className="flex gap-2">
                    {card.png_path && (
                      <button
                        onClick={() => handleDownload(card.png_path)}
                        className="text-blue-600 hover:text-blue-700"
                        title="Download PNG"
                      >
                        <Download size={18} />
                      </button>
                    )}
                    {card.pdf_path && (
                      <button
                        onClick={() => handleDownload(card.pdf_path)}
                        className="text-red-600 hover:text-red-700"
                        title="Download PDF"
                      >
                        <Download size={18} />
                      </button>
                    )}
                  </div>
                </div>
              ))
            )}
          </div>
        </Card>
      </div>
    </Layout>
  )
}
