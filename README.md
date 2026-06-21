# 🎲 RubiCam

> Solve your Rubik's Cube using your phone camera and intelligent solving algorithms.

RubiCam is a full-stack mobile application built with **Flutter** and **FastAPI** that helps users solve a standard 3×3 Rubik's Cube. Users can manually enter cube colors or scan the cube using their smartphone camera. The application validates the cube state, generates a solution using a solving algorithm, and provides step-by-step solving instructions.

---

## ✨ Features

### Current Features
- Manual cube state input
- Cube state validation
- FastAPI backend API
- Solution generation using Kociemba algorithm
- Flutter mobile interface

### Planned Features
- Camera-based cube scanning
- Automatic color detection using OpenCV
- Interactive 3D cube visualization
- Step-by-step solve animation
- Solve history tracking
- Statistics dashboard
- User authentication

---

## 🛠️ Tech Stack

### Frontend
- Flutter
- Dart

### Backend
- FastAPI
- Python
- Kociemba Solver
- OpenCV (Planned)

### Database
- SQLite

### Development Tools
- Git & GitHub
- VS Code
- Postman

---

## 📂 Project Structure

```text
rubicam/
│
├── backend/
│   ├── app/
│   ├── requirements.txt
│   ├── .env.example
│   └── cubesolver.db
│
├── frontend/
│   ├── lib/
│   ├── android/
│   ├── ios/
│   ├── web/
│   ├── test/
│   └── pubspec.yaml
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/rubicam.git
cd rubicam
```

### 2. Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend API:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

### 3. Frontend Setup

```bash
cd frontend

flutter pub get

flutter run
```

---

## 📋 Development Roadmap

### Phase 1
- [x] Project setup
- [x] FastAPI backend
- [x] Flutter frontend
- [ ] Manual cube input
- [ ] Cube validation
- [ ] Cube solving API

### Phase 2
- [ ] Camera integration
- [ ] OpenCV color detection
- [ ] Automatic cube scanning

### Phase 3
- [ ] 3D cube visualization
- [ ] Solution animations
- [ ] Solve history

### Phase 4
- [ ] Authentication
- [ ] User profiles
- [ ] Analytics dashboard

---

## 🎯 Project Goals

RubiCam aims to provide an intuitive and educational Rubik's Cube solving experience by combining:

- Mobile development
- Backend API development
- Computer vision
- Algorithmic problem solving
- Interactive user interfaces

---

## 👨‍💻 Author

**Kavindu Chandupa**

Software Engineering Undergraduate  
Informatics Institute of Technology (IIT) Sri Lanka  
University of Westminster

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you find this project interesting, consider giving it a star on GitHub.