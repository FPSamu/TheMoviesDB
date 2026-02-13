# 🚀 Inicio Rápido - TheMovieDB Search API

## Pasos para empezar:

### 1️⃣ Obtén tu API Key de TheMovieDB

1. Ve a https://www.themoviedb.org/
2. Crea una cuenta o inicia sesión
3. Ve a Settings → API (https://www.themoviedb.org/settings/api)
4. Solicita una API key (tipo "Developer")
5. Copia el **"API Read Access Token"** (el token Bearer, NO el API Key v3)

### 2️⃣ Configura tu API Key

Edita el archivo `.env` y pega tu API key:

```bash
TMDB_API_KEY=eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI...tu_token_aqui
```

### 3️⃣ Inicia la API

```bash
python3 main.py
```

O con uvicorn:

```bash
python3 -m uvicorn main:app --reload
```

La API estará disponible en: http://localhost:8000

### 4️⃣ Prueba la API

Tienes varias opciones:

#### Opción A: Interfaz Web (Más fácil)
Abre en tu navegador: `index.html`

#### Opción B: Documentación Interactiva (Swagger)
Visita: http://localhost:8000/docs

#### Opción C: Script de Python
```bash
python3 test_api.py
```

#### Opción D: Curl (Terminal)
```bash
curl "http://localhost:8000/search/movie?query=Matrix"
```

---

## 📌 Endpoints Principales

### 🔍 Buscar películas
```
GET /search/movie?query={titulo}
```

**Parámetros:**
- `query` (requerido) - Título de la película
- `page` (opcional) - Número de página (default: 1)
- `language` (opcional) - Idioma (default: "es-MX")
- `include_adult` (opcional) - Contenido adulto (default: false)

**Ejemplo:**
```bash
curl "http://localhost:8000/search/movie?query=Avengers&language=es-MX"
```

### ❤️ Health Check
```
GET /health
```

Verifica que la API esté funcionando y que la API key esté configurada.

---

## ⚠️ Solución de Problemas

### "TMDB_API_KEY no está configurada"
- Asegúrate de haber editado el archivo `.env`
- Verifica que el token sea el **"API Read Access Token"** (Bearer), NO el API Key v3

### "No se puede conectar a la API"
- Verifica que la API esté corriendo: `python3 main.py`
- Asegúrate de estar usando el puerto correcto (8000)

### "Error al consultar TheMovieDB"
- Verifica que tu API key sea válida
- Asegúrate de tener conexión a internet

---

## 📚 Más Información

Lee el archivo `README.md` para documentación completa.
