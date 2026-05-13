# 🚀 LinkedIn Job Feed

A modern SaaS-style job discovery platform that showcases the latest LinkedIn software engineering jobs from the past 24 hours.

Built with FastAPI + Playwright, this project provides a fast, clean, and distraction-free experience for browsing curated developer opportunities across multiple tech domains.

---

# ✨ Features

* 🔍 Scrapes latest LinkedIn job listings automatically
* 🧠 Smart job classification by role/category
* ⚡ Fast backend API powered by FastAPI
* 🎨 Modern SaaS-inspired UI
* 🌙 Dark / Light theme toggle
* 📱 Fully responsive design
* 🔗 Direct LinkedIn job links
* 🧩 Role-based filtering system
* ⬆️ Smooth scroll-to-top floating button
* 💎 Professional card-based job layout

---

# 🧠 Supported Job Categories

* AI / ML
* Frontend
* Backend
* Fullstack
* System / DevOps
* Software Engineering

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* Playwright

## Frontend

* HTML
* CSS
* JavaScript

## Utilities

* rapidfuzz (smart keyword matching / classification)

---

# 📁 Project Structure

```bash
job-dashboard/
│
├── main.py            # FastAPI backend + API routes
├── jobs.py            # LinkedIn scraper & job fetching logic
├── classifier.py      # Smart job role classification
├── cache.py           # Job caching layer for faster responses
├── index.html         # Frontend SaaS dashboard UI
├── requirements.txt   # Python dependencies
│
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Start the FastAPI server

```bash
python -m uvicorn main:app --reload
```

---

## 3️⃣ Open in browser

```bash
http://127.0.0.1:8000
```

---

# 💡 UI Highlights

* Modern gradient hero section
* Floating SaaS-style controls
* Interactive hover animations
* Responsive job card grid
* Smooth dark/light mode switching
* Minimal and clean browsing experience

---

# 📸 Preview

<img width="1905" height="873" alt="image" src="https://github.com/user-attachments/assets/88ca87df-f24a-4556-a5bd-aa0f799e814d" />

