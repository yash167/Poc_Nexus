
# 🚀 PoCForge FINAL - How to Run

## OPTION 1 — Run with Docker (Recommended)

1. Install Docker
2. Open terminal inside project folder
3. Run:

   cd docker
   docker-compose up --build

4. Open browser:
   http://localhost:8000/health

Frontend:
   cd frontend
   npm install
   npm run dev

   http://localhost:5173


## OPTION 2 — Run Backend Directly

cd backend
pip install -r requirements.txt
uvicorn pocforge.api.main:app --reload

Visit:
http://localhost:8000


## OPTION 3 — Deploy to Kubernetes

kubectl apply -f k8s/

---

Now you can test:

GET http://localhost:8000/risk/demo
GET http://localhost:8000/executive-summary/demo

---

PoCForge is ready 🚀
