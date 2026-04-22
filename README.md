# 🩺 E-Doctor — FastAPI Edition

AI-powered disease prediction web app with a beautiful medical dashboard UI.

---

## 📁 Folder Structure

```
edoctor/
│
├── main.py                  ← FastAPI application (all routes & API)
├── requirements.txt         ← Python dependencies
│
├── models/                  ← 🔴 Apne trained .sav files yahan rakhein
│   ├── Diabetes.sav
│   ├── Heart.sav
│   └── Parkinsons.sav
│
├── templates/
│   └── index.html           ← Beautiful frontend UI
│
└── static/                  ← CSS/JS/Images (future use)
    ├── css/
    ├── js/
    └── images/
```

---

## ⚙️ Setup & Run

### 1. Dependencies install karein
```bash
pip install -r requirements.txt
```

### 2. Models folder mein apni .sav files rakhein
```
models/Diabetes.sav
models/Heart.sav
models/Parkinsons.sav
```

### 3. Server start karein
```bash
uvicorn main:app --reload
```

### 4. Browser mein kholein
```
http://localhost:8000
```

---

## 🌐 API Endpoints

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| GET    | `/`                  | Beautiful frontend UI     |
| POST   | `/predict/diabetes`  | Diabetes prediction       |
| POST   | `/predict/heart`     | Heart disease prediction  |
| POST   | `/predict/parkinsons`| Parkinson's prediction    |

### Example API Call (Diabetes)
```bash
curl -X POST http://localhost:8000/predict/diabetes \
  -H "Content-Type: application/json" \
  -d '{"pregnancies":2,"glucose":138,"blood_pressure":62,"skin_thickness":35,"insulin":0,"bmi":33.6,"dpf":0.627,"age":47}'
```

### Response
```json
{
  "prediction": 1,
  "label": "Diabetic",
  "status": "positive"
}
```

---

## 🎨 Features
- ✅ Animated ECG background strip
- ✅ Floating health icons
- ✅ Glassmorphism card design
- ✅ 3 disease prediction tabs
- ✅ Real-time API calls (no page reload)
- ✅ Color-coded results (green = healthy, red = detected)
- ✅ Fully responsive (mobile friendly)
- ✅ Auto API docs at `/docs` (FastAPI Swagger)
