# ─────────────────────────────────────────────
#  CONTROL D'ACCÉS — Mòdul 4
#  Gestió de Privilegis i Administració de Comptes
#  Asignatura: Control d'Accés
# ─────────────────────────────────────────────

TEMA = {
    "id":         13,
    "nombre":     "Gestión de Privilegios y Administración de Cuentas",
    "asignatura": "Control d'Accés",
}

TEST = [
    {
        "enunciado": "¿Cuál es el objetivo principal del movimiento lateral en un ataque?",
        "opciones": [
            ("Obtener privilegios de administrador inmediatamente tras el acceso inicial", False),
            ("Moverse entre sistemas del mismo nivel de seguridad para buscar datos sensibles, sistemas de mayor valor o cuentas con más privilegios", True),
            ("Borrar todos los logs del sistema comprometido", False),
            ("Instalar ransomware en el sistema inicial para luego extenderlo", False),
        ]
    },
    {
        "enunciado": "¿En qué se diferencia el movimiento vertical (escalado de privilegios) del movimiento lateral?",
        "opciones": [
            ("El movimiento vertical se mueve entre sistemas del mismo nivel; el lateral obtiene privilegios más altos", False),
            ("El movimiento lateral se mueve entre sistemas del mismo nivel; el vertical obtiene niveles de acceso más altos que los inicialmente otorgados", True),
            ("El movimiento vertical solo ocurre en sistemas Windows; el lateral en sistemas Linux", False),
            ("El movimiento lateral es siempre detectado por los IDS; el vertical no", False),
        ]
    },
    {
        "enunciado": "¿Qué proceso del ciclo de vida de cuentas se activa cuando un nuevo empleado se incorpora a la organización?",
        "opciones": [
            ("Leaver", False),
            ("Mover", False),
            ("Joiner", True),
            ("Reviewer", False),
        ]
    },
    {
        "enunciado": "¿Qué debe ocurrir con las cuentas de usuario cuando un empleado abandona la organización?",
        "opciones": [
            ("Deben mantenerse activas durante 6 meses por si el empleado vuelve", False),
            ("Deben desactivarse inmediatamente para evitar accesos no autorizados", True),
            ("Deben transferirse al supervisor directo del empleado", False),
            ("Solo deben desactivarse las cuentas de empleados con privilegios de administrador", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el principal riesgo de las cuentas de usuario inactivas que no se desactivan?",
        "opciones": [
            ("Consumen recursos del servidor de autenticación", False),
            ("Pueden ser usadas por atacantes para acceder al sistema sin ser detectados fácilmente, ya que la actividad puede parecer legítima", True),
            ("Generan notificaciones de error en los sistemas IAM", False),
            ("Bloquean automáticamente a otros usuarios del mismo grupo", False),
        ]
    },
    {
        "enunciado": "¿Qué es una 'bóveda de credenciales' en el contexto de PAM?",
        "opciones": [
            ("Un gestor de contraseñas personal para empleados", False),
            ("Un sistema que almacena, rota y gestiona de forma automática las contraseñas de cuentas privilegiadas", True),
            ("Un archivo cifrado donde se guardan las contraseñas de backup", False),
            ("Un módulo del SIEM que almacena los hashes de contraseñas robadas", False),
        ]
    },
    {
        "enunciado": "¿Qué herramienta aplica Machine Learning para detectar comportamientos anómalos de usuarios que podrían indicar abuso de privilegios?",
        "opciones": [
            ("DLP (Data Loss Prevention)", False),
            ("IAM (Identity and Access Management)", False),
            ("UBA/UEBA (User Behavior Analytics / User and Entity Behavior Analytics)", True),
            ("SIEM (Security Information and Event Management)", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el propósito principal de los sistemas DLP en el contexto de la gestión de privilegios?",
        "opciones": [
            ("Gestionar el ciclo de vida de las contraseñas de administrador", False),
            ("Monitorizar el flujo de datos sensibles para detectar y prevenir su uso o transferencia indebida", True),
            ("Detectar intentos de escalado de privilegios en tiempo real", False),
            ("Bloquear el acceso a sistemas externos desde la red corporativa", False),
        ]
    },
    {
        "enunciado": "¿Por qué es importante que quienes realizan las auditorías de privilegios sean personas diferentes a quienes los asignan?",
        "opciones": [
            ("Para reducir la carga de trabajo del equipo de IT", False),
            ("Para evitar conflictos de interés y garantizar la objetividad e independencia de la revisión", True),
            ("Porque la normativa ISO 27001 lo exige en todos los casos", False),
            ("Porque los administradores no tienen conocimiento técnico suficiente para auditar", False),
        ]
    },
    {
        "enunciado": "¿Qué política de seguridad define cómo se gestionan las cuentas, privilegios, autenticación y el ciclo de vida de los usuarios?",
        "opciones": [
            ("Política General de Seguridad de la Información", False),
            ("Política de Gestión de Activos", False),
            ("Política de Control de Accesos", True),
            ("Política de Uso Aceptable de Recursos (AUP)", False),
        ]
    },
    {
        "enunciado": "Una política de 'Uso Aceptable de Recursos (AUP)' tiene como objetivo principal:",
        "opciones": [
            ("Definir los privilegios de administrador de los sistemas corporativos", False),
            ("Especificar qué pueden y qué no pueden hacer los empleados con los recursos corporativos (equipos, internet, email, software)", True),
            ("Establecer los procedimientos de auditoría de accesos privilegiados", False),
            ("Regular la clasificación y el etiquetado de la información confidencial", False),
        ]
    },
    {
        "enunciado": "¿Qué indica el acrónimo JML en el contexto de la administración de cuentas?",
        "opciones": [
            ("Java Management Layer — capa de gestión para aplicaciones Java", False),
            ("Joiner-Mover-Leaver — ciclo de vida completo del acceso de un usuario en la organización", True),
            ("JSON Management Library — biblioteca de gestión de tokens", False),
            ("Joint Monitoring Log — registro conjunto de monitorización de accesos", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes escenarios representa un escalado de privilegios LEGÍTIMO?",
        "opciones": [
            ("Un atacante explota una vulnerabilidad del SO para obtener acceso root", False),
            ("Un empleado usa la cuenta de su compañero con más permisos para completar una tarea", False),
            ("Un técnico solicita formalmente privilegios temporales de administrador para realizar un mantenimiento específico, con aprobación y registro", True),
            ("Un usuario descubre que puede acceder a carpetas de otros departamentos por una ACL mal configurada", False),
        ]
    },
    {
        "enunciado": "¿Qué es el RTO (Recovery Time Objective) en el contexto de la política de BCP/DRP?",
        "opciones": [
            ("El tiempo máximo que una organización puede estar sin operar antes de sufrir daños inaceptables", True),
            ("El punto en el tiempo más antiguo hasta el que se pueden recuperar los datos", False),
            ("El tiempo necesario para completar una auditoría de control de accesos", False),
            ("El tiempo de respuesta objetivo del equipo de seguridad ante un incidente", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes es el objetivo principal de la Política de Clasificación y Manejo de la Información?",
        "opciones": [
            ("Definir los niveles de acceso de cada empleado a los sistemas de la organización", False),
            ("Establecer niveles de sensibilidad de la información (ej. Pública/Interna/Confidencial/Restringida) y cómo se etiqueta, almacena, transmite y destruye", True),
            ("Gestionar el inventario de activos tecnológicos de la organización", False),
            ("Regular el uso de dispositivos personales en el entorno corporativo", False),
        ]
    },
    {
        "enunciado": "Un administrador de sistemas accede a los servidores de producción usando la misma cuenta con la que revisa su correo electrónico. ¿Qué principio de seguridad viola esto?",
        "opciones": [
            ("Principio de confidencialidad", False),
            ("Separación de cuentas de usuario y administrador como parte del principio de mínimo privilegio y separación de privilegios", True),
            ("Principio de disponibilidad del sistema", False),
            ("Política de copias de seguridad", False),
        ]
    },
    {
        "enunciado": "¿Cuándo debe revisarse y actualizarse una política de seguridad de la información?",
        "opciones": [
            ("Solo cuando se produce un incidente de seguridad grave", False),
            ("Periódicamente y también cuando cambien las amenazas, la tecnología o las necesidades empresariales", True),
            ("Una vez al año, siempre en enero, independientemente de los cambios", False),
            ("Solo cuando lo exija una auditoría externa o una normativa", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja aporta la automatización en la gestión del ciclo de vida de cuentas de usuario?",
        "opciones": [
            ("Elimina completamente la necesidad de revisiones manuales periódicas", False),
            ("Reduce errores humanos, mejora la consistencia y acelera los procesos de onboarding y offboarding", True),
            ("Permite que los propios usuarios gestionen sus privilegios sin intervención de IT", False),
            ("Garantiza el cumplimiento automático de todas las normativas sin necesidad de auditorías", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el objetivo principal de la grabación de sesiones privilegiadas en un sistema PAM?",
        "opciones": [
            ("Mejorar el rendimiento de los servidores privilegiados", False),
            ("Permitir la reproducción y auditoría forense de todas las acciones realizadas con cuentas privilegiadas", True),
            ("Bloquear automáticamente las sesiones que superen un tiempo determinado", False),
            ("Reducir el número de cuentas privilegiadas necesarias en la organización", False),
        ]
    },
    {
        "enunciado": "¿Qué debe incluir un checklist de desactivación de cuenta al producirse la baja de un empleado?",
        "opciones": [
            ("Solo la desactivación de la cuenta de correo electrónico corporativo", False),
            ("Todos los sistemas y servicios a los que el usuario tenía acceso, incluyendo aplicaciones, VPNs, accesos físicos y servicios Cloud", True),
            ("Únicamente las cuentas con privilegios de administrador del empleado saliente", False),
            ("El borrado de todos los archivos creados por el empleado durante su estancia", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Ciclo de vida JML y gestión de cuentas",
        "enunciado": (
            "Describe el ciclo de vida completo de una cuenta de usuario siguiendo el modelo JML "
            "(Joiner, Mover, Leaver). Para cada fase indica qué acciones deben realizarse, "
            "quién es responsable y qué riesgos de seguridad pueden aparecer si no se gestiona correctamente. "
            "¿Por qué es importante automatizar este proceso mediante herramientas IAM?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "PAM: Gestión de Accesos Privilegiados",
        "enunciado": (
            "Explica qué es un sistema PAM, cuáles son sus componentes principales y qué problemas resuelve. "
            "¿Por qué las cuentas privilegiadas son el objetivo más valioso para un atacante? "
            "Describe cómo el movimiento lateral y el escalado de privilegios explotan una gestión "
            "deficiente de privilegios y qué medidas concretas del PAM los previenen."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Políticas de seguridad en la organización",
        "enunciado": (
            "Una empresa mediana sin políticas de seguridad documentadas quiere implementarlas por primera vez. "
            "Selecciona las cinco políticas que consideres más prioritarias de las doce estudiadas, "
            "justifica por qué las has elegido y describe brevemente qué debe incluir cada una. "
            "¿Qué relación hay entre la Política de Control de Accesos y las demás políticas?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Segregación de funciones y separación de privilegios",
        "enunciado": (
            "Explica los conceptos de Segregación de Funciones (SoD) y Separación de Privilegios. "
            "¿Por qué son fundamentales para prevenir el fraude y el abuso de accesos? "
            "Describe dos ejemplos concretos donde la falta de SoD podría llevar a un incidente de seguridad o fraude. "
            "¿Cómo se implementa la SoD en un sistema RBAC?"
        ),
        "puntos": 15,
    },
]
