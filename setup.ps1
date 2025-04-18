# Exit on any error
$ErrorActionPreference = "Stop"

Write-Host "Starting Django setup..."

# 1. Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install it and try again." -ForegroundColor Red
    exit 1
}

# 2. Check if pip is installed
if (-not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "pip is not installed. Please install it and try again." -ForegroundColor Red
    exit 1
}

# 3. Create a virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate the virtual environment
Write-Host "Activating virtual environment..."
& .\venv\Scripts\Activate.ps1

# 4. Upgrade pip
Write-Host "Upgrading pip..."
pip install --upgrade pip

# 5. Install dependencies
if (-not (Test-Path "requirements.txt")) {
    Write-Host "requirements.txt not found. Please make sure the file exists in the current directory." -ForegroundColor Red
    exit 1
}

Write-Host "Installing dependencies from requirements.txt..."
pip install .

# 6. Run initial migrations
Write-Host "Running initial migrations..."
python manage.py migrate

# 7. Start the Django development server
Write-Host "Starting the Django development server..."
python manage.py runserver

Write-Host "============================================="
Write-Host "Django setup complete. Visit http://127.0.0.1:8000 in your browser."
Write-Host "============================================="

# Prevent PowerShell from closing immediately
Read-Host "Press Enter to exit"
