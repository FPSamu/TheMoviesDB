# TheMovieDB Search API

API desarrollada con FastAPI que permite buscar películas usando la API de TheMovieDB.

## 🚀 Características

- 🔍 Búsqueda de películas por título
- 🌐 Soporte multiidioma (por defecto: español de México)
- 📄 Paginación de resultados
- 📚 Documentación automática con Swagger UI
- ✅ Validación de datos con Pydantic
- 🔒 Manejo seguro de API keys con variables de entorno

## 📋 Requisitos

- Python 3.8 o superior
- Una API key de TheMovieDB (Read Access Token)

## 🔑 Obtener tu API Key

1. Crea una cuenta en [TheMovieDB](https://www.themoviedb.org/)
2. Ve a tu perfil → Settings → [API](https://www.themoviedb.org/settings/api)
3. Solicita un API key (selecciona "Developer" si te preguntan)
4. Copia el **"API Read Access Token"** (es el Bearer token, NO el API Key v3)

## 🛠️ Instalación

1. **Clona o descarga este proyecto**

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configura tu API key:**

Copia el archivo `.env.example` a `.env`:
```bash
cp .env.example .env
```

Edita el archivo `.env` y reemplaza `tu_api_key_aqui` con tu API Read Access Token de TheMovieDB:
```
TMDB_API_KEY=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI...
```

## ▶️ Ejecución

Ejecuta la aplicación con:

```bash
python main.py
```

O con uvicorn directamente:

```bash
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📖 Uso de la API

### Endpoints disponibles

#### 1. Endpoint raíz
```
GET /
```
Retorna información básica de la API.

**Ejemplo:**
```bash
curl http://localhost:8000/
```

#### 2. Buscar películas
```
GET /search/movie?query={titulo}
```

**Parámetros:**
- `query` (requerido): Título de la película a buscar
- `page` (opcional): Número de página (default: 1)
- `language` (opcional): Idioma de resultados (default: "es-MX")
- `include_adult` (opcional): Incluir contenido para adultos (default: false)

**Ejemplo:**
```bash
# Búsqueda simple
curl "http://localhost:8000/search/movie?query=Matrix"

# Búsqueda con parámetros adicionales
curl "http://localhost:8000/search/movie?query=Avengers&page=1&language=es-MX"
```

**Respuesta:**
```json
{
  "page": 1,
  "total_results": 42,
  "total_pages": 3,
  "results": [
    {
      "id": 603,
      "title": "The Matrix",
      "original_title": "The Matrix",
      "overview": "Thomas Anderson lleva una doble vida...",
      "release_date": "1999-03-30",
      "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
      "backdrop_path": "/fNG7i7RqMErkcqhohV2a6cV1Ehy.jpg",
      "vote_average": 8.2,
      "vote_count": 23000,
      "popularity": 85.5
    }
  ]
}
```

#### 3. Health check
```
GET /health
```
Verifica el estado de la API y si la API key está configurada.

**Ejemplo:**
```bash
curl http://localhost:8000/health
```

### 📚 Documentación interactiva

FastAPI genera automáticamente documentación interactiva:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Puedes probar todos los endpoints directamente desde estas interfaces.

## 🖼️ Construcción de URLs de imágenes

Los campos `poster_path` y `backdrop_path` retornan rutas relativas. Para obtener la URL completa de las imágenes:

```
https://image.tmdb.org/t/p/{tamaño}{poster_path}
```

**Tamaños disponibles:**
- Posters: `w92`, `w154`, `w185`, `w342`, `w500`, `w780`, `original`
- Backdrops: `w300`, `w780`, `w1280`, `original`

**Ejemplo:**
```
https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg
```

## 🛡️ Manejo de errores

La API retorna códigos de estado HTTP apropiados:

- `200 OK`: Solicitud exitosa
- `400 Bad Request`: Parámetros inválidos
- `500 Internal Server Error`: Error de configuración (API key no configurada)
- `503 Service Unavailable`: Error de conexión con TheMovieDB

## 📝 Estructura del proyecto

```
TheMovieDB/
├── main.py              # Aplicación FastAPI principal
├── requirements.txt     # Dependencias de Python
├── .env.example        # Ejemplo de configuración
├── .env                # Tu configuración (no incluir en git)
├── .gitignore          # Archivos a ignorar en git
└── README.md           # Esta documentación
```

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de experimentar y mejorarlo.

## 📄 Licencia

Este proyecto usa la API de TheMovieDB. Asegúrate de cumplir con sus [términos de uso](https://www.themoviedb.org/documentation/api/terms-of-use).

## 🔗 Enlaces útiles

- [Documentación de TheMovieDB API](https://developer.themoviedb.org/docs)
- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [TheMovieDB](https://www.themoviedb.org/)
