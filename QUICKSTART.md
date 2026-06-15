# Quick Start Guide - Student ID Card Generator System

## Installation (Windows)

1. Extract the ZIP file
2. Double-click `setup.bat`
3. Wait for installation to complete

## Installation (Linux/Mac)

1. Extract the ZIP file
2. Run `chmod +x setup.sh && ./setup.sh`
3. Wait for installation to complete

## Starting the Application

### Method 1: Manual Start

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### Method 2: Docker (Optional)

```bash
docker-compose up -d
```

## Access the Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Default Login Credentials

- **Username**: admin
- **Password**: admin123

⚠️ **IMPORTANT**: Change the default password immediately!

## First Time Setup

1. Login with default credentials
2. Go to "Institute Settings"
3. Fill in your institute information
4. Upload institute logo, watermark, and principal signature
5. Go to "Students" and add students or use bulk import
6. Generate ID cards from "ID Cards" section

## Bulk Import Format

Prepare an Excel file with these columns:
- **Class**: Student's class (e.g., 10, 11, 12)
- **Roll**: Roll number
- **Name**: Student's full name
- **Age**: Age in years
- **Address**: Student's address
- **Image Name**: Filename of student photo (must match ZIP file)

Example:
```
Class | Roll | Name        | Age | Address         | Image Name
10    | 15   | Rahim H.    | 16  | Khulna          | 10-15-Rahim.jpg
10    | 14   | Fatima A.   | 16  | Dhaka           | 10-14-Fatima.jpg
```

Prepare a ZIP file with all student photos with matching filenames.

## Features

✅ Admin Authentication
✅ Institute Settings
✅ Student Management
✅ Bulk Import (Excel + ZIP)
✅ ID Card Generation (PNG & PDF)
✅ QR Code Integration
✅ Dashboard with Statistics
✅ Responsive UI

## Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed
- Check if port 8000 is not in use
- Verify all dependencies installed: `pip install -r requirements.txt`

### Frontend won't start
- Ensure Node.js 14+ is installed
- Check if port 5173 is not in use
- Delete `node_modules` and run `npm install` again

### API calls failing
- Ensure both backend and frontend are running
- Check browser console for errors
- Verify backend URL in frontend API client

## Database

The application uses SQLite database at `backend/sims.db`

To reset the database:
```bash
cd backend
rm sims.db  # or del sims.db on Windows
python app.py  # Will create fresh database
```

## Support

For detailed documentation, see `README.md`

For issues or questions, check the API documentation at http://localhost:8000/docs
