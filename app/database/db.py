import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any

DB_PATH = Path(__file__).parent.parent.parent / "estudiantes.db"

def get_connection() -> sqlite3.Connection:
    """Obtiene una conexión a la base de datos SQLite."""
    connection = sqlite3.connect(str(DB_PATH))
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database() -> None:
    """Crea la tabla de estudiantes si no existe."""
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            programa TEXT NOT NULL
        )
    """)
    
    connection.commit()
    connection.close()
    print("✓ Base de datos inicializada correctamente")

def crear_estudiante(nombre: str, edad: int, programa: str) -> Dict[str, Any]:
    """Inserta un nuevo estudiante en la base de datos."""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            INSERT INTO estudiantes (nombre, edad, programa)
            VALUES (?, ?, ?)
        """, (nombre, edad, programa))
        
        connection.commit()
        estudiante_id = cursor.lastrowid
        connection.close()
        
        return {
            "id": estudiante_id,
            "nombre": nombre,
            "edad": edad,
            "programa": programa
        }
    except sqlite3.Error as e:
        raise Exception(f"Error al crear estudiante: {str(e)}")

def obtener_todos_estudiantes() -> List[Dict[str, Any]]:
    """Obtiene todos los estudiantes de la base de datos."""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("SELECT id, nombre, edad, programa FROM estudiantes")
        rows = cursor.fetchall()
        connection.close()
        
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        raise Exception(f"Error al obtener estudiantes: {str(e)}")

def obtener_estudiante_por_id(estudiante_id: int) -> Optional[Dict[str, Any]]:
    """Obtiene un estudiante específico por su ID."""
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(
            "SELECT id, nombre, edad, programa FROM estudiantes WHERE id = ?",
            (estudiante_id,)
        )
        row = cursor.fetchone()
        connection.close()
        
        return dict(row) if row else None
    except sqlite3.Error as e:
        raise Exception(f"Error al obtener estudiante: {str(e)}")

def actualizar_estudiante(estudiante_id: int, nombre: str, edad: int, programa: str) -> Optional[Dict[str, Any]]:
    """Actualiza los datos de un estudiante existente."""
    try:
        if not obtener_estudiante_por_id(estudiante_id):
            return None
        
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE estudiantes
            SET nombre = ?, edad = ?, programa = ?
            WHERE id = ?
        """, (nombre, edad, programa, estudiante_id))
        
        connection.commit()
        connection.close()
        
        return {
            "id": estudiante_id,
            "nombre": nombre,
            "edad": edad,
            "programa": programa
        }
    except sqlite3.Error as e:
        raise Exception(f"Error al actualizar estudiante: {str(e)}")

def eliminar_estudiante(estudiante_id: int) -> bool:
    """Elimina un estudiante de la base de datos."""
    try:
        if not obtener_estudiante_por_id(estudiante_id):
            return False
        
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute("DELETE FROM estudiantes WHERE id = ?", (estudiante_id,))
        connection.commit()
        connection.close()
        
        return True
    except sqlite3.Error as e:
        raise Exception(f"Error al eliminar estudiante: {str(e)}")
