# HK Stock Price Check

This is not deployed yet, only for localhosting.

To run on local server, run the following commands:

## How to start and run the website in the localhost

### Backend (Django)

Navigate into backend folder

    cd Backend-Django

Initiate virtual environment
(windows)

    python -m venv .env
    .env/Scripts/activate
    pip install -r requirements.txt

(macos/linux)

    python3 -m venv .env
    source .env/bin/activate
    pip3 install -r requirements.txt

Run the server

    python manage.py runserver

### Frontend (Vue)

Navigate into frontend folder

    cd Frontend-Vue

Install required packages

    yarn install

Start the frontend browser

    yarn serve

Then, open <localhost:8080>

## Features of the website

1. User Authentication system  
   Users records are stored in database, with jwt as authentication token to fetch stock data
2. Records of lastest 3 months of 5 stock prices
3. Easy and user friendly UI/UX

## Areas of improvement for the website

1. Users' passwords should be hashed in database
2. Stock Data should be fetched from realtime api
3. Should use other database like postgreSQL for long-term saving of stock data
