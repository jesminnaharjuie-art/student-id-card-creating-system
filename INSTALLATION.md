# 📋 Student ID Card Generator System (SIMS) v1.0
## Complete Installation & Deployment Package

---

## 📦 What's Included

This ZIP file contains a complete, production-ready Student ID Card Generator System with:

### Backend (FastAPI)
- ✅ Admin authentication & authorization
- ✅ SQLite database with 7 tables
- ✅ Complete REST API with 20+ endpoints
- ✅ Image processing (Pillow)
- ✅ PDF generation (ReportLab)
- ✅ QR code generation
- ✅ Excel import/processing (Pandas)
- ✅ ZIP file extraction for bulk photos

### Frontend (React + Vite + Tailwind)
- ✅ Modern, responsive UI design
- ✅ Authentication pages
- ✅ Dashboard with statistics
- ✅ Student management interface
- ✅ ID card generation module
- ✅ Institute settings page
- ✅ Bulk import wizard
- ✅ Real-time API integration

### Database
- ✅ SQLite with 7 optimized tables
- ✅ Automatic schema creation
- ✅ File path storage for uploads

### Documentation
- ✅ Complete README with API endpoints
- ✅ Quick start guide
- ✅ Setup scripts for Windows & Linux/Mac

---

## 🚀 Quick Start (Windows)

1. **Extract** the ZIP file
2. **Run** `setup.bat` (double-click)
3. **Open two terminals:**

   Terminal 1:
   ```cmd
   cd backend
   venv\Scripts\activate
   python app.py
   ```

   Terminal 2:
   ```cmd
   cd frontend
   npm run dev
   ```

4. **Access** http://localhost:5173
5. **Login** with: admin / admin123

---

## 🔒 Default Credentials (Change Immediately!)

**Username**: admin  
**Password**: admin123

---

## 📁 Project Structure

```
sims-project/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── config.py              # Configuration settings
│   ├── database.py            # Database setup
│   ├── models.py              # SQLAlchemy ORM models
│   ├── schemas.py             # Pydantic validation schemas
│   ├── requirements.txt        # Python dependencies
│   ├── routes/                # API endpoints
│   │   ├── auth.py            # Authentication
│   │   ├── institute.py       # Institute settings
│   │   ├── students.py        # Student CRUD
│   │   ├── id_cards.py        # Card generation
│   │   └── dashboard.py       # Statistics
│   ├── utils/                 # Helper functions
│   │   ├── image_handler.py   # Image processing
│   │   ├── qr_generator.py    # QR code generation
│   │   ├── pdf_generator.py   # PDF export
│   │   ├── id_card_generator.py # Card PNG generation
│   │   ├── excel_processor.py # Excel parsing
│   │   └── zip_handler.py     # ZIP extraction
│   └── uploads/               # User uploads directory
│       ├── photos/            # Student photos
│       ├── documents/         # Documents
│       ├── logos/             # Institute logos
│       ├── signatures/        # Signatures
│       └── generated_cards/   # Generated cards
├── frontend/
│   ├── package.json           # NPM dependencies
│   ├── vite.config.js         # Vite configuration
│   ├── tailwind.config.js     # Tailwind CSS config
│   ├── index.html             # HTML entry point
│   └── src/
│       ├── App.jsx            # Main app component
│       ├── main.jsx           # React entry point
│       ├── index.css          # Global styles
│       ├── api/
│       │   └── client.js      # API client with axios
│       ├── components/        # Reusable components
│       │   ├── UI.jsx         # Common UI elements
│       │   └── Layout.jsx     # Sidebar & header
│       ├── pages/             # Page components
│       │   ├── Login.jsx      # Login page
│       │   ├── Dashboard.jsx  # Dashboard
│       │   ├── Students.jsx   # Student list
│       │   ├── IDCards.jsx    # Card generator
│       │   └── InstituteSettings.jsx # Settings
│       ├── context/           # Context API
│       │   └── AuthContext.jsx # Auth state
│       └── hooks/             # Custom hooks
│           └── useNotification.js # Toast notifications
├── README.md                  # Full documentation
├── QUICKSTART.md              # Quick start guide
├── setup.bat                  # Windows setup script
├── setup.sh                   # Linux/Mac setup script
└── .env.example               # Environment variables

```

---

## 🎯 Key Features

### Module 1: Dashboard
- Real-time statistics
- Total students count
- Uploaded photos count
- Generated cards count
- Missing photos alert

### Module 2: Students Management
- Add individual students
- Search by name/ID/roll
- View student details
- Upload student photos
- Bulk import from Excel + ZIP
- Delete students

### Module 3: Institute Settings
- Institute name & contact
- Address & website
- Logo upload
- Watermark upload
- Principal signature upload
- Card template settings

### Module 4: ID Card Generation
- Generate single student card
- Generate entire class cards
- Generate all students cards
- PNG & PDF export options
- QR code (student ID in QR)
- Download generated cards

### Module 5: Bulk Import
- Excel file support (Class, Roll, Name, Age, Address, ImageName)
- ZIP file with student photos
- Automatic validation
- Error reporting
- Duplicate detection

---

## 🔌 API Endpoints (20+)

