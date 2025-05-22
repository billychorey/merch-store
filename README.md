# 🛍️ Merch Store

**A full-stack merch store built with React (frontend) and Flask (backend).**  
Clean code, responsive design, and just the right amount of calm energy.

> “Clear code, calm energy — with a hint of drip.”

---

## 📦 Overview

This is a two-part application:
- **Frontend**: React + Tailwind CSS (via Vite)
- **Backend**: Python Flask + SQLAlchemy

Designed as a minimalist, extendable e-commerce platform. Think starter kit for a merch shop — ideal for solo creators, pop-up brands, or portfolio projects.

---

## 🛠 Tech Stack

### Frontend:
- React
- Tailwind CSS
- Vite
- React Router

### Backend:
- Python 3.8+
- Flask
- SQLAlchemy
- Marshmallow (optional)

---

## ✨ Features

- Product list rendered via dynamic `ProductCard` components
- Responsive UI with Tailwind styling
- Backend routes for creating and managing products — with room to grow (carts, users, etc.)
- Built to be extended with authentication, checkout flows, and admin views

---

## 🚀 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/billychorey/merch-store.git
   ```

2. **Install frontend dependencies**
   ```bash
   cd merch-store-tailwind
   npm install
   ```

3. **Install backend dependencies**
   ```bash
   cd ../merch-store-backend
   pipenv install
   ```

4. **Run the apps**
   - Frontend:
     ```bash
     cd merch-store-tailwind
     npm run dev
     ```
   - Backend:
     ```bash
     cd merch-store-backend
     pipenv shell
     python app.py
     ```

---

## 🗂 Folder Structure

```
merch-store/
├── merch-store-backend/     # Flask backend
├── merch-store-tailwind/    # React frontend
├── README.md
└── LICENSE
```

---

## 📸 Optional

You can add a screenshot or demo link here later:

```markdown
![Merch Store Screenshot](screenshot.png)

[Live Demo](https://your-live-url.com)
```

---

Feel free to reach out or contribute. Built with calm energy and tested on a terrier.
