# 📚 API REST de Registro de Estudiantes

API moderna y profesional para gestionar estudiantes con **FastAPI**, **SQLite** y arquitectura en capas. Completa con validación automática, documentación interactiva y ejemplos prácticos.

---


### 1️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2️⃣ Ejecutar la API

```bash
python app/main.py
```

O directamente con uvicorn:

```bash
uvicorn app.main:app --reload
```

### 3️⃣ Acceder a la API

📚 **Swagger UI (Recomendado - Interfaz Interactiva):**
```
http://127.0.0.1:8000/docs
```

📖 **ReDoc (Documentación Estática):**
```
http://127.0.0.1:8000/redoc
```

---

## 📁 Estructura del Proyecto

```
aca_pw/
├── app/                          # 📦 Código principal
│   ├── main.py                   # ⚙️ Inicialización FastAPI
│   ├── database/
│   │   └── db.py                 # 💾 Operaciones SQLite
│   ├── routes/
│   │   └── estudiantes.py        # 🔄 Endpoints CRUD
│   ├── schemas/
│   │   └── estudiante.py         # 📋 Esquemas Pydantic
│   ├── models/                   # 📊 Modelos de datos
│   └── utils/                    # 🛠️ Utilidades
│
├── tests/
│   └── test_api.py               # 🧪 Pruebas automatizadas
│
│── README.md                 # Este archivo
└── requirements.txt          # Dependencias
```

---

## 🔌 Endpoints Disponibles

### Operaciones CRUD

| Método | Endpoint | Status | Descripción |
|--------|----------|--------|-------------|
| **POST** | `/estudiantes` | 201 | Crear nuevo estudiante |
| **GET** | `/estudiantes` | 200 | Listar todos los estudiantes |
| **GET** | `/estudiantes/{id}` | 200 | Obtener estudiante por ID |
| **PUT** | `/estudiantes/{id}` | 200 | Actualizar estudiante |
| **DELETE** | `/estudiantes/{id}` | 200 | Eliminar estudiante |

### Utilidad

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| **GET** | `/` | Información de la API |
| **GET** | `/health` | Health check |
| **GET** | `/docs` | Swagger UI |
| **GET** | `/redoc` | ReDoc |

---

## 📊 Campos del Estudiante

| Campo | Tipo | Validación | Descripción |
|-------|------|-----------|-------------|
| **id** | `int` | Auto (PK) | ID único |
| **nombre** | `string` | 1-100 caracteres | Nombre completo |
| **edad** | `int` | 1-100 | Edad en años |
| **programa** | `string` | 1-100 caracteres | Programa académico |

---

## 📝 Ejemplos Prácticos

### ✨ Health Check

Verifica que la API está funcionando:

```bash
curl -X GET "http://127.0.0.1:8000/health"
```

**Respuesta:**
```json
{
  "status": "healthy",
  "message": "La API está funcionando correctamente"
}
```

---

### ➕ CREATE - Crear Estudiante

```bash
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Pérez",
    "edad": 20,
    "programa": "Ingeniería en Sistemas"
  }'
```

**Respuesta (HTTP 201):**
```json
{
  "success": true,
  "message": "Estudiante creado exitosamente",
  "data": {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 20,
    "programa": "Ingeniería en Sistemas"
  }
}
```

---

### 📖 READ - Listar Todos

```bash
curl -X GET "http://127.0.0.1:8000/estudiantes"
```

**Respuesta (HTTP 200):**
```json
{
  "success": true,
  "message": "Se encontraron 3 estudiante(s)",
  "data": {
    "estudiantes": [
      {
        "id": 1,
        "nombre": "Juan Pérez",
        "edad": 20,
        "programa": "Ingeniería en Sistemas"
      },
      {
        "id": 2,
        "nombre": "María García",
        "edad": 22,
        "programa": "Administración de Empresas"
      },
      {
        "id": 3,
        "nombre": "Carlos López",
        "edad": 21,
        "programa": "Ingeniería Civil"
      }
    ]
  }
}
```

Con formato mejorado usando `jq`:
```bash
curl -s "http://127.0.0.1:8000/estudiantes" | jq '.data.estudiantes'
```

---

### 🔍 READ - Obtener por ID

```bash
curl -X GET "http://127.0.0.1:8000/estudiantes/1"
```

**Respuesta (HTTP 200):**
```json
{
  "success": true,
  "message": "Estudiante encontrado",
  "data": {
    "id": 1,
    "nombre": "Juan Pérez",
    "edad": 20,
    "programa": "Ingeniería en Sistemas"
  }
}
```

**Si no existe (HTTP 404):**
```bash
curl -X GET "http://127.0.0.1:8000/estudiantes/999"
```

```json
{
  "detail": "Estudiante 999 no encontrado"
}
```

---

### ✏️ UPDATE - Actualizar Estudiante

