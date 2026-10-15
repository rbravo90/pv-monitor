from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PV Monitor API",
    description="API para monitoreo, optimización y predicción de fallas en sistemas fotovoltaicos de pequeña y mediana escala",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajustar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "PV Monitor API - Sistemas de pequeña y mediana escala"}

@app.get("/health")
def health():
    return {"status": "ok"}