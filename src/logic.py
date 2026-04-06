import pandas as pd

def generar_reportes(path_csv):
    """
    Procesa el archivo de transacciones para generar 
    el Estado de Resultados y el Balance General integrados.
    """
    # Carga de datos con limpieza de espacios
    df = pd.read_csv(path_csv)
    df['tipo'] = df['tipo'].str.strip()
    df['categoria'] = df['categoria'].str.strip()

    # --- 1. LÓGICA DE ESTADO DE RESULTADOS (P&L) ---
    # Filtramos por categorías de rendimiento
    ingresos = df[df['categoria'] == 'Ingreso']['monto'].sum()
    costos = df[df['categoria'] == 'Costo']['monto'].sum()
    gastos = df[df['categoria'] == 'Gasto']['monto'].sum()
    
    utilidad_neta = ingresos - costos - gastos

    # --- 2. LÓGICA DE BALANCE GENERAL ---
    # Activos y Pasivos son acumulativos
    activos = df[df['tipo'] == 'Activo']['monto'].sum()
    pasivos = df[df['tipo'] == 'Pasivo']['monto'].sum()
    
    # El Patrimonio se compone del capital inicial (en el CSV) 
    # más la utilidad neta del ejercicio actual.
    patrimonio_base = df[df['tipo'] == 'Patrimonio']['monto'].sum()
    patrimonio_total = patrimonio_base + utilidad_neta

    # --- 3. RETORNO DE DATOS ESTRUCTURADOS ---
    return {
        "resultado": {
            "Ventas Netas": ingresos,
            "Costo de Venta": costos,
            "Gastos Op": gastos,
            "Utilidad": utilidad_neta
        },
        "balance": {
            "Total Activos": activos,
            "Total Pasivos": pasivos,
            "Patrimonio Total": patrimonio_total,
            "Equilibrio": activos - (pasivos + patrimonio_total)
        }
    }