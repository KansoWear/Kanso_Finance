import os
from src.logic import generar_reportes

def format_moneda(valor):
    """Formato sofisticado para CLP/USD: $1.234.567"""
    return f"${valor:,.0f}".replace(",", ".")

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_cabecera():
    print("="*50)
    print("       KANSO FINANCE STUDIO | E-COMMERCE ")
    print("        Filosofía: Menos es Más (簡素)")
    print("="*50)

def ejecutar_consola():
    limpiar_pantalla()
    imprimir_cabecera()
    
    path_csv = "data/transacciones.csv"
    
    # Verificación de integridad de archivos
    if not os.path.exists(path_csv):
        print(f"\n[!] ERROR: Archivo '{path_csv}' no detectado.")
        print("    Crea el CSV en la carpeta 'data' para continuar.")
        return

    try:
        # Llamada al motor contable
        data = generar_reportes(path_csv)
        res = data["resultado"]
        bal = data["balance"]

        # 1. ESTADO DE RESULTADOS (P&L)
        print("\n[ I. ESTADO DE RESULTADOS ]")
        print("-" * 30)
        print(f"(+) Ingresos Totales    : {format_moneda(res['Ventas Netas'])}")
        print(f"(-) Costo de Ventas     : {format_moneda(res['Costo de Venta'])}")
        print(f"(-) Gastos Operativos   : {format_moneda(res['Gastos Op'])}")
        print("-" * 30)
        print(f"(=) UTILIDAD NETA       : {format_moneda(res['Utilidad'])}")

        # 2. BALANCE GENERAL
        print("\n[ II. BALANCE GENERAL ]")
        print("-" * 30)
        print(f"ACTIVOS TOTALES         : {format_moneda(bal['Total Activos'])}")
        print(f"PASIVOS TOTALES         : {format_moneda(bal['Total Pasivos'])}")
        print(f"PATRIMONIO TOTAL        : {format_moneda(bal['Patrimonio Total'])}")
        print("-" * 30)
        
        # 3. CONTROL DE INTEGRIDAD
        diff = bal["Equilibrio"]
        if abs(diff) < 0.01:
            print("\nESTADO: [ SISTEMA EN EQUILIBRIO ZEN ]")
        else:
            print(f"\nALERTA: [ DESBALANCE DE {format_moneda(diff)} ]")
            print("REVISIÓN: Verifica las entradas en 'transacciones.csv'.")

    except Exception as e:
        print(f"\n[!] Error técnico en la ejecución: {e}")

    print("\n" + "="*50)

if __name__ == "__main__":
    ejecutar_consola()
