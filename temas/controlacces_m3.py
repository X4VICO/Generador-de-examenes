# ─────────────────────────────────────────────
#  CONTROL D'ACCÉS — Mòdul 3
#  Sistemes d'Identificació i Autenticació
#  Asignatura: Control d'Accés
# ─────────────────────────────────────────────

TEMA = {
    "id":         12,
    "nombre":     "Identificación, Autenticación y MFA",
    "asignatura": "Control d'Accés",
}

TEST = [
    {
        "enunciado": "¿Cuál de los siguientes es un método de autenticación del tipo 'algo que el usuario sabe'?",
        "opciones": [
            ("Huella dactilar", False),
            ("Token de seguridad físico", False),
            ("Contraseña o PIN", True),
            ("Tarjeta inteligente con chip", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes es un método de autenticación del tipo 'algo que el usuario tiene'?",
        "opciones": [
            ("Reconocimiento facial", False),
            ("Respuesta a una pregunta de seguridad", False),
            ("Aplicación de autenticación móvil que genera TOTP", True),
            ("Contraseña maestra del gestor de contraseñas", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes representa el factor 'algo que el usuario es'?",
        "opciones": [
            ("PIN de 6 dígitos", False),
            ("USB Key con clave criptográfica", False),
            ("Escaneo de iris", True),
            ("Código OTP enviado por SMS", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal ventaja de las aplicaciones de autenticación móvil (TOTP) respecto a los tokens físicos?",
        "opciones": [
            ("Son más seguras porque generan códigos más largos", False),
            ("No pueden ser interceptadas bajo ningún concepto", False),
            ("Son más baratas y accesibles gracias a la omnipresencia de los smartphones", True),
            ("No dependen de la seguridad del dispositivo donde se instalan", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la vulnerabilidad más conocida de las aplicaciones de autenticación móvil?",
        "opciones": [
            ("Los códigos TOTP no expiran nunca", False),
            ("Son vulnerables a ataques de SIM swapping y dependen de la seguridad del dispositivo móvil", True),
            ("No se pueden usar en combinación con contraseñas", False),
            ("Solo funcionan con conexión a internet activa", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja de seguridad específica aportan los tokens físicos USB Key respecto a otros métodos de autenticación?",
        "opciones": [
            ("Generan contraseñas más largas que cualquier otro método", False),
            ("Requieren posesión física del dispositivo, lo que previene la mayoría de ataques remotos", True),
            ("Son el método más económico de implementar en organizaciones grandes", False),
            ("Funcionan sin necesidad de ningún driver ni software adicional", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes métodos biométricos ofrece los niveles más altos de seguridad y precisión?",
        "opciones": [
            ("Reconocimiento facial por cámara de smartphone", False),
            ("Huella dactilar en sensor capacitivo", False),
            ("Escaneo del iris", True),
            ("Reconocimiento de voz", False),
        ]
    },
    {
        "enunciado": "¿Qué es un 'falso negativo' (FAR) en un sistema biométrico?",
        "opciones": [
            ("El sistema acepta a un impostor como usuario legítimo", False),
            ("El sistema no reconoce a un usuario autorizado y le deniega el acceso", True),
            ("El sensor biométrico genera un error de lectura por condiciones ambientales", False),
            ("El sistema genera dos identificadores iguales para usuarios distintos", False),
        ]
    },
    {
        "enunciado": "¿Por qué los datos biométricos requieren una protección especial respecto a otros datos de autenticación?",
        "opciones": [
            ("Porque son más fáciles de robar que las contraseñas", False),
            ("Porque son inherentemente imprecisos y necesitan verificación adicional", False),
            ("Porque si se comprometen no se pueden cambiar como una contraseña — son permanentes e irreemplazables", True),
            ("Porque están protegidos por una normativa específica solo aplicable a biometría", False),
        ]
    },
    {
        "enunciado": "¿Cuántos factores de autenticación como mínimo requiere la MFA (Autenticación Multifactor)?",
        "opciones": [
            ("Solo uno, pero muy robusto", False),
            ("Dos o más factores de diferente categoría", True),
            ("Exactamente tres factores siempre", False),
            ("El número de factores que el sistema operativo determine", False),
        ]
    },
    {
        "enunciado": "¿Por qué la MFA protege mejor contra el phishing que la autenticación solo con contraseña?",
        "opciones": [
            ("Porque hace que las contraseñas sean más largas y seguras", False),
            ("Porque incluso si el atacante obtiene la contraseña, necesita comprometer también los otros factores de autenticación", True),
            ("Porque el phishing no puede robar contraseñas de páginas que usan MFA", False),
            ("Porque la MFA cifra todas las credenciales de forma automática", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el factor MFA 'algo que el usuario ubica'?",
        "opciones": [
            ("El nombre de la ciudad de nacimiento del usuario", False),
            ("La dirección IP del dispositivo o datos de geolocalización GPS para restringir accesos desde lugares no habituales", True),
            ("La dirección postal del domicilio del empleado", False),
            ("El nombre de la red WiFi a la que el usuario suele conectarse", False),
        ]
    },
    {
        "enunciado": "En el SSO (Single Sign-On), ¿qué emite el sistema tras la autenticación inicial para que el usuario no tenga que volver a autenticarse?",
        "opciones": [
            ("Una contraseña temporal de un solo uso", False),
            ("Un token de sesión (como JWT o SAML Assertion) con información de identidad y permisos", True),
            ("Un certificado digital válido permanentemente", False),
            ("Una cookie de sesión sin caducidad", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el principal riesgo de seguridad del SSO?",
        "opciones": [
            ("Obliga a los usuarios a recordar más contraseñas", False),
            ("Si las credenciales del SSO se comprometen, el atacante obtiene acceso a todos los servicios integrados en él", True),
            ("Impide la implementación de MFA en los sistemas integrados", False),
            ("Solo funciona con aplicaciones locales, no con servicios Cloud", False),
        ]
    },
    {
        "enunciado": "Para proteger los tokens de sesión en un sistema SSO, ¿cuál de las siguientes prácticas es correcta?",
        "opciones": [
            ("Almacenar los tokens en localStorage del navegador para acceso rápido", False),
            ("Asignar a los tokens un período de validez indefinido para mejorar la experiencia de usuario", False),
            ("Transmitirlos solo a través de conexiones TLS, usar cookies con flags HttpOnly y Secure, y establecer períodos de validez limitados", True),
            ("Compartir el mismo token entre varios usuarios del mismo departamento", False),
        ]
    },
    {
        "enunciado": "¿Qué es el reconocimiento de venas de la mano como método biométrico y cuál es su principal ventaja?",
        "opciones": [
            ("Analiza los patrones superficiales de la piel; ventaja: funciona con guantes puestos", False),
            ("Analiza el patrón vascular interno de la palma; ventaja: es muy difícil de capturar o replicar por ser interno", True),
            ("Analiza el movimiento al escribir; ventaja: no requiere contacto físico con el sensor", False),
            ("Analiza las huellas de los nudillos; ventaja: es más preciso que la huella dactilar", False),
        ]
    },
    {
        "enunciado": "¿Qué implica el principio de 'limitación de almacenamiento' en el contexto de los datos biométricos?",
        "opciones": [
            ("Los datos biométricos deben almacenarse en servidores con capacidad limitada", False),
            ("Los datos biométricos solo deben conservarse el tiempo estrictamente necesario para el propósito específico para el que fueron recopilados", True),
            ("Los datos biométricos no pueden almacenarse en servidores Cloud", False),
            ("El almacenamiento de datos biométricos está limitado a un máximo de 1GB por usuario", False),
        ]
    },
    {
        "enunciado": "¿Qué norma relevante establece requisitos específicos para la autenticación en el acceso a datos de tarjetas de crédito?",
        "opciones": [
            ("GDPR", False),
            ("HIPAA", False),
            ("PCI DSS", True),
            ("FERPA", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes afirmaciones sobre las preguntas de seguridad como método de autenticación es correcta?",
        "opciones": [
            ("Son el método más robusto de autenticación individual", False),
            ("Su seguridad depende de la naturaleza de las preguntas; muchas respuestas son públicas o fácilmente investigables", True),
            ("Están recomendadas como único factor de autenticación en sistemas bancarios", False),
            ("No pueden ser comprometidas mediante ingeniería social", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal razón por la que la MFA mejora la cultura de seguridad de una organización?",
        "opciones": [
            ("Elimina completamente la necesidad de contraseñas", False),
            ("Al requerir múltiples verificaciones, hace que los usuarios sean más conscientes de la seguridad en cada acceso", True),
            ("Reduce el número de incidentes de seguridad a cero", False),
            ("Permite a los administradores ver las contraseñas de los usuarios", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Los tres factores de autenticación",
        "enunciado": (
            "Describe en detalle los tres factores clásicos de autenticación (algo que sabes, algo que tienes, algo que eres). "
            "Para cada factor enumera al menos tres métodos concretos, indica sus principales fortalezas y debilidades "
            "y explica en qué situaciones es más apropiado cada uno. "
            "¿Por qué la combinación de factores aumenta la seguridad de forma exponencial?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Sistemas biométricos: ventajas, retos y privacidad",
        "enunciado": (
            "Explica qué son los sistemas biométricos y qué tipos existen (al menos cuatro). "
            "Describe los conceptos de falso positivo y falso negativo y su impacto en la seguridad. "
            "¿Cuáles son los principales desafíos en cuanto a privacidad y protección de datos biométricos? "
            "¿Por qué son especialmente sensibles comparados con una contraseña?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Implementación de MFA en una organización",
        "enunciado": (
            "Una empresa quiere implementar MFA para todos sus empleados. "
            "Describe el proceso completo: cómo evaluar qué sistemas lo requieren, "
            "cómo elegir los métodos adecuados para distintos perfiles de usuario, "
            "cómo gestionar la resistencia al cambio y cómo planificar la respuesta si un método falla. "
            "¿Qué equilibrio debe buscarse entre seguridad y usabilidad?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "SSO: funcionamiento, ventajas y riesgos",
        "enunciado": (
            "Explica cómo funciona un sistema SSO describiendo el papel de los tokens de sesión. "
            "¿Qué ventajas aporta respecto a la autenticación independiente en cada aplicación? "
            "¿Cuáles son sus principales riesgos y cómo se mitigan? "
            "¿Es compatible el SSO con el modelo Zero Trust? Razona tu respuesta."
        ),
        "puntos": 15,
    },
]
