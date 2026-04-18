# The Sandras - Full Stack Application

This is a full-stack application for "The Sandars" village development, featuring a React/TanStack frontend and a FastAPI/MongoDB backend.

## 🚀 Quick Start

The project is designed to be set up automatically on any system (Windows, Mac, Linux).

### Prerequisites
- **Python 3.8+**
- **Node.js 18+**
- **MongoDB** (Local instance or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))

### Setup
1. Clone the repository.
2. Open a terminal in the project root.
3. Configure your environment:
   - Go to `backend/`
   - Copy `.env.example` to `.env`
   - Paste your MongoDB connection string in `.env`.
4. Run the orchestration script:
   ```bash
   python app.py
   ```

**The script will automatically:**
- Install backend dependencies (`pip install`).
- Install frontend dependencies (`npm install`).
- Start the FastAPI backend on `http://localhost:8000`.
- Start the Vite/React frontend on `http://localhost:8080`.

## 📂 Project Structure
- `frontend/`: React application using TanStack Start & Router.
- `backend/`: FastAPI application with MongoDB integration.
- `app.py`: Cross-platform orchestration script.

## 🛠️ Tech Stack
- **Frontend**: React, TanStack, Tailwind CSS, Vite.
- **Backend**: FastAPI, MongoDB (Motor), Pydantic.
- **Orchestration**: Python Subprocess.

## 🧪 Testing
- **API Health**: `http://localhost:8000/api/health`
- **Inquiries API**: `http://localhost:8000/api/inquiries`
