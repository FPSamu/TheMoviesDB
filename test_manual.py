"""
Script para probar la API sin levantar servidor
Usando TestClient de FastAPI para simular requests
"""

from fastapi.testclient import TestClient
from main import app, Movie, SearchResponse
import json

# Crear cliente de prueba (no necesita servidor corriendo)
client = TestClient(app)

print("=" * 80)
print("PRUEBAS SIN SERVIDOR - Usando TestClient de FastAPI")
print("=" * 80)
print()

# ============================================================================
# 1. PRUEBA DE MODELOS PYDANTIC (Instancias directas)
# ============================================================================

print("1️⃣  PROBANDO MODELOS PYDANTIC DIRECTAMENTE")
print("-" * 80)

# Crear instancia de Movie manualmente
movie_data = {
    "id": 603,
    "title": "The Matrix",
    "original_title": "The Matrix",
    "overview": "Un hacker descubre la verdad sobre su realidad...",
    "release_date": "1999-03-31",
    "poster_path": "/path/to/poster.jpg",
    "backdrop_path": "/path/to/backdrop.jpg",
    "vote_average": 8.7,
    "vote_count": 25000,
    "popularity": 95.5
}

# Instanciar el modelo Movie
movie = Movie(**movie_data)

print(f"✅ Película creada: {movie.title}")
print(f"   ID: {movie.id}")
print(f"   Rating: {movie.vote_average}/10")
print(f"   Fecha: {movie.release_date}")
print(f"   Overview: {movie.overview[:50]}...")
print()

# Convertir a JSON
print("📄 Convertir a JSON:")
print(json.dumps(movie.model_dump(), indent=2, ensure_ascii=False))
print()

# Crear instancia de SearchResponse
response_data = {
    "page": 1,
    "total_results": 42,
    "total_pages": 3,
    "results": [movie, movie]  # Lista de películas
}

search_response = SearchResponse(**response_data)
print(f"✅ Respuesta de búsqueda creada:")
print(f"   Total resultados: {search_response.total_results}")
print(f"   Películas en resultados: {len(search_response.results)}")
print()