```bash
curl -X PUT "http://127.0.0.1:8000/estudiantes/1" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan Carlos Pérez",
    "edad": 21,
    "programa": "Ingeniería de Software"
  }'
```

**Respuesta (HTTP 200):**
```json
{
  "success": true,
  "message": "Estudiante actualizado exitosamente",
  "data": {
    "id": 1,
    "nombre": "Juan Carlos Pérez",
    "edad": 21,
    "programa": "Ingeniería de Software"
  }
}
```

---

### 🗑️ DELETE - Eliminar Estudiante

```bash
curl -X DELETE "http://127.0.0.1:8000/estudiantes/1"
```

**Respuesta (HTTP 200):**
```json
{
  "success": true,
  "message": "Estudiante con ID 1 eliminado exitosamente"
}
```

Verificar que fue eliminado:
```bash
curl -X GET "http://127.0.0.1:8000/estudiantes/1"
```

```json
{
  "detail": "Estudiante 1 no encontrado"
}
```

---

## ⚠️ Errores y Validación

### Edad Fuera del Rango

```bash
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Test",
    "edad": 150,
    "programa": "Test"
  }'
```

**Respuesta (HTTP 422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "edad"],
      "msg": "ensure this value is less than or equal to 100",
      "type": "value_error.number.not_le",
      "ctx": {
        "limit_value": 100
      }
    }
  ]
}
```

### Nombre Vacío

```bash
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "",
    "edad": 20,
    "programa": "Test"
  }'
```

**Respuesta (HTTP 422):**
```json
{
  "detail": [
    {
      "loc": ["body", "nombre"],
      "msg": "ensure this value has at least 1 characters",
      "type": "value_error.string.too_short"
    }
  ]
}
```

### Campo Requerido Faltante

```bash
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "edad": 20
  }'
