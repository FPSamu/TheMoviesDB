"""
Script de ejemplo para probar la API de búsqueda de películas
Puedes ejecutar esto después de que la API esté corriendo
"""

import requests

# URL base de nuestra API
BASE_URL = "http://localhost:8000"

def test_root():
    """Probar el endpoint raíz"""
    print("=" * 50)
    print("Probando endpoint raíz (/)...")
    print("=" * 50)
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_health():
    """Probar el health check"""
    print("=" * 50)
    print("Probando health check...")
    print("=" * 50)
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def search_movie(query, page=1, language="es-MX"):
    """Buscar películas"""
    print("=" * 50)
    print(f"Buscando películas: '{query}'")
    print("=" * 50)
    
    params = {
        "query": query,
        "page": page,
        "language": language
    }
    
    response = requests.get(f"{BASE_URL}/search/movie", params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Total de resultados: {data['total_results']}")
        print(f"Página: {data['page']} de {data['total_pages']}")
        print(f"\nPelículas encontradas ({len(data['results'])}):\n")
        
        for i, movie in enumerate(data['results'][:5], 1):  # Mostrar solo las primeras 5
            print(f"{i}. {movie['title']} ({movie.get('release_date', 'N/A')[:4]})")
            print(f"   Rating: ⭐ {movie.get('vote_average', 0):.1f}/10")
            print(f"   Sinopsis: {movie.get('overview', 'No disponible')[:100]}...")
            if movie.get('poster_path'):
                print(f"   Poster: https://image.tmdb.org/t/p/w500{movie['poster_path']}")
            print()
    else:
        print(f"Error {response.status_code}: {response.text}")
    print()

def main():
    print("\n🎬 PRUEBAS DE LA API DE BÚSQUEDA DE PELÍCULAS 🎬\n")
    
    # Pruebas básicas
    test_root()
    test_health()
    
    # Búsquedas de ejemplo
    search_movie("Matrix")
    search_movie("Avengers")
    search_movie("El Padrino")
    
    # Búsqueda interactiva
    print("=" * 50)
    print("Búsqueda interactiva")
    print("=" * 50)
    user_query = input("Ingresa el título de una película para buscar: ")
    if user_query:
        search_movie(user_query)

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: No se puede conectar a la API.")
        print("Asegúrate de que la API esté corriendo en http://localhost:8000")
        print("Ejecuta: python main.py")
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