### Authentication
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/register`

### Institute
- `GET /api/v1/institute/settings`
- `POST /api/v1/institute/settings`
- `PUT /api/v1/institute/settings/{id}`
- `POST /api/v1/institute/upload-logo`
- `POST /api/v1/institute/upload-watermark`
- `POST /api/v1/institute/upload-signature`

### Students
- `GET /api/v1/students/`
- `POST /api/v1/students/`
- `GET /api/v1/students/{id}`
- `PUT /api/v1/students/{id}`
- `DELETE /api/v1/students/{id}`
- `POST /api/v1/students/upload-photo/{id}`
- `POST /api/v1/students/bulk-import`

### ID Cards
- `POST /api/v1/id-cards/generate-single/{id}`
- `POST /api/v1/id-cards/generate-class/{class}`
- `POST /api/v1/id-cards/generate-all/{institute_id}`
- `GET /api/v1/id-cards/list/{institute_id}`
- `GET /api/v1/id-cards/download/{fileName}`

### Dashboard
- `GET /api/v1/dashboard/stats/{institute_id}`

---

## 💾 Database Schema

### 7 Tables:
1. **admins** - Admin users (username, password, full_name, email)
2. **institutes** - Institute info (name, address, logo, watermark, signature)
3. **students** - Student records (name, class, roll, age, address, photo)
4. **student_parents** - Parent info (father, mother, guardian details)
5. **student_documents** - Documents (birth cert, NID copies, etc.)
6. **generated_cards** - Card records (PNG path, PDF path, issue date)
7. **settings** - System settings (key-value pairs)

---

## 🛠 Technology Stack

### Frontend
- React 18.2
- Vite 5.0
- Tailwind CSS 3.4
- React Router 6.20
- Axios 1.6
- Lucide Icons 0.294

### Backend
- FastAPI 0.104
- SQLAlchemy 2.0
- SQLite (included)
- Pillow 10.1 (image processing)
- ReportLab 4.0 (PDF generation)
- qrcode 7.4 (QR codes)
- openpyxl 3.11 (Excel reading)
- Pandas 2.1 (data processing)
- python-jose 3.3 (JWT tokens)
- passlib 1.7 (password hashing)

---

## ⚙️ System Requirements

### Minimum Requirements
- Windows 10 / Mac OS 10.15+ / Linux (Ubuntu 18.04+)
- Python 3.8+
- Node.js 14+
- 500MB free disk space
- 2GB RAM

### Recommended
- Windows 11 / Mac OS 12+ / Linux (Ubuntu 20.04+)
- Python 3.10+
- Node.js 18+
- 1GB free disk space
- 4GB RAM

---

## 📖 How to Use

### 1. Initial Setup (First Time)
1. Extract ZIP file
2. Run setup script (setup.bat or setup.sh)
3. Wait for installation

### 2. Add Institute Information
1. Login with admin/admin123
2. Go to "Institute Settings"
3. Fill institute details
4. Upload logo, watermark, signature

### 3. Import Students
1. Prepare Excel file:
   - Columns: Class, Roll, Name, Age, Address, Image Name
2. Prepare ZIP with photos (matching Image Name column)
3. Go to "Institute Settings" → Bulk Import
4. Upload Excel and ZIP files

### 4. Generate ID Cards
1. Go to "ID Cards"
2. Select format (PNG, PDF, or Both)
3. Choose: Single Student / Class / All Students
4. Click generate
5. Download from the list

### 5. View Students
1. Go to "Students"
2. Search by name, ID, or roll
3. Click to view details or upload photo

---

## 🔐 Security Notes

⚠️ **IMPORTANT**: Before production deployment:

1. Change default admin password immediately
2. Update SECRET_KEY in config.py
3. Set secure database location
4. Enable HTTPS
5. Implement rate limiting
6. Add input validation
7. Setup proper logging

Example:
```python
# backend/config.py
SECRET_KEY = "your-very-long-random-secret-key-here"
```

---

## 🐛 Troubleshooting

### Backend not starting?
```bash
# Check Python version
python --version

# Verify dependencies
pip install -r requirements.txt

# Check port 8000
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # Mac/Linux
```

### Frontend not starting?
```bash
# Check Node.js version
node --version

# Clear cache
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Database issues?
```bash
# Reset database (DELETE DATA!)
cd backend
rm sims.db
python app.py
```

---

## 📞 Support & Documentation

1. **API Documentation**: http://localhost:8000/docs (Swagger UI)
2. **README.md**: Full feature documentation
3. **QUICKSTART.md**: Getting started guide
4. **Code comments**: Throughout all files

---

## 🚀 Deployment Options

### Option 1: Windows PC (Local)
- Just run setup.bat and both servers
- Access on http://localhost:5173

### Option 2: Local Network
- Run on server PC
- Access from other PCs: http://<SERVER_IP>:5173
- Update API URL in frontend config

### Option 3: Docker
```bash
# Install Docker
# Run: docker-compose up -d
```

### Option 4: Cloud (Heroku, AWS, DigitalOcean)
- Deploy backend to cloud
- Deploy frontend to Netlify/Vercel
- Update API URLs

---

## 📄 License

MIT License - Free to use and modify

---

## ✨ Version Info

**Version**: 1.0.0  
**Release Date**: June 15, 2026  
**Status**: Stable

---

## 🎉 Ready to Use!

Your Student ID Card Generator System is ready to deploy. Follow the Quick Start guide above to begin.

**Need help?** Check the API docs at http://localhost:8000/docs once the backend is running.

---

**Happy generating! 📋**
