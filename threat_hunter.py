import psutil
import os

# --- DETECTOR DE PROCESOS SOSPECHOSOS EN ENDPOINT v1 ---
# Autor: Bastián Gallardo - Analista SOC Nivel 1 (Blue Team)

print("[+] Iniciando escaneo de procesos en tiempo real...")
print("-" * 60)

procesos_sospechosos = 0

# Rutas donde habitualmente se esconde el malware/keyloggers en Windows
carpetas_criticas = ["temp", "appdata\\local\\temp"]

for proceso in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent']):
    try:
        nombre = proceso.info['name']
        pid = proceso.info['pid']
        ruta = proceso.info['exe']
        cpu = proceso.info['cpu_percent']

        if ruta:
            ruta_lower = ruta.lower()
            
            # Criterio de Deteccion: Proceso corriendo desde carpetas temporales
            for carpeta in carpetas_criticas:
                if carpeta in ruta_lower:
                    procesos_sospechosos += 1
                    print(f"🚨 [ALERTA DE SEGURIDAD] Proceso ejecutado desde ubicación temporal!")
                    print(f"   👉 Nombre del Proceso: {nombre} | PID: {pid}")
                    print(f"   👉 Ruta de Ejecucion: {ruta}")
                    print("-" * 60)

    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        # Ignoramos procesos del sistema que requieren privilegios de SYSTEM
        pass

if procesos_sospechosos == 0:
    print("✅ [OK] No se detectaron procesos anómalos corriendo en carpetas temporales.")

print("-" * 60)
print("[+] Escaneo de telemetria finalizado con exito.")