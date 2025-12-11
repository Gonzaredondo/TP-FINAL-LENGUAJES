from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
import json
import os

# ───────────────── CONFIGURACIÓN BÁSICA ───────────────── #

app = FastAPI(
    title="Mini API TMDB - Lenguajes 2025",
    description="Exposición de resultados del análisis TMDB 5000 Movies",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SALIDA_DIR = os.path.join(BASE_DIR, "salida")


def cargar_json(nombre_archivo: str):
    """Lee un archivo JSON desde la carpeta 'salida'."""
    ruta = os.path.join(SALIDA_DIR, nombre_archivo)
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

# ───────────────── PÁGINA DE INICIO (MENÚ) ───────────────── #


@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>Mini API TMDB - Lenguajes 2025</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: #e5e7eb;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    background-color: #020617;
                    padding: 30px 40px;
                    border-radius: 12px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
                    max-width: 600px;
                }
                h1 {
                    margin-bottom: 10px;
                }
                h2 {
                    margin-top: 0;
                    font-weight: normal;
                    color: #9ca3af;
                    font-size: 16px;
                }
                .btn {
                    display: block;
                    margin: 10px auto;
                    padding: 12px 16px;
                    width: 100%;
                    max-width: 340px;
                    border-radius: 8px;
                    text-decoration: none;
                    color: #f9fafb;
                    background-color: #2563eb;
                    transition: background-color 0.2s, transform 0.1s;
                    font-weight: 600;
                }
                .btn.secondary {
                    background-color: #16a34a;
                }
                .btn.docs {
                    background-color: #f97316;
                }
                .btn:hover {
                    background-color: #1d4ed8;
                    transform: translateY(-1px);
                }
                .btn.secondary:hover {
                    background-color: #15803d;
                }
                .btn.docs:hover {
                    background-color: #ea580c;
                }
                .footer {
                    margin-top: 15px;
                    font-size: 12px;
                    color: #6b7280;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Mini API TMDB</h1>
                <h2>Trabajo Final Lenguajes 2025</h2>

                <a href="/top_generos_html" class="btn">
                    📊 Ver tabla: Top géneros por ROI promedio
                </a>
                <a href="/roi_por_idioma_html" class="btn">
                    🌎 Ver tabla: ROI promedio por idioma original
                </a>

                <a href="/top_generos" class="btn secondary">
                    🔧 Endpoint JSON: /top_generos
                </a>
                <a href="/roi_por_idioma" class="btn secondary">
                    🔧 Endpoint JSON: /roi_por_idioma
                </a>

                <a href="/docs" class="btn docs">
                    📚 Documentación interactiva (Swagger)
                </a>

                <div class="footer">
                    Dataset: TMDB 5000 Movies — Análisis y exposición de resultados.
                </div>
            </div>
        </body>
    </html>
    """
    return html

# ───────────────── ENDPOINTS JSON OFICIALES ───────────────── #


@app.get("/top_generos")
def get_top_generos():
    data = cargar_json("top_generos.json")
    return JSONResponse(content=data)


@app.get("/roi_por_idioma")
def get_roi_por_idioma():
    data = cargar_json("roi_por_idioma.json")
    return JSONResponse(content=data)

# ───────────────── VISTAS HTML ───────────────── #


@app.get("/top_generos_html", response_class=HTMLResponse)
def top_generos_html():
    data = cargar_json("top_generos.json")

    filas = ""
    for fila in data:
        filas += f"""
        <tr>
            <td>{fila['genero']}</td>
            <td>{fila['roi_promedio']:.2f}</td>
        </tr>
        """

    html = f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>Top géneros por ROI promedio</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #111827;
                    color: #e5e7eb;
                    padding: 20px;
                }}
                h1 {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                table {{
                    width: 60%;
                    margin: 0 auto;
                    border-collapse: collapse;
                    background-color: #1f2937;
                    border-radius: 8px;
                    overflow: hidden;
                }}
                th, td {{
                    padding: 10px 14px;
                    text-align: left;
                }}
                th {{
                    background-color: #111827;
                }}
                tr:nth-child(even) {{
                    background-color: #111827;
                }}
                tr:hover {{
                    background-color: #374151;
                }}
            </style>
        </head>
        <body>
            <h1>Top géneros por ROI promedio</h1>
            <table>
                <thead>
                    <tr>
                        <th>Género</th>
                        <th>ROI promedio</th>
                    </tr>
                </thead>
                <tbody>
                    {filas}
                </tbody>
            </table>
        </body>
    </html>
    """
    return html


@app.get("/roi_por_idioma_html", response_class=HTMLResponse)
def roi_por_idioma_html():
    data = cargar_json("roi_por_idioma.json")

    filas = ""
    for fila in data:
        filas += f"""
        <tr>
            <td>{fila['idioma_original']}</td>
            <td>{fila['roi_promedio']:.2f}</td>
        </tr>
        """

    html = f"""
    <html>
        <head>
            <meta charset="utf-8">
            <title>ROI promedio por idioma original</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #111827;
                    color: #e5e7eb;
                    padding: 20px;
                }}
                h1 {{
                    text-align: center;
                    margin-bottom: 20px;
                }}
                table {{
                    width: 60%;
                    margin: 0 auto;
                    border-collapse: collapse;
                    background-color: #1f2937;
                    border-radius: 8px;
                    overflow: hidden;
                }}
                th, td {{
                    padding: 10px 14px;
                    text-align: left;
                }}
                th {{
                    background-color: #111827;
                }}
                tr:nth-child(even) {{
                    background-color: #111827;
                }}
                tr:hover {{
                    background-color: #374151;
                }}
            </style>
        </head>
        <body>
            <h1>ROI promedio por idioma original</h1>
            <table>
                <thead>
                    <tr>
                        <th>Idioma</th>
                        <th>ROI promedio</th>
                    </tr>
                </thead>
                <tbody>
                    {filas}
                </tbody>
            </table>
        </body>
    </html>
    """
    return html
