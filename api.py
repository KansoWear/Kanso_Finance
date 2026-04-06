from fastapi import FastAPI, HTTPException
from src.logic import generar_reportes
import os

app = FastAPI(title="KANSO Finance API", description="Dashboard Contable de Alto Gramaje")

PATH_CSV = "data/transacciones.csv"

@app.get("/")
def read_root():
    return {"status": "Online", "brand": "KANSO (簡素)", "mode": "Premium"}

@app.get("/finanzas")
def obtener_finanzas():
    if not os.path.exists(PATH_CSV):
        raise HTTPException(status_code=404, detail="Archivo de transacciones no encontrado.")
    
    try:
        reportes = generar_reportes(PATH_CSV)
        return reportes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/salud")
def verificar_equilibrio():
    reportes = generar_reportes(PATH_CSV)
    equilibrio = reportes["balance"]["Equilibrio"]
    
    if abs(equilibrio) < 0.01:
        return {"estado": "Equilibrio Zen", "diferencia": 0}
    else:
        return {"estado": "Desbalance Detectado", "diferencia": equilibrio}