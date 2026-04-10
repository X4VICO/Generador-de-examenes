# ─────────────────────────────────────────────
#  CONTROL D'ACCÉS — Mòdul 1
#  Introducció al Control d'Accessos
#  Asignatura: Control d'Accés
# ─────────────────────────────────────────────

TEMA = {
    "id":         10,
    "nombre":     "Introducción al Control de Accesos",
    "asignatura": "Control d'Accés",
}

TEST = [
    {
        "enunciado": "¿Cuál es el objetivo principal del Control de Accesos en ciberseguridad?",
        "opciones": [
            ("Maximizar el rendimiento de los sistemas informáticos", False),
            ("Proteger la confidencialidad, integridad y disponibilidad de los recursos", True),
            ("Reducir los costes de infraestructura tecnológica", False),
            ("Gestionar el inventario de hardware y software de la organización", False),
        ]
    },
    {
        "enunciado": "¿Qué representa la triada CIA en el contexto del Control de Accesos?",
        "opciones": [
            ("Confidencialidad, Identificación y Autenticación", False),
            ("Control, Integridad y Autorización", False),
            ("Confidencialidad, Integridad y Disponibilidad", True),
            ("Cifrado, Integridad y Acceso", False),
        ]
    },
    {
        "enunciado": "¿En qué orden correcto se produce el proceso AAA?",
        "opciones": [
            ("Autorización → Autenticación → Autenticación", False),
            ("Identificación → Autenticación → Autorización → Accountability", True),
            ("Autenticación → Identificación → Autorización → Auditoría", False),
            ("Autorización → Identificación → Autenticación → Accountability", False),
        ]
    },
    {
        "enunciado": "En el proceso AAA, ¿qué fase consiste en declarar quién eres ante el sistema sin que se verifique todavía?",
        "opciones": [
            ("Autenticación", False),
            ("Autorización", False),
            ("Identificación", True),
            ("Accountability", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de control técnico (lógico)?",
        "opciones": [
            ("Guardia de seguridad en la entrada del edificio", False),
            ("Política de contraseñas fuertes establecida por RRHH", False),
            ("Firewall que filtra el tráfico de red", True),
            ("Cámara de vigilancia en el centro de datos", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes es un ejemplo de control administrativo?",
        "opciones": [
            ("Sistema de cifrado de disco completo", False),
            ("Política de seguridad y programa de formación de empleados", True),
            ("Cerradura biométrica en la sala de servidores", False),
            ("Sistema de detección de intrusos (IDS)", False),
        ]
    },
    {
        "enunciado": "Un control que tiene como objetivo evitar que ocurra un incidente de seguridad se denomina:",
        "opciones": [
            ("Control detectivo", False),
            ("Control correctivo", False),
            ("Control preventivo", True),
            ("Control compensatorio", False),
        ]
    },
    {
        "enunciado": "¿Qué tipo de control son los planes de respuesta a incidentes y las copias de seguridad?",
        "opciones": [
            ("Controles preventivos", False),
            ("Controles detectivos", False),
            ("Controles correctivos", True),
            ("Controles físicos", False),
        ]
    },
    {
        "enunciado": "¿Qué fase del proceso AAA rastrea y registra todas las acciones realizadas por un usuario?",
        "opciones": [
            ("Identificación", False),
            ("Autenticación", False),
            ("Autorización", False),
            ("Accountability (Rendición de cuentas)", True),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes NO es un componente de infraestructura del Control de Accesos?",
        "opciones": [
            ("Servidor LDAP para autenticación", False),
            ("Sistema IAM para gestión de identidades", False),
            ("Switch de capa 2 para conectividad básica de red", True),
            ("Tokens de seguridad para segundo factor", False),
        ]
    },
    {
        "enunciado": "¿Qué estrategia de seguridad asume que ningún usuario o dispositivo es de confianza por defecto, incluso dentro de la red corporativa?",
        "opciones": [
            ("Defensa en Profundidad", False),
            ("Zero Trust", True),
            ("Seguridad Perimetral", False),
            ("Principio de Mínimo Privilegio", False),
        ]
    },
    {
        "enunciado": "¿Cuál es uno de los principales desafíos del Control de Accesos en entornos IoT?",
        "opciones": [
            ("Exceso de ancho de banda disponible en los dispositivos", False),
            ("Los dispositivos IoT tienen capacidades computacionales limitadas que dificultan el cifrado y la autenticación tradicional", True),
            ("Los dispositivos IoT no se conectan a redes corporativas", False),
            ("La excesiva centralización de la gestión de identidades", False),
        ]
    },
    {
        "enunciado": "¿Qué protocolo se usa habitualmente como servidor de autenticación centralizado en redes corporativas?",
        "opciones": [
            ("HTTP y HTTPS", False),
            ("LDAP o RADIUS", True),
            ("DNS y DHCP", False),
            ("FTP y SFTP", False),
        ]
    },
    {
        "enunciado": "La política BYOD (Bring Your Own Device) en el Control de Accesos plantea principalmente el reto de:",
        "opciones": [
            ("Reducir los costes de licencias de software corporativo", False),
            ("Equilibrar la flexibilidad de los empleados con la seguridad en el acceso a datos corporativos", True),
            ("Gestionar el inventario de dispositivos personales de los empleados", False),
            ("Garantizar la velocidad de conexión de los dispositivos personales", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre la evolución del Control de Accesos es correcta?",
        "opciones": [
            ("Los primeros sistemas de CA ya usaban autenticación biométrica avanzada", False),
            ("Internet no tuvo impacto en la complejidad de los controles de acceso", False),
            ("La evolución fue de sistemas rudimentarios (ACLs, contraseñas simples) hacia sistemas con MFA, biometría y enfoques basados en identidad", True),
            ("Los sistemas modernos de CA han eliminado completamente la necesidad de controles físicos", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la función principal de un sistema IAM (Identity and Access Management)?",
        "opciones": [
            ("Monitorizar el rendimiento de la red corporativa", False),
            ("Administrar identidades de usuario: creación, modificación, desactivación de cuentas y gestión de roles y permisos", True),
            ("Cifrar las comunicaciones entre sistemas internos y externos", False),
            ("Gestionar las copias de seguridad de los datos corporativos", False),
        ]
    },
    {
        "enunciado": "¿Qué necesidad fundamental del CA se encarga de verificar que solo las personas autorizadas puedan modificar la información?",
        "opciones": [
            ("Prevención de accesos no autorizados", False),
            ("Control de privilegios y autorizaciones", False),
            ("Mantenimiento de la integridad de los datos", True),
            ("Gestión de identidades y autenticación", False),
        ]
    },
    {
        "enunciado": "La 'Defensa en Profundidad' como estrategia de seguridad implica:",
        "opciones": [
            ("Concentrar todos los recursos de seguridad en el perímetro de la red", False),
            ("Implementar una única capa de seguridad muy robusta", False),
            ("Implementar múltiples capas de seguridad independientes para que si una falla, las demás compensen", True),
            ("Defender únicamente los sistemas más críticos de la organización", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el principal riesgo de los errores de configuración en el Control de Accesos?",
        "opciones": [
            ("Degradación del rendimiento de los servidores de autenticación", False),
            ("Pueden exponer datos mediante permisos excesivamente permisivos o reglas mal configuradas", True),
            ("Aumentan el tiempo de respuesta en la autenticación de usuarios", False),
            ("Generan conflictos entre los sistemas IAM y los servidores LDAP", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes representa un desafío específico del Control de Accesos relacionado con la Inteligencia Artificial?",
        "opciones": [
            ("La IA elimina completamente la necesidad de autenticación humana", False),
            ("La IA no puede integrarse con sistemas IAM existentes", False),
            ("La IA procesa grandes volúmenes de datos sensibles y puede ser manipulada o comprometida si no tiene un CA robusto", True),
            ("La IA solo puede usarse para controles físicos, no lógicos", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "El proceso AAA y la triada CIA",
        "enunciado": (
            "Explica el proceso AAA (Identificación, Autenticación, Autorización y Accountability) "
            "describiendo qué ocurre en cada fase y qué información se maneja. "
            "Relaciona cada fase con la protección de los principios de la triada CIA "
            "(Confidencialidad, Integridad y Disponibilidad)."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Tipos de controles de acceso",
        "enunciado": (
            "Clasifica y describe los tipos de controles de acceso según su naturaleza "
            "(físicos, técnicos y administrativos) y según su función (preventivos, detectivos y correctivos). "
            "Para cada tipo proporciona al menos dos ejemplos concretos y explica "
            "por qué ninguna categoría es suficiente por sí sola."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Desafíos del CA en entornos modernos",
        "enunciado": (
            "Describe los principales desafíos que plantea el Control de Accesos en tres entornos modernos: "
            "Cloud/Mobile, IoT y entornos con Inteligencia Artificial. "
            "Para cada entorno indica al menos dos retos específicos y una medida para afrontarlos. "
            "¿Qué tienen en común estos desafíos?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Zero Trust vs. Seguridad Perimetral",
        "enunciado": (
            "Explica en qué consiste el modelo Zero Trust y en qué se diferencia fundamentalmente "
            "del modelo tradicional de seguridad perimetral. "
            "¿Por qué la adopción del Cloud y el trabajo remoto han acelerado la adopción de Zero Trust? "
            "Indica dos ventajas y dos dificultades de implementar Zero Trust en una organización mediana."
        ),
        "puntos": 15,
    },
]
