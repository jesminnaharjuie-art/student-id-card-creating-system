import React, { useState, useEffect } from 'react'
import { instituteAPI, studentAPI } from '../api/client'
import { useAuth } from '../context/AuthContext'
import { Layout } from '../components/Layout'
import { Card, Button, Input, Notification } from '../components/UI'
import { Upload } from 'lucide-react'

export const InstituteSettings = () => {
  const { institute } = useAuth()
  const [settings, setSettings] = useState(null)
  const [loading, setLoading] = useState(true)
  const [notification, setNotification] = useState(null)
  const [formData, setFormData] = useState({})

  useEffect(() => {
    fetchSettings()
  }, [])

  const fetchSettings = async () => {
    try {
      const response = await instituteAPI.getSettings()
      setSettings(response.data)
      setFormData(response.data)
      setLoading(false)
    } catch (err) {
      setNotification({ message: 'Failed to fetch settings', type: 'error' })
      setLoading(false)
    }
  }

  const handleSaveSettings = async () => {
    try {
      const updateData = {
        name: formData.name,
        address: formData.address,
        phone: formData.phone,
        email: formData.email,
        website: formData.website,
      }

      if (settings && settings.id) {
        await instituteAPI.updateInstitute(settings.id, updateData)
      } else {
        await instituteAPI.updateSettings(updateData)
      }

      setNotification({ message: 'Settings saved successfully', type: 'success' })
      fetchSettings()
    } catch (err) {
      setNotification({ message: 'Failed to save settings', type: 'error' })
    }
  }

  const handleFileUpload = async (type, file) => {
    try {
      if (type === 'logo') {
        await instituteAPI.uploadLogo(file)
        setNotification({ message: 'Logo uploaded', type: 'success' })
      } else if (type === 'watermark') {
        await instituteAPI.uploadWatermark(file)
        setNotification({ message: 'Watermark uploaded', type: 'success' })
      } else if (type === 'signature') {
        await instituteAPI.uploadSignature(file)
        setNotification({ message: 'Signature uploaded', type: 'success' })
      }
      fetchSettings()
    } catch (err) {
      setNotification({ message: 'Upload failed', type: 'error' })
    }
  }

  const handleBulkImport = async (excelFile, zipFile) => {
    if (!excelFile) {
      setNotification({ message: 'Please select Excel file', type: 'warning' })
      return
    }

    try {
      const response = await studentAPI.bulkImport(institute || 1, excelFile, zipFile)
      setNotification({
        message: `Imported ${response.data.imported} students`,
        type: response.data.errors.length === 0 ? 'success' : 'warning',
      })
    } catch (err) {
      setNotification({ message: 'Import failed', type: 'error' })
    }
  }

  if (loading) return <div className="flex items-center justify-center h-screen">Loading...</div>

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
        <h1 className="text-3xl font-bold text-primary-950">Institute Settings</h1>
        <p className="text-gray-600">Manage institute information and assets</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Institute Information */}
        <Card>
          <h2 className="text-xl font-bold mb-4">Institute Information</h2>

          <Input
            label="Institute Name"
            type="text"
            value={formData.name || ''}
            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
          />

          <Input
            label="Address"
            type="text"
            value={formData.address || ''}
            onChange={(e) => setFormData({ ...formData, address: e.target.value })}
          />

          <Input
            label="Phone"
            type="text"
            value={formData.phone || ''}
            onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
          />

          <Input
            label="Email"
            type="email"
            value={formData.email || ''}
            onChange={(e) => setFormData({ ...formData, email: e.target.value })}
          />

          <Input
            label="Website"
            type="text"
            value={formData.website || ''}
            onChange={(e) => setFormData({ ...formData, website: e.target.value })}
          />

          <Button onClick={handleSaveSettings} className="w-full">
            Save Information
          </Button>
        </Card>

        {/* Assets Upload */}
        <Card>
          <h2 className="text-xl font-bold mb-4">Assets</h2>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-semibold mb-2">Institute Logo</label>
              <label className="flex items-center gap-2 p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-500">
                <Upload size={20} />
                <span className="text-sm">Click to upload</span>
                <input
                  type="file"
                  accept="image/*"
                  onChange={(e) =>
                    e.target.files[0] && handleFileUpload('logo', e.target.files[0])
                  }
                  className="hidden"
                />
              </label>
            </div>

            <div>
              <label className="block text-sm font-semibold mb-2">Watermark</label>
              <label className="flex items-center gap-2 p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-500">
                <Upload size={20} />
                <span className="text-sm">Click to upload</span>
                <input
                  type="file"
                  accept="image/*"
                  onChange={(e) =>
                    e.target.files[0] && handleFileUpload('watermark', e.target.files[0])
                  }
                  className="hidden"
                />
              </label>
            </div>

            <div>
              <label className="block text-sm font-semibold mb-2">Principal Signature</label>
              <label className="flex items-center gap-2 p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-500">
                <Upload size={20} />
                <span className="text-sm">Click to upload</span>
                <input
                  type="file"
                  accept="image/*"
                  onChange={(e) =>
                    e.target.files[0] && handleFileUpload('signature', e.target.files[0])
                  }
                  className="hidden"
                />
              </label>
            </div>
          </div>
        </Card>

        {/* Bulk Import */}
        <Card className="lg:col-span-2">
          <h2 className="text-xl font-bold mb-4">📊 Bulk Import Students</h2>
          <p className="text-gray-600 text-sm mb-4">
            Upload an Excel file with columns: Class | Roll | Name | Age | Address | Image Name
          </p>

          <BulkImportForm onImport={handleBulkImport} />
        </Card>
      </div>
    </Layout>
  )
}

const BulkImportForm = ({ onImport }) => {
  const [excelFile, setExcelFile] = useState(null)
  const [zipFile, setZipFile] = useState(null)

  const handleImport = () => {
    onImport(excelFile, zipFile)
  }

  return (
    <div className="space-y-4">
      <div>
        <label className="block text-sm font-semibold mb-2">Excel File *</label>
        <label className="flex items-center gap-2 p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-500">
          <Upload size={20} />
          <span className="text-sm">{excelFile ? excelFile.name : 'Click to upload Excel'}</span>
          <input
            type="file"
            accept=".xlsx,.xls"
            onChange={(e) => setExcelFile(e.target.files[0])}
            className="hidden"
          />
        </label>
      </div>

      <div>
        <label className="block text-sm font-semibold mb-2">Photos ZIP (Optional)</label>
        <label className="flex items-center gap-2 p-4 border-2 border-dashed border-gray-300 rounded-lg cursor-pointer hover:border-blue-500">
          <Upload size={20} />
          <span className="text-sm">{zipFile ? zipFile.name : 'Click to upload ZIP'}</span>
          <input
            type="file"
            accept=".zip"
            onChange={(e) => setZipFile(e.target.files[0])}
            className="hidden"
          />
        </label>
      </div>

      <Button onClick={handleImport} className="w-full">
        Import Students
      </Button>
    </div>
  )
}
