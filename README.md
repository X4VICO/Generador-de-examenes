# 🎓 Generador de Exámenes en Python

> Un simulador interactivo por consola para practicar antes de los exámenes parciales y finales. 

Este proyecto es un entorno de autoevaluación dinámico escrito en Python. El programa actúa como un "Runner" que busca, valida y carga automáticamente archivos de preguntas (bancos de test y redacción) para generar simulacros de examen a medida.

---

## 🚀 Características Principales

*   **Carga Dinámica de Temas:** El programa lee automáticamente cualquier archivo `.py` válido que se encuentre dentro de la carpeta `temas/`.
*   **Generación de Exámenes a Medida:** Permite al usuario seleccionar qué temas quiere repasar y cuántas preguntas de cada tipo desea afrontar.
*   **Tipos de Preguntas Soportadas:**
    *   **Tipo Test:** Opciones mezcladas aleatoriamente (A, B, C, D) con validación automática y feedback en tiempo real.
    *   **Redacción (Desarrollo):** Permite respuestas multilínea por consola y genera un bloque de texto estructurado para su posterior corrección manual.
*   **Cálculo de Notas:** Genera una nota parcial instantánea basada en el test y prepara la estructura para sumar la nota de las preguntas de redacción.
*   **Interfaz CLI Amigable:** Uso de colores ANSI para una lectura cómoda, menús interactivos y envoltura de texto (*text wrapping*) para evitar líneas infinitas.

---

## 📁 Estructura del Proyecto

El flujo de trabajo está diseñado para mantener un repositorio ordenado de todas las asignaturas:

```text
📦 Generador-de-examenes
 ┣ 📜 examen.py        # Script principal que ejecuta el simulacro
 ┣ 📜 README.md        # Documentación del proyecto
 ┣ 📂 biblioteca       # Almacén de TODOS los archivos de preguntas creados
 ┗ 📂 temas            # Carpeta activa: el script SOLO lee los archivos aquí
```

**💡 ¿Cómo funciona el sistema de carpetas?**
Para evitar que el programa cargue todas las asignaturas a la vez, guarda todos tus archivos de preguntas en la carpeta `biblioteca`. Cuando vayas a estudiar, simplemente **copia o mueve** los archivos específicos que quieras repasar (ej: `redes3_tema1.py` o `controlacces_m1.py`) a la carpeta `temas`.

---

## 🛠️ Instalación y Uso

1. **Clona el repositorio** en tu máquina local:
   ```bash
   git clone https://github.com/X4VICO/Generador-de-examenes.git
   cd Generador-de-examenes
   ```

2. **Prepara tu examen:**
   Mueve los archivos de los módulos que quieras repasar desde la carpeta `biblioteca/` hacia la carpeta `temas/`.

3. **Ejecuta el simulador:**
   No requiere dependencias externas, utiliza únicamente la biblioteca estándar de Python (requiere Python 3.x).
   ```bash
   python examen.py
   ```
   *(Sigue las instrucciones en pantalla para elegir los temas y el número de preguntas).*

---

## 📝 Cómo añadir nuevas preguntas

Para añadir una nueva asignatura o módulo, crea un archivo `.py` (por ejemplo: `asignatura_modulo.py`) y asegúrate de definir en él las siguientes tres variables obligatorias: `TEMA`, `TEST` y `REDACCION`.

Aquí tienes la plantilla base:

```python
# Variables obligatorias para que el runner detecte el archivo

TEMA = {
    "id": 1,                     # Número identificador único para ordenar
    "nombre": "Nombre del Tema", # Nombre que aparecerá en el menú
    "asignatura": "Asignatura",  # Agrupación 
}

TEST = [
    {
        "enunciado": "Texto de la pregunta de opción múltiple",
        "opciones": [
            ("Opción A incorrecta", False),
            ("Opción B correcta", True),   # Solo UNA opción debe ser True
            ("Opción C incorrecta", False),
            ("Opción D incorrecta", False),
        ]
    },
    # Añadir más diccionarios para más preguntas...
]

REDACCION = [
    {
        "titulo": "Título corto de la pregunta",
        "enunciado": "Enunciado completo explicando qué debe desarrollar el alumno.",
        "puntos": 15, # Puntuación máxima de esta pregunta
    },
    # Añadir más diccionarios para más preguntas...
]
```

**Notas importantes sobre el formato:**
* El runner validará automáticamente al arrancar que cada pregunta de tipo test tenga **exactamente una respuesta correcta** (`True`). Si hay errores, te lo notificará en la consola y omitirá ese archivo para evitar fallos durante el examen.
