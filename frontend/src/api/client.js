import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000/api/v1'

const api = axios.create({
  baseURL: API_BASE_URL,
})

// Add token to all requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// Auth APIs
export const authAPI = {
  login: (username, password) => api.post('/auth/login', { username, password }),
  register: (username, password) => api.post('/auth/register', { username, password }),
}

// Institute APIs
export const instituteAPI = {
  getSettings: () => api.get('/institute/settings'),
  updateSettings: (data) => api.post('/institute/settings', data),
  updateInstitute: (id, data) => api.put(`/institute/settings/${id}`, data),
  uploadLogo: (file) => {
    const formData = new FormData()
    formData.append('file', file)
    return api.post('/institute/upload-logo', formData)
  },
  uploadWatermark: (file) => {
    const formData = new FormData()
    formData.append('file', file)
    return api.post('/institute/upload-watermark', formData)
  },
  uploadSignature: (file) => {
    const formData = new FormData()
    formData.append('file', file)
    return api.post('/institute/upload-signature', formData)
  },
}

// Student APIs
export const studentAPI = {
  list: (instituteId, search = '', className = '') =>
    api.get('/students/', {
      params: { institute_id: instituteId, search, class_name: className },
    }),
  get: (id) => api.get(`/students/${id}`),
  create: (instituteId, data) => api.post('/students/', { ...data, institute_id: instituteId }),
  update: (id, data) => api.put(`/students/${id}`, data),
  delete: (id) => api.delete(`/students/${id}`),
  uploadPhoto: (id, file) => {
    const formData = new FormData()
    formData.append('file', file)
    return api.post(`/students/upload-photo/${id}`, formData)
  },
  bulkImport: (instituteId, excelFile, photoZip) => {
    const formData = new FormData()
    formData.append('excel_file', excelFile)
    if (photoZip) formData.append('photos_zip', photoZip)
    return api.post(`/students/bulk-import?institute_id=${instituteId}`, formData)
  },
}

// ID Card APIs
export const idCardAPI = {
  generateSingle: (studentId, format = 'both') =>
    api.post(`/id-cards/generate-single/${studentId}?format=${format}`),
  generateClass: (className, instituteId, format = 'both') =>
    api.post(`/id-cards/generate-class/${className}?institute_id=${instituteId}&format=${format}`),
  generateAll: (instituteId, format = 'both') =>
    api.post(`/id-cards/generate-all/${instituteId}?format=${format}`),
  list: (instituteId) => api.get(`/id-cards/list/${instituteId}`),
  download: (fileName) => api.get(`/id-cards/download/${fileName}`, { responseType: 'blob' }),
}

// Dashboard APIs
export const dashboardAPI = {
  getStats: (instituteId) => api.get(`/dashboard/stats/${instituteId}`),
}

export default api
