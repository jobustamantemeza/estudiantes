from pydantic import BaseModel, Field
from typing import Optional

class EstudianteBase(BaseModel):
    """Esquema base para estudiante con validaciones."""
    nombre: str = Field(..., min_length=1, max_length=100, description="Nombre del estudiante")
    edad: int = Field(..., ge=1, le=100, description="Edad del estudiante")
    programa: str = Field(..., min_length=1, max_length=100, description="Programa académico")

class EstudianteCrear(EstudianteBase):
    """Esquema para crear un nuevo estudiante."""
    pass

class EstudianteActualizar(EstudianteBase):
    """Esquema para actualizar un estudiante."""
    pass

class Estudiante(EstudianteBase):
    """Esquema de respuesta para un estudiante con ID."""
    id: int = Field(..., description="ID único del estudiante")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "nombre": "Juan Pérez",
                "edad": 20,
                "programa": "Ingeniería en Sistemas"
            }
        }

class RespuestaExito(BaseModel):
    """Esquema genérico para respuestas exitosas."""
    success: bool
    message: str
    data: Optional[dict] = None

class RespuestaError(BaseModel):
    """Esquema genérico para respuestas de error."""
    success: bool
    message: str
    error: Optional[str] = None
