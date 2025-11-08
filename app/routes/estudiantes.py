from fastapi import APIRouter, HTTPException, status
from app.schemas import EstudianteCrear, EstudianteActualizar, RespuestaExito
from app.database import (
    crear_estudiante,
    obtener_todos_estudiantes,
    obtener_estudiante_por_id,
    actualizar_estudiante,
    eliminar_estudiante
)

router = APIRouter(
    prefix="/estudiantes",
    tags=["Estudiantes"],
    responses={404: {"description": "No encontrado"}}
)

@router.post("", response_model=RespuestaExito, status_code=status.HTTP_201_CREATED)
async def crear(estudiante: EstudianteCrear):
    """Crear un nuevo estudiante"""
    try:
        nuevo = crear_estudiante(estudiante.nombre, estudiante.edad, estudiante.programa)
        return RespuestaExito(success=True, message="Estudiante creado", data=nuevo)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=RespuestaExito)
async def listar():
    """Listar todos los estudiantes"""
    try:
        estudiantes = obtener_todos_estudiantes()
        return RespuestaExito(
            success=True,
            message=f"Se encontraron {len(estudiantes)} estudiante(s)",
            data={"estudiantes": estudiantes}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{estudiante_id}", response_model=RespuestaExito)
async def obtener(estudiante_id: int):
    """Obtener un estudiante por ID"""
    try:
        est = obtener_estudiante_por_id(estudiante_id)
        if not est:
            raise HTTPException(status_code=404, detail=f"Estudiante {estudiante_id} no encontrado")
        return RespuestaExito(success=True, message="Encontrado", data=est)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{estudiante_id}", response_model=RespuestaExito)
async def actualizar(estudiante_id: int, estudiante: EstudianteActualizar):
    """Actualizar un estudiante"""
    try:
        actualizado = actualizar_estudiante(estudiante_id, estudiante.nombre, estudiante.edad, estudiante.programa)
        if not actualizado:
            raise HTTPException(status_code=404, detail=f"Estudiante {estudiante_id} no encontrado")
        return RespuestaExito(success=True, message="Actualizado", data=actualizado)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{estudiante_id}", response_model=RespuestaExito)
async def eliminar(estudiante_id: int):
    """Eliminar un estudiante"""
    try:
        fue_eliminado = eliminar_estudiante(estudiante_id)
        if not fue_eliminado:
            raise HTTPException(status_code=404, detail=f"Estudiante {estudiante_id} no encontrado")
        return RespuestaExito(success=True, message=f"Estudiante {estudiante_id} eliminado")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
