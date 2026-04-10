# ─────────────────────────────────────────────
#  CONTROL D'ACCÉS — Mòdul 5
#  Auditoria i Monitoratge de Control d'Accessos
#  Asignatura: Control d'Accés
# ─────────────────────────────────────────────

TEMA = {
    "id":         14,
    "nombre":     "Auditoría y Monitoreo de Control de Accesos",
    "asignatura": "Control d'Accés",
}

TEST = [
    {
        "enunciado": "¿Cuál de los siguientes es un principio fundamental de la auditoría de Control de Accesos?",
        "opciones": [
            ("Maximizar el número de alertas generadas para no perder ningún evento", False),
            ("Evaluar la conformidad de los controles con las políticas internas y las regulaciones externas", True),
            ("Limitar la auditoría a los sistemas con datos financieros únicamente", False),
            ("Realizar auditorías solo cuando se detecte un incidente de seguridad", False),
        ]
    },
    {
        "enunciado": "¿Qué herramienta SIEM está entre las más utilizadas en el sector para recopilación y análisis de eventos de seguridad?",
        "opciones": [
            ("Wireshark y Nagios", False),
            ("Okta y SailPoint", False),
            ("Splunk, IBM QRadar o LogRhythm", True),
            ("Nessus y Metasploit", False),
        ]
    },
    {
        "enunciado": "¿Qué función realiza la normalización de logs en un sistema de gestión centralizado?",
        "opciones": [
            ("Eliminar los logs que no contienen información relevante para reducir el almacenamiento", False),
            ("Convertir los logs de diferentes sistemas y formatos a un formato común que facilite su análisis y correlación", True),
            ("Aumentar la velocidad de generación de logs en los sistemas monitorizados", False),
            ("Cifrar los logs para protegerlos de accesos no autorizados", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el objetivo de la correlación de eventos en un SIEM?",
        "opciones": [
            ("Reducir el número de logs generados por los sistemas", False),
            ("Combinar y analizar datos de diferentes fuentes para identificar patrones de ataque que individualmente parecerían inocentes", True),
            ("Almacenar los logs de forma más eficiente en bases de datos relacionales", False),
            ("Reemplazar la necesidad de auditorías manuales periódicas", False),
        ]
    },
    {
        "enunciado": "En el análisis de logs, el análisis estadístico se usa principalmente para:",
        "opciones": [
            ("Buscar firmas de malware conocidas en los registros de eventos", False),
            ("Comparar logs de diferentes años para detectar tendencias históricas", False),
            ("Identificar desviaciones de los patrones normales de comportamiento y detectar outliers", True),
            ("Generar automáticamente reglas de firewall basadas en el tráfico registrado", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja específica aporta el Machine Learning en el análisis de eventos de seguridad?",
        "opciones": [
            ("Elimina completamente los falsos positivos en los sistemas SIEM", False),
            ("Puede identificar y clasificar patrones complejos y sospechosos sin necesidad de reglas predefinidas", True),
            ("Garantiza el 100% de detección de amenazas desconocidas", False),
            ("Reduce el coste de las licencias de los sistemas SIEM", False),
        ]
    },
    {
        "enunciado": "En la auditoría de servicios en el Cloud, ¿qué implica el 'modelo de responsabilidad compartida'?",
        "opciones": [
            ("El proveedor de Cloud es responsable de toda la seguridad de los datos del cliente", False),
            ("La seguridad es responsabilidad exclusiva del cliente que contrata el servicio", False),
            ("La seguridad se divide entre el proveedor (infraestructura) y el cliente (datos, configuraciones, accesos)", True),
            ("Ambas partes comparten las credenciales de administración del entorno Cloud", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el principal riesgo que aborda la auditoría de configuraciones de seguridad en sistemas operativos?",
        "opciones": [
            ("La posible incompatibilidad entre versiones de software instalado", False),
            ("Que los sistemas tengan configuraciones incorrectas o políticas de contraseñas débiles que faciliten accesos no autorizados", True),
            ("El uso excesivo de recursos de CPU por parte de los procesos del sistema", False),
            ("La obsolescencia del hardware de los servidores auditados", False),
        ]
    },
    {
        "enunciado": "¿Qué normativa exige la implementación de procedimientos para la revisión y monitoreo de logs relacionados con la Información de Salud Protegida (PHI)?",
        "opciones": [
            ("GDPR", False),
            ("PCI DSS", False),
            ("HIPAA", True),
            ("FERPA", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes patrones en los logs es un indicador típico de un ataque de fuerza bruta?",
        "opciones": [
            ("Un único intento de inicio de sesión fallido seguido de uno exitoso", False),
            ("Múltiples intentos fallidos de inicio de sesión desde una misma IP en un corto período de tiempo", True),
            ("Un usuario que inicia sesión siempre desde la misma dirección IP", False),
            ("Accesos a archivos de configuración durante el horario de trabajo habitual", False),
        ]
    },
    {
        "enunciado": "¿Cuánto tiempo deben conservarse los logs según la normativa de una organización?",
        "opciones": [
            ("Siempre 90 días, que es el estándar internacional", False),
            ("Indefinidamente para garantizar la disponibilidad de evidencias", False),
            ("El tiempo que determinen los requisitos legales, normativos y de seguridad específicos de la organización", True),
            ("Solo hasta que el sistema de almacenamiento esté al 80% de capacidad", False),
        ]
    },
    {
        "enunciado": "¿Qué es el análisis de causa raíz (root cause analysis) en el contexto de la gestión de incidentes?",
        "opciones": [
            ("Identificar qué sistema fue el primero en fallar durante un ataque", False),
            ("Analizar los eventos que precedieron al incidente para determinar cómo accedió el atacante y qué técnicas usó", True),
            ("Calcular el coste económico total de un incidente de seguridad", False),
            ("Determinar qué empleado cometió el error que permitió el incidente", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas IAM es un sistema en la nube ampliamente usado para gestión de identidades y accesos?",
        "opciones": [
            ("Splunk Enterprise", False),
            ("Okta o Microsoft Azure Active Directory", True),
            ("Wireshark Professional", False),
            ("IBM QRadar", False),
        ]
    },
    {
        "enunciado": "¿Qué debe incluir un informe de auditoría de Control de Accesos?",
        "opciones": [
            ("Solo las vulnerabilidades encontradas, sin necesidad de evidencias", False),
            ("Metodología usada, deficiencias encontradas con evidencias, evaluación del impacto potencial y recomendaciones priorizadas", True),
            ("Solo las recomendaciones positivas para no generar alarma en la organización", False),
            ("Únicamente los accesos realizados durante el período auditado", False),
        ]
    },
    {
        "enunciado": "¿Qué establece el ISO/IEC 27001 en relación con las auditorías?",
        "opciones": [
            ("Que las auditorías deben realizarse exclusivamente por consultores externos certificados", False),
            ("Que las auditorías internas y externas son herramientas fundamentales para la mejora continua del Sistema de Gestión de Seguridad de la Información (SGSI)", True),
            ("Que solo los sistemas financieros necesitan pasar auditorías bajo este estándar", False),
            ("Que la frecuencia de auditorías mínima es una vez cada cinco años", False),
        ]
    },
    {
        "enunciado": "En la auditoría de aplicaciones, ¿qué aspecto concreto debe verificarse sobre la gestión de sesiones?",
        "opciones": [
            ("Que las sesiones no expiren nunca para mejorar la experiencia del usuario", False),
            ("Que los tokens de sesión y cookies se gestionen de forma que minimicen el riesgo de interceptación y reutilización", True),
            ("Que cada usuario solo pueda tener una sesión activa en toda la organización", False),
            ("Que las sesiones se compartan entre usuarios del mismo departamento", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la ventaja principal de centralizar los logs de múltiples sistemas en un único repositorio?",
        "opciones": [
            ("Reduce el coste de los sistemas de almacenamiento individuales", False),
            ("Facilita el análisis, la correlación entre sistemas y mejora la respuesta a incidentes al tener todo accesible desde un punto", True),
            ("Garantiza que los logs no puedan ser modificados por los administradores del sistema", False),
            ("Elimina la necesidad de implementar alertas automáticas", False),
        ]
    },
    {
        "enunciado": "¿Qué técnica de auditoría permite identificar vulnerabilidades en los controles de acceso simulando un ataque real?",
        "opciones": [
            ("Revisión de políticas y procedimientos", False),
            ("Entrevistas al personal de seguridad", False),
            ("Pruebas de penetración (pentest)", True),
            ("Análisis de la documentación del sistema", False),
        ]
    },
    {
        "enunciado": "¿Por qué es importante integrar las herramientas de monitoreo con los procesos de respuesta a incidentes?",
        "opciones": [
            ("Para reducir el número de logs generados por los sistemas de seguridad", False),
            ("Para permitir una reacción rápida y efectiva cuando el monitoreo detecta una actividad sospechosa o un incidente", True),
            ("Para evitar que el equipo de seguridad tenga que revisar manualmente los logs", False),
            ("Para compartir automáticamente los incidentes detectados con autoridades externas", False),
        ]
    },
    {
        "enunciado": "En el contexto de la auditoría del GDPR, ¿cuál es uno de los requisitos más importantes relacionados con el Control de Accesos?",
        "opciones": [
            ("Publicar un listado de todos los usuarios que acceden a datos personales", False),
            ("Implementar medidas técnicas adecuadas para proteger los datos personales, con auditorías y monitoreo regular de los controles de acceso para prevenir brechas", True),
            ("Permitir a cualquier ciudadano europeo auditar los sistemas de la organización", False),
            ("Almacenar todos los datos personales exclusivamente en servidores europeos", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "El SIEM como núcleo del monitoreo de seguridad",
        "enunciado": (
            "Explica qué es un SIEM, cuáles son sus componentes principales y qué proceso sigue "
            "desde la recolección hasta la generación de alertas (pipeline del SIEM). "
            "¿Cuáles son sus ventajas respecto al monitoreo manual? "
            "Describe tres tipos de ataques o incidentes que un SIEM bien configurado podría detectar "
            "y que serían difíciles de identificar sin él."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Metodología de auditoría de Control de Accesos",
        "enunciado": (
            "Describe el proceso completo de una auditoría de Control de Accesos: "
            "qué principios la guían, qué métodos y técnicas se utilizan y cómo se estructura el informe final. "
            "¿Qué diferencias existen entre auditar entornos Cloud, sistemas operativos y aplicaciones? "
            "¿Qué papel juega el principio de mejora continua tras una auditoría?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Normativas y su impacto en el CA",
        "enunciado": (
            "Selecciona tres normativas de las estudiadas (GDPR, PCI DSS, HIPAA, ISO 27001, CCPA u otras) "
            "y describe qué requisitos específicos imponen sobre el Control de Accesos y la auditoría. "
            "¿Qué tienen en común estas normativas? ¿Cuáles son las consecuencias para una organización "
            "que no cumple con ellas?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Gestión de incidentes con datos de auditoría",
        "enunciado": (
            "Describe cómo los datos de auditoría y los logs pueden usarse para detectar, investigar "
            "y responder a un incidente de seguridad de Control de Accesos. "
            "Explica el proceso de análisis de causa raíz. "
            "¿Cómo se usa esa información para mejorar los controles y prevenir incidentes futuros? "
            "Pon un ejemplo concreto de un incidente y cómo se identificaría con los logs."
        ),
        "puntos": 15,
    },
]
