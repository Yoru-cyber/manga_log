#!/bin/bash

# Exit on any error
set -e

echo "Starting Django setup..."

# 1. Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi

# 2. Check if pip is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 is not installed. Please install it and try again."
    exit 1
fi

# 3. Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 4. Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 5. Install Django
echo "Installing dependencies..."
pip install -r requirements.txt

# 6. Run initial migrations
echo "Running initial migrations..."
python manage.py migrate

# 7. Start the Django development server
echo "Starting the Django development server..."
python manage.py runserver

echo "Django setup complete. Visit http://127.0.0.1:8000 in your browser."