```

**Respuesta (HTTP 422):**
```json
{
  "detail": [
    {
      "loc": ["body", "programa"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

### Tipo de Dato Incorrecto

```bash
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Juan",
    "edad": "veinte",
    "programa": "Test"
  }'
```

**Respuesta (HTTP 422):**
```json
{
  "detail": [
    {
      "loc": ["body", "edad"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

---

## 🧪 Testing

### Pruebas Automatizadas

Ejecuta la suite completa de pruebas (mientras el servidor está corriendo):

```bash
python tests/test_api.py
```

Esto prueba:
- ✅ Health check
- ✅ Crear estudiante válido
- ✅ Listar todos
- ✅ Obtener por ID
- ✅ Actualizar existente
- ✅ Error 404 (no existe)
- ✅ Error 422 (validación falla)
- ✅ Eliminar

### Pruebas en Swagger UI

1. Abre http://127.0.0.1:8000/docs
2. Haz clic en un endpoint
3. Llena los parámetros
4. Haz clic en "Try it out"
5. Revisa la respuesta

---

## 🔧 Opciones Útiles de cURL

### Mostrar headers de respuesta

```bash
curl -i "http://127.0.0.1:8000/estudiantes"
```

### Mostrar solo el código de estado

```bash
curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:8000/estudiantes"
```

### Guardar respuesta en archivo

```bash
curl -X GET "http://127.0.0.1:8000/estudiantes" > estudiantes.json
```

### Ver detalles de la conexión

```bash
curl -v "http://127.0.0.1:8000/estudiantes"
```

### OpenAPI JSON

```bash
curl "http://127.0.0.1:8000/openapi.json" | jq
```

---

## 📚 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|-----------|---------|-----------|
| **FastAPI** | 0.104.1 | Framework web asincrónico moderno |
| **Uvicorn** | 0.24.0 | Servidor ASGI de producción |
| **Pydantic** | 2.5.0 | Validación automática de datos |
| **SQLite3** | Nativo | Base de datos relacional |
| **Python** | 3.7+ | Lenguaje de programación |
| **Requests** | 2.31.0 | Cliente HTTP para testing |

---

## 🏗️ Arquitectura en Capas

```
┌─────────────────────────────────────────┐
│ 1️⃣  Capa de Presentación                │
│    • FastAPI initialization             │
│    • CORS configuration                 │
│    • Health check endpoints             │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 2️⃣  Capa de Rutas                      │
│    • HTTP endpoints                     │
│    • Request/Response handling          │
│    • Business logic wrapping            │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 3️⃣  Capa de Esquemas                   │
│    • Pydantic models                    │
│    • Data validation                    │
│    • Auto documentation                 │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 4️⃣  Capa de Datos                      │
│    • SQLite operations                  │
│    • CRUD functions                     │
│    • Connection management              │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ 💾 Base de Datos (SQLite)               │
│    • estudiantes table                  │
│    • Persistent storage                 │
└─────────────────────────────────────────┘
```

**Beneficios:**
- ✅ Separación clara de responsabilidades
- ✅ Fácil mantenimiento y escalabilidad
- ✅ Testeable y reutilizable
- ✅ Cambios sin efectos secundarios

---

## ✨ Características Destacadas

### ✅ Validación Automática

Pydantic valida automáticamente:
- Tipos de datos
- Rangos y longitudes
- Campos requeridos
- Formato de respuesta

### ✅ Documentación Automática

FastAPI genera automáticamente:
- Swagger UI (interfaz interactiva)
- ReDoc (documentación estática)
- OpenAPI specification
- Schemas JSON

### ✅ Seguridad

- 🛡️ SQL injection prevention (queries parametrizadas)
- 🛡️ Data validation
- 🛡️ CORS configurado
- 🛡️ Manejo robusto de errores
- 🛡️ Códigos HTTP apropiados

### ✅ Rendimiento

- ⚡ Async/await para no bloquear
- ⚡ Uvicorn servidor ASGI
- ⚡ Soporta múltiples solicitudes simultáneas
- ⚡ Ligero y eficiente

### ✅ Testing

- 🧪 Pruebas automatizadas incluidas
- 🧪 Cobertura completa de endpoints
- 🧪 Casos de error validados
- 🧪 Fácil de extender

---

## 🚀 Flujo Completo de Ejemplo

```bash
# 1. Verificar que la API está corriendo
curl "http://127.0.0.1:8000/health"

# 2. Crear primer estudiante
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan","edad":20,"programa":"Ingeniería"}' > resp1.json

# 3. Listar todos los estudiantes
curl "http://127.0.0.1:8000/estudiantes"

# 4. Obtener el estudiante que acabamos de crear
curl "http://127.0.0.1:8000/estudiantes/1"

# 5. Crear más estudiantes
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"María","edad":22,"programa":"Administración"}'

curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Carlos","edad":21,"programa":"Derecho"}'

# 6. Actualizar un estudiante
curl -X PUT "http://127.0.0.1:8000/estudiantes/1" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan Updated","edad":21,"programa":"Software"}'

# 7. Obtener actualizado
curl "http://127.0.0.1:8000/estudiantes/1"

# 8. Listar todos nuevamente
curl "http://127.0.0.1:8000/estudiantes"

# 9. Eliminar un estudiante
curl -X DELETE "http://127.0.0.1:8000/estudiantes/1"

# 10. Verificar que fue eliminado
curl "http://127.0.0.1:8000/estudiantes/1"  # 404 Not Found
```

---

## 📖 Documentación Adicional

Para información más detallada sobre la implementación:

- **[ARQUITECTURA.md](ARQUITECTURA.md)** - Explicación de la arquitectura en capas y principios SOLID
- **[DOCUMENTACION_TECNICA.md](DOCUMENTACION_TECNICA.md)** - Guía técnica completa con explicación de cada ruta

---

## ⚙️ Configuración

### Variables de Entorno

Actualmente usa configuración por defecto. Para producción:

```python
# app/main.py
CORS_ORIGINS = ["https://tu-dominio.com"]  # En producción
DEBUG = False  # En producción
```

### Puerto y Host

```bash
# Cambiar puerto y host
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

---

## 🐛 Troubleshooting

### Error: ModuleNotFoundError: No module named 'fastapi'

**Solución:** Instala las dependencias
```bash
pip install -r requirements.txt
```

### Error: Port 8000 is already in use

**Solución:** Usa otro puerto
```bash
uvicorn app.main:app --port 8001
```

### Error: Database locked

**Solución:** Cierra otras conexiones y reinicia
```bash
rm app/database/estudiantes.db  # Opcional: borra la BD
python app/main.py
```

---

## 🎯 Próximos Pasos

Mejoras sugeridas para un entorno de producción:

1. **Autenticación** - Implementar JWT o OAuth2
2. **Base de Datos** - Migrar a PostgreSQL
3. **ORM** - Usar SQLAlchemy
4. **Testing** - Pytest con cobertura completa
5. **Logging** - ELK o Datadog
6. **Caching** - Redis para datos frecuentes
7. **Paginación** - Para grandes conjuntos de datos
8. **Rate Limiting** - Prevenir abuso
9. **CI/CD** - GitHub Actions, GitLab CI
10. **Deployment** - Docker, Kubernetes

---

## 📄 Licencia

Proyecto educativo - Uso libre

---

## 📞 Soporte

Para reportar bugs o sugerir mejoras:
1. Revisa los logs de la consola
2. Usa Swagger UI para debug interactivo
3. Ejecuta los tests para verificar funcionamiento

---

## ✨ Resumen Rápido

```bash
# Instalación
pip install -r requirements.txt

# Ejecutar
python app/main.py

# Documentación
http://127.0.0.1:8000/docs

# Testing
python tests/test_api.py

# Ejemplo: Crear estudiante
curl -X POST "http://127.0.0.1:8000/estudiantes" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Juan","edad":20,"programa":"Ingeniería"}'
```

---

**¡API lista para usar! 🚀**

Para comenzar: instala dependencias y ejecuta `python app/main.py`
