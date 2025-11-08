"""Pruebas de la API"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    END = '\033[0m'

def test_health():
    """Test health check"""
    print(f"\n{Colors.BLUE}🧪 Health Check{Colors.END}")
    resp = requests.get(f"{BASE_URL}/health")
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 200

def test_crear():
    """Test crear estudiante"""
    print(f"\n{Colors.BLUE}🧪 Crear Estudiante{Colors.END}")
    data = {"nombre": "Juan Pérez", "edad": 20, "programa": "Ingeniería"}
    resp = requests.post(f"{BASE_URL}/estudiantes", json=data)
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 201
    return resp.json()["data"]["id"]

def test_listar():
    """Test listar"""
    print(f"\n{Colors.BLUE}🧪 Listar Estudiantes{Colors.END}")
    resp = requests.get(f"{BASE_URL}/estudiantes")
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 200

def test_obtener(est_id):
    """Test obtener por ID"""
    print(f"\n{Colors.BLUE}🧪 Obtener por ID ({est_id}){Colors.END}")
    resp = requests.get(f"{BASE_URL}/estudiantes/{est_id}")
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 200

def test_actualizar(est_id):
    """Test actualizar"""
    print(f"\n{Colors.BLUE}🧪 Actualizar ({est_id}){Colors.END}")
    data = {"nombre": "Juan Updated", "edad": 21, "programa": "Software"}
    resp = requests.put(f"{BASE_URL}/estudiantes/{est_id}", json=data)
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 200

def test_eliminar(est_id):
    """Test eliminar"""
    print(f"\n{Colors.BLUE}🧪 Eliminar ({est_id}){Colors.END}")
    resp = requests.delete(f"{BASE_URL}/estudiantes/{est_id}")
    print(f"Status: {resp.status_code}")
    print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    assert resp.status_code == 200

def main():
    """Ejecutar todas las pruebas"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.GREEN}🚀 Iniciando Pruebas{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    
    try:
        test_health()
        est_id = test_crear()
        test_listar()
        test_obtener(est_id)
        test_actualizar(est_id)
        test_eliminar(est_id)
        
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.GREEN}✅ Todas las pruebas pasaron{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Error: {str(e)}{Colors.END}\n")

if __name__ == "__main__":
    main()
