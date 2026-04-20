# 🚀 Job Dashboard
This is a simple job dashboard that shows the latest software developer jobs from LinkedIn (last 24 hours).

It helps you quickly see jobs in different categories like:

AI/ML
Frontend
Backend
Fullstack
System / DevOps
Software

## ✨ Features
🔍 Scrapes latest LinkedIn jobs
🧠 Automatically groups jobs by type
⚡ Fast API using FastAPI
🎨 Clean frontend UI
🌙 Dark / Light mode
📱 Mobile responsive design
🔗 Click and open job directly on LinkedIn

## 📁 Project Structure
job-dashboard/
 ├── main.py          # FastAPI backend (API routes)
 ├── jobs.py          # LinkedIn scraper + job fetching logic
 ├── classifier.py    # Job category detection (AI/ML, Fullstack, etc.)
 ├── cache.py         # Stores cached jobs (faster API response)
 ├── index.html       # Frontend UI (job dashboard)
 ├── requirements.txt # Python dependencies

## 🛠️ Tech Stack
Python (FastAPI)
Playwright (for scraping)
HTML, CSS, JavaScript
rapidfuzz (for smart matching)

## 🚀 How to Run

pip install -r requirements.txt
python -m uvicorn main:app --reload

Open in browser: http://127.0.0.1:8000

## 💡 Future Ideas
Save jobs
Email alerts
Better AI filtering
React frontend upgrade


