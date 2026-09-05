# 🔍 Process Threat Hunter v1 - Endpoint Monitoring

## 📝 Resumen del Proyecto
Herramienta de detección temprana de amenazas en Endpoints (Windows). Desarrollada en Python, la aplicación escanea la telemetría de procesos en tiempo real utilizando la librería `psutil` para identificar ejecutables sospechosos o posibles malwares (Keyloggers, Spyware) alojados en carpetas temporales del sistema (`AppData\Local\Temp`).

---

## 🛠️ Tecnologías y Entorno
* **Lenguaje:** Python 3.14 (Librerías `psutil` y `os`)
* **Consola:** Windows PowerShell / CMD
* **Habilidades Blue Team:** Endpoint Detection & Response (EDR), Threat Hunting, Identificación de Comportamiento Anómalo, Triaje de Procesos (PID / Execution Path).

---

## 🔍 Metodología y Troubleshooting (Bitácora de Terreno)

1. **Gestión de Entornos e Intérprete:** Resolución de errores de sintaxis en consola al diferenciar entre el intérprete interactivo de Python y la CLI de Windows PowerShell.
2. **Invocación de Módulos:** Corrección en el enrutamiento de variables de entorno invocando el gestor de paquetes directamente con `python -m pip install psutil`.
3. **Aislamiento de Excepciones:** Implementación de manejo de excepciones (`psutil.NoSuchProcess`, `AccessDenied`) para evitar caídas del script ante procesos protegidos del kernel de Windows (`SYSTEM`).

---

## 🚨 Criterios de Detección e Impacto de Negocio
El script evalúa el vector de ataque habitual donde el código malicioso intenta ejecutarse desde zonas con permisos de escritura directa sin elevación previa de privilegios.

**Acción de Respuesta a Incidentes (Playbook SOC):**
1. **Contención:** Aislamiento inmediato del host de la red local/VLAN.
2. **Terminación:** Finalización forzada del proceso por PID (`taskkill /PID <PID> /F`).
3. **Extracción:** Recolección de muestra para análisis estático y consulta de hash en VirusTotal.

---

## 👤 Autor
* **Bastián Gallardo** - *Analista SOC Nivel 1 (Blue Team)*
