# Student ID Card Generator System - SIMS

A complete Student ID Card Management System built with React, FastAPI, and SQLite.

## Features

- ✅ Admin authentication
- ✅ Institute settings management
- ✅ Student management (CRUD)
- ✅ Bulk import from Excel + ZIP photos
- ✅ ID card generation (PNG & PDF)
- ✅ QR code integration
- ✅ Dashboard with statistics
- ✅ Responsive design

## Project Structure

```
sims-project/
├── backend/
│   ├── app.py              # FastAPI main app
│   ├── config.py           # Configuration
│   ├── database.py         # Database setup
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── requirements.txt    # Python dependencies
│   ├── routes/             # API endpoints
│   ├── utils/              # Helper functions
│   └── uploads/            # User uploads
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main app
│   │   ├── api/            # API client
│   │   ├── components/     # UI components
│   │   ├── pages/          # Page components
│   │   ├── context/        # Auth context
│   │   ├── hooks/          # Custom hooks
│   │   └── index.css       # Styles
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
└── README.md
```

## Installation

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
python app.py
```

Backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run development server:
```bash
npm run dev
```

Frontend will be available at `http://localhost:5173`

## Default Admin Credentials

- **Username**: admin
- **Password**: admin123

⚠️ Change this immediately in production!

## Usage

1. **Login**: Use default admin credentials
2. **Setup Institute**: Go to Institute Settings and fill in details
3. **Import Students**: 
   - Prepare Excel with columns: Class, Roll, Name, Age, Address, Image Name
   - Prepare ZIP with student photos
   - Upload both files
4. **Generate ID Cards**: Select students and generate cards in PNG/PDF format
5. **Download**: Download generated cards from the ID Cards page

## API Endpoints

### Authentication
- `POST /api/v1/auth/login` - Admin login
- `POST /api/v1/auth/register` - Register admin

### Institute
- `GET /api/v1/institute/settings` - Get settings
- `POST /api/v1/institute/settings` - Create/Update settings
- `POST /api/v1/institute/upload-logo` - Upload logo
- `POST /api/v1/institute/upload-watermark` - Upload watermark
- `POST /api/v1/institute/upload-signature` - Upload signature

### Students
- `GET /api/v1/students/` - List students
- `POST /api/v1/students/` - Create student
- `PUT /api/v1/students/{id}` - Update student
- `DELETE /api/v1/students/{id}` - Delete student
- `POST /api/v1/students/upload-photo/{id}` - Upload photo
- `POST /api/v1/students/bulk-import` - Bulk import

### ID Cards
- `POST /api/v1/id-cards/generate-single/{id}` - Generate single card
- `POST /api/v1/id-cards/generate-class/{class}` - Generate class cards
- `POST /api/v1/id-cards/generate-all/{institute_id}` - Generate all cards
- `GET /api/v1/id-cards/list/{institute_id}` - List generated cards
- `GET /api/v1/id-cards/download/{fileName}` - Download card

### Dashboard
- `GET /api/v1/dashboard/stats/{institute_id}` - Get statistics

## Database Schema

### Tables
- **admins** - Admin users
- **institutes** - Institute information
- **students** - Student records
- **student_parents** - Parent information
- **student_documents** - Uploaded documents
- **generated_cards** - Generated ID cards
- **settings** - System settings

## Technology Stack

### Frontend
- React 18
- Vite
- Tailwind CSS
- React Router
- Axios
- Lucide Icons

### Backend
- FastAPI
- SQLAlchemy
- SQLite
- Pillow (Image processing)
- ReportLab (PDF generation)
- qrcode (QR code generation)
- Pandas (Excel processing)

## Configuration

Edit `backend/config.py` to modify:
- Database path
- Upload directories
- File size limits
- Card dimensions
- Security settings

## Future Features

- Attendance tracking
- Fee management
- Results management
- SMS notifications
- Student promotion
- Advanced reporting

## License

MIT License

## Support

For issues or questions, please refer to the documentation or create an issue.
