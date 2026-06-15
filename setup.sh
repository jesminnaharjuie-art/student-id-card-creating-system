#!/bin/bash

# Student ID Card Generator System - Setup Script for Linux/Mac

echo ""
echo "================================================"
echo "Student ID Card Generator System - Setup"
echo "================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org"
    exit 1
fi

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org"
    exit 1
fi

echo "Python and Node.js found!"
echo ""

# Setup Backend
echo "Setting up Backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install -r requirements.txt -q

echo ""
echo "Backend setup complete!"
echo ""

# Setup Frontend
cd ../frontend
echo "Setting up Frontend..."

if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies..."
    npm install
fi

echo ""
echo "Frontend setup complete!"
echo ""

echo ""
echo "================================================"
echo "Setup Complete!"
echo "================================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Start Backend:"
echo "   - Open terminal in 'backend' folder"
echo "   - Run: source venv/bin/activate"
echo "   - Run: python app.py"
echo ""
echo "2. Start Frontend:"
echo "   - Open terminal in 'frontend' folder"
echo "   - Run: npm run dev"
echo ""
echo "3. Access Application:"
echo "   - Backend API: http://localhost:8000"
echo "   - Frontend: http://localhost:5173"
echo "   - API Docs: http://localhost:8000/docs"
echo ""
echo "4. Default Credentials:"
echo "   - Username: admin"
echo "   - Password: admin123"
echo ""
echo "================================================"
echo ""
