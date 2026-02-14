from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from typing import List, Optional
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

app = FastAPI(
    title="TheMovieDB Search API",
    description="API para buscar películas usando TheMovieDB",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obtener API key de TheMovieDB
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = "https://api.themoviedb.org/3"

# Modelos de datos
class Movie(BaseModel):
    id: int
    title: str
    original_title: str
    overview: Optional[str] = None
    release_date: Optional[str] = None
    poster_path: Optional[str] = None
    backdrop_path: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    popularity: Optional[float] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 550,
                "title": "Fight Club",
                "original_title": "Fight Club",
                "overview": "A ticking-time-bomb insomniac...",
                "release_date": "1999-10-15",
                "poster_path": "/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
                "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
                "vote_average": 8.433,
                "vote_count": 26280,
                "popularity": 61.416
            }
        }

class SearchResponse(BaseModel):
    page: int
    total_results: int
    total_pages: int
    results: List[Movie]

@app.get("/")
async def root():
    """
    Endpoint raíz - Información de la API
    """
    return {
        "message": "TheMovieDB Search API",
        "version": "1.0.0",
        "endpoints": {
            "search": "/search/movie?query=nombre_pelicula",
            "docs": "/docs"
        }
    }

@app.get("/search/movie", response_model=SearchResponse)
async def search_movie(
    query: str = Query(..., description="Título de la película a buscar", min_length=1),
    page: int = Query(1, description="Número de página", ge=1),
    language: str = Query("es-MX", description="Idioma de los resultados"),
    include_adult: bool = Query(False, description="Incluir contenido para adultos")
):
    
    # Verificar que la API key esté configurada
    if not TMDB_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="TMDB_API_KEY no está configurada. Por favor configura tu API key en el archivo .env"
        )
    
    # Preparar parámetros de la solicitud
    params = {
        "query": query,
        "page": page,
        "language": language,
        "include_adult": include_adult
    }
    
    # Headers con autenticación
    headers = {
        "Authorization": f"Bearer {TMDB_API_KEY}",
        "accept": "application/json"
    }
    
    try:
        # Hacer la solicitud a TheMovieDB
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{TMDB_BASE_URL}/search/movie",
                params=params,
                headers=headers,
                timeout=10.0
            )
            response.raise_for_status()
            data = response.json()
        
        # Formatear la respuesta
        return SearchResponse(
            page=data.get("page", 1),
            total_results=data.get("total_results", 0),
            total_pages=data.get("total_pages", 0),
            results=[
                Movie(
                    id=movie["id"],
                    title=movie.get("title", ""),
                    original_title=movie.get("original_title", ""),
                    overview=movie.get("overview"),
                    release_date=movie.get("release_date"),
                    poster_path=movie.get("poster_path"),
                    backdrop_path=movie.get("backdrop_path"),
                    vote_average=movie.get("vote_average"),
                    vote_count=movie.get("vote_count"),
                    popularity=movie.get("popularity")
                )
                for movie in data.get("results", [])
            ]
        )
    
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error al consultar TheMovieDB: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Error de conexión con TheMovieDB: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """
    Verificar el estado de la API
    """
    has_api_key = bool(TMDB_API_KEY)
    return {
        "status": "healthy" if has_api_key else "warning",
        "api_key_configured": has_api_key,
        "message": "API funcionando correctamente" if has_api_key else "API key no configurada"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
