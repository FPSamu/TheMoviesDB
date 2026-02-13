# Ejemplos de Respuestas de la API

## 1. Endpoint Raíz (/)

**Request:**
```bash
GET http://localhost:8000/
```

**Response:**
```json
{
  "message": "TheMovieDB Search API",
  "version": "1.0.0",
  "endpoints": {
    "search": "/search/movie?query=nombre_pelicula",
    "docs": "/docs"
  }
}
```

---

## 2. Health Check (/health)

**Request:**
```bash
GET http://localhost:8000/health
```

**Response (API Key configurada):**
```json
{
  "status": "healthy",
  "api_key_configured": true,
  "message": "API funcionando correctamente"
}
```

**Response (API Key NO configurada):**
```json
{
  "status": "warning",
  "api_key_configured": false,
  "message": "API key no configurada"
}
```

---

## 3. Búsqueda de Películas (/search/movie)

### Ejemplo 1: Búsqueda simple

**Request:**
```bash
GET http://localhost:8000/search/movie?query=Matrix
```

**Response:**
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
      "overview": "Thomas Anderson lleva una doble vida: por el día es programador informático y hacker informático por la noche. Un día es contactado por Morfeo, un legendario hacker...",
      "release_date": "1999-03-30",
      "poster_path": "/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg",
      "backdrop_path": "/fNG7i7RqMErkcqhohV2a6cV1Ehy.jpg",
      "vote_average": 8.2,
      "vote_count": 23542,
      "popularity": 85.456
    },
    {
      "id": 604,
      "title": "The Matrix Reloaded",
      "original_title": "The Matrix Reloaded",
      "overview": "Las máquinas avanzan imparables hacia Zion en su afán por destruir a toda la humanidad...",
      "release_date": "2003-05-15",
      "poster_path": "/9TGHDvWrqKBzwDxDodHYXEmOE6J.jpg",
      "backdrop_path": "/1Xx8LkKPOhg5CYZwmfPMTdVG8Gp.jpg",
      "vote_average": 7.1,
      "vote_count": 11234,
      "popularity": 65.234
    }
  ]
}
```

### Ejemplo 2: Búsqueda con paginación

**Request:**
```bash
GET http://localhost:8000/search/movie?query=Avengers&page=2&language=es-MX
```

**Response:**
```json
{
  "page": 2,
  "total_results": 156,
  "total_pages": 8,
  "results": [
    {
      "id": 271110,
      "title": "Capitán América y el Soldado del Invierno",
      "original_title": "Captain America: The Winter Soldier",
      "overview": "Después de los acontecimientos catastróficos acontecidos en Nueva York con Los Vengadores...",
      "release_date": "2014-03-26",
      "poster_path": "/5TQ6YDmymBpnF005OyoB7ohZps9.jpg",
      "backdrop_path": "/4qfXT9BtxeFuamR4F49m2mpKQI1.jpg",
      "vote_average": 7.7,
      "vote_count": 15678,
      "popularity": 72.123
    }
  ]
}
```

### Ejemplo 3: Búsqueda en inglés

**Request:**
```bash
GET http://localhost:8000/search/movie?query=Inception&language=en-US
```

**Response:**
```json
{
  "page": 1,
  "total_results": 12,
  "total_pages": 1,
  "results": [
    {
      "id": 27205,
      "title": "Inception",
      "original_title": "Inception",
      "overview": "Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets...",
      "release_date": "2010-07-16",
      "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
      "backdrop_path": "/s3TBrRGB1iav7gFOCNx3H31MoES.jpg",
      "vote_average": 8.4,
      "vote_count": 32456,
      "popularity": 95.678
    }
  ]
}
```

### Ejemplo 4: Sin resultados

**Request:**
```bash
GET http://localhost:8000/search/movie?query=xyzabc123notexist
```

**Response:**
```json
{
  "page": 1,
  "total_results": 0,
  "total_pages": 0,
  "results": []
}
```

---

## 4. Errores

### Error: API Key no configurada

**Request:**
```bash
GET http://localhost:8000/search/movie?query=Matrix
```

**Response (500):**
```json
{
  "detail": "TMDB_API_KEY no está configurada. Por favor configura tu API key en el archivo .env"
}
```

### Error: Parámetro query vacío

**Request:**
```bash
GET http://localhost:8000/search/movie?query=
```

**Response (422):**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["query", "query"],
      "msg": "String should have at least 1 character",
      "input": "",
      "ctx": {
        "min_length": 1
      }
    }
  ]
}
```

### Error: Página inválida

**Request:**
```bash
GET http://localhost:8000/search/movie?query=Matrix&page=0
```

**Response (422):**
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": ["query", "page"],
      "msg": "Input should be greater than or equal to 1",
      "input": "0",
      "ctx": {
        "ge": 1
      }
    }
  ]
}
```

---

## URLs de Imágenes

Los campos `poster_path` y `backdrop_path` retornan rutas relativas. Para obtener la URL completa:

### Posters
```
https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg
```

Tamaños disponibles: `w92`, `w154`, `w185`, `w342`, `w500`, `w780`, `original`

### Backdrops
```
https://image.tmdb.org/t/p/w1280/fNG7i7RqMErkcqhohV2a6cV1Ehy.jpg
```

Tamaños disponibles: `w300`, `w780`, `w1280`, `original`

---

## Idiomas Soportados

- `es-MX` - Español (México) - **Default**
- `es-ES` - Español (España)
- `en-US` - Inglés (Estados Unidos)
- `fr-FR` - Francés
- `de-DE` - Alemán
- `it-IT` - Italiano
- `pt-BR` - Portugués (Brasil)
- `ja-JP` - Japonés
- `ko-KR` - Coreano
- `zh-CN` - Chino Simplificado

[Lista completa de idiomas soportados](https://developer.themoviedb.org/docs/languages)
