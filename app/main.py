from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import initialize_database
from app.routes import router

# Inicializar base de datos
initialize_database()

# Crear app
app = FastAPI(
    title="API Registro de Estudiantes",
    description="Sistema REST para gestionar estudiantes",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(router)

@app.get("/")
async def root():
    """Bienvenida"""
    return {
        "message": "API Registro de Estudiantes",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health():
    """Health check"""
    return {"status": "ok"}
