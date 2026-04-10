# ─────────────────────────────────────────────
#  CONTROL D'ACCÉS — Mòdul 2
#  Principis Bàsics i Models de Control d'Accés
#  Asignatura: Control d'Accés
# ─────────────────────────────────────────────

TEMA = {
    "id":         11,
    "nombre":     "Modelos de Control de Acceso (DAC, MAC, RBAC, ABAC)",
    "asignatura": "Control d'Accés",
}

TEST = [
    {
        "enunciado": "En el modelo DAC (Control de Acceso Discrecional), ¿quién decide los permisos de acceso a un recurso?",
        "opciones": [
            ("La administración central del sistema mediante políticas predefinidas", False),
            ("El propietario o creador del recurso", True),
            ("El departamento de seguridad de la organización", False),
            ("El sistema operativo en función de las etiquetas asignadas", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal desventaja del modelo DAC en organizaciones grandes?",
        "opciones": [
            ("No permite asignar permisos granulares a los usuarios", False),
            ("No se puede implementar en entornos Windows ni Linux", False),
            ("Depende del criterio individual de cada propietario de recurso, lo que dificulta la gestión y auditoría a escala", True),
            ("Requiere etiquetas de seguridad para cada recurso, lo que lo hace muy complejo", False),
        ]
    },
    {
        "enunciado": "¿En qué tipo de entorno es más adecuado el modelo MAC (Control de Acceso Obligatorio)?",
        "opciones": [
            ("Pequeñas empresas con pocos usuarios", False),
            ("Instalaciones militares, gubernamentales y organizaciones con información altamente sensible", True),
            ("Startups tecnológicas que necesitan flexibilidad para compartir recursos", False),
            ("Plataformas de comercio electrónico con millones de usuarios", False),
        ]
    },
    {
        "enunciado": "En el modelo MAC, ¿qué mecanismo controla si un sujeto puede acceder a un objeto?",
        "opciones": [
            ("El propio sujeto establece sus permisos de acceso", False),
            ("El administrador del objeto decide caso por caso quién puede acceder", False),
            ("Las etiquetas de seguridad asignadas a sujetos y objetos, comparadas con las políticas centralizadas", True),
            ("La hora del día y la ubicación geográfica del sujeto", False),
        ]
    },
    {
        "enunciado": "En el modelo RBAC, ¿cómo obtiene un usuario sus permisos de acceso?",
        "opciones": [
            ("Se le asignan directamente permisos individuales por el administrador", False),
            ("Los hereda al ser asignado a uno o más roles que ya tienen permisos definidos", True),
            ("Los negocia con el propietario de cada recurso que necesita usar", False),
            ("Se generan automáticamente en función de sus atributos personales", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja principal aporta el modelo RBAC respecto a la administración de permisos?",
        "opciones": [
            ("Permite que cada usuario personalice sus propios permisos", False),
            ("Los cambios en los permisos de un rol se propagan automáticamente a todos los usuarios que tienen ese rol asignado", True),
            ("Elimina completamente la necesidad de auditorías de acceso", False),
            ("Funciona mejor que cualquier otro modelo en entornos con alta seguridad requerida", False),
        ]
    },
    {
        "enunciado": "¿Qué es la Segregación de Funciones (SoD) en el contexto del RBAC?",
        "opciones": [
            ("Dividir los roles en categorías según el departamento organizacional", False),
            ("Asegurar que un solo rol no tenga demasiado poder distribuyendo tareas críticas entre diferentes roles", True),
            ("Separar los permisos de lectura de los permisos de escritura en todos los recursos", False),
            ("Crear roles diferentes para entornos cloud y on-premise", False),
        ]
    },
    {
        "enunciado": "En el modelo ABAC, ¿qué tipo de información puede usarse para tomar una decisión de acceso?",
        "opciones": [
            ("Solo el nombre de usuario y su contraseña", False),
            ("Únicamente el rol asignado al usuario en la organización", False),
            ("Atributos del usuario, del recurso, de la acción y del contexto (hora, ubicación, dispositivo)", True),
            ("Solo las etiquetas de seguridad asignadas por la administración central", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal ventaja del modelo ABAC respecto al RBAC?",
        "opciones": [
            ("Es más simple de implementar y gestionar", False),
            ("Ofrece mayor granularidad y puede considerar el contexto en tiempo real para tomar decisiones de acceso", True),
            ("No requiere ningún tipo de política predefinida", False),
            ("Es más adecuado para entornos militares donde la seguridad es crítica", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal desventaja del modelo ABAC?",
        "opciones": [
            ("No permite políticas dinámicas ni basadas en contexto", False),
            ("Solo funciona en entornos Cloud, no on-premise", False),
            ("Es el modelo más complejo de implementar y gestionar, requiriendo un sistema robusto para gestionar múltiples atributos y políticas", True),
            ("No escala bien en organizaciones con más de 100 usuarios", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los cuatro modelos ofrece la mayor seguridad en entornos donde la confidencialidad es crítica?",
        "opciones": [
            ("DAC", False),
            ("MAC", True),
            ("RBAC", False),
            ("ABAC", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los cuatro modelos es más adecuado para un entorno empresarial mediano con estructura organizacional bien definida?",
        "opciones": [
            ("DAC, por su flexibilidad individual", False),
            ("MAC, por su alto nivel de seguridad", False),
            ("RBAC, por su escalabilidad y facilidad de gestión en organizaciones con roles definidos", True),
            ("ABAC, por su granularidad", False),
        ]
    },
    {
        "enunciado": "El Principio de Mínimo Privilegio establece que:",
        "opciones": [
            ("Todos los usuarios deben tener los mismos permisos para garantizar la equidad", False),
            ("Solo se otorgan los accesos y permisos estrictamente necesarios para realizar las tareas asignadas", True),
            ("Los administradores no necesitan restricciones de acceso al ser de confianza", False),
            ("Los permisos deben revisarse una vez al año como máximo", False),
        ]
    },
    {
        "enunciado": "¿Qué son las ACLs (Listas de Control de Acceso) en el contexto de la autorización?",
        "opciones": [
            ("Registros de todas las acciones realizadas por los usuarios en el sistema", False),
            ("Listas que definen qué usuarios o grupos tienen permisos específicos (lectura, escritura, ejecución) sobre un objeto particular", True),
            ("Listas de usuarios bloqueados por intentos fallidos de acceso", False),
            ("Registros de auditoría de los cambios realizados en los permisos de los sistemas", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el propósito principal de realizar revisiones periódicas de accesos?",
        "opciones": [
            ("Aumentar el número de roles definidos en el sistema RBAC", False),
            ("Asegurar que los permisos siguen siendo apropiados, especialmente tras cambios en funciones o responsabilidades", True),
            ("Generar informes estadísticos sobre el uso de los sistemas", False),
            ("Identificar qué usuarios han olvidado sus contraseñas", False),
        ]
    },
    {
        "enunciado": "En términos de escalabilidad, ¿qué modelo escala peor cuando la organización crece significativamente en número de usuarios y recursos?",
        "opciones": [
            ("DAC, porque cada recurso se controla individualmente y la gestión se vuelve inmanejable", True),
            ("MAC, porque las etiquetas de seguridad no pueden ampliarse", False),
            ("RBAC, porque los roles no pueden asignarse a más de 100 usuarios", False),
            ("ABAC, porque los atributos no pueden ampliarse una vez definidos", False),
        ]
    },
    {
        "enunciado": "Un sistema universitario permite el acceso a un examen solo si el usuario es estudiante matriculado en esa asignatura, accede desde la red del campus y durante el horario del examen. ¿Qué modelo de CA representa mejor este escenario?",
        "opciones": [
            ("DAC — el profesor decide quién puede ver el examen", False),
            ("MAC — el examen tiene una etiqueta de seguridad que solo los estudiantes pueden ver", False),
            ("RBAC — el rol 'Estudiante' tiene acceso al examen", False),
            ("ABAC — la decisión evalúa atributos del usuario, recurso y contexto simultáneamente", True),
        ]
    },
    {
        "enunciado": "¿Qué normativa europea tiene un impacto directo en la necesidad de implementar controles de acceso robustos para proteger datos personales?",
        "opciones": [
            ("PCI DSS", False),
            ("FERPA", False),
            ("GDPR", True),
            ("HIPAA", False),
        ]
    },
    {
        "enunciado": "La gestión de identidades (IdM) permite, entre otras cosas:",
        "opciones": [
            ("Solo la creación de nuevas cuentas de usuario", False),
            ("La creación, gestión y eliminación de cuentas, además del control de perfiles, roles y credenciales", True),
            ("Únicamente la autenticación de usuarios mediante contraseñas", False),
            ("La gestión exclusiva de dispositivos físicos de acceso como tokens y tarjetas", False),
        ]
    },
    {
        "enunciado": "¿Qué diferencia fundamental existe entre el control de acceso físico y el lógico?",
        "opciones": [
            ("El físico es siempre más seguro que el lógico", False),
            ("El físico controla el acceso a espacios y dispositivos tangibles; el lógico controla el acceso a sistemas informáticos y datos digitales", True),
            ("El lógico solo aplica a dispositivos móviles; el físico a edificios y servidores", False),
            ("No hay diferencia, ambos términos son sinónimos en ciberseguridad", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Comparativa de los cuatro modelos de CA",
        "enunciado": (
            "Compara los cuatro modelos de Control de Acceso (DAC, MAC, RBAC y ABAC) en términos de: "
            "quién toma las decisiones de acceso, nivel de seguridad, flexibilidad, complejidad y escalabilidad. "
            "Para cada modelo indica un caso de uso real donde sería la opción más adecuada y justifica por qué."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Diseño RBAC para una organización",
        "enunciado": (
            "Una empresa de desarrollo de software tiene los siguientes perfiles: "
            "Desarrollador Junior, Desarrollador Senior, DevOps, QA Tester, Project Manager y Director Técnico. "
            "Diseña un esquema RBAC básico: define qué permisos tendría cada rol sobre los recursos "
            "(código fuente, servidores de producción, base de datos, panel de facturación, documentación interna). "
            "Aplica el principio de mínimo privilegio y la Segregación de Funciones (SoD) y justifica las decisiones más importantes."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Principio de Mínimo Privilegio",
        "enunciado": (
            "Explica en detalle el Principio de Mínimo Privilegio: qué significa, cómo se implementa en la práctica "
            "y qué beneficios aporta a la seguridad. "
            "¿Qué relación tiene con la Segregación de Funciones? "
            "Describe tres situaciones concretas donde no aplicarlo podría llevar a un incidente de seguridad."
        ),
        "puntos": 15,
    },
    {
        "titulo": "ABAC en entornos dinámicos",
        "enunciado": (
            "Explica cómo funciona el modelo ABAC y por qué es especialmente útil en entornos dinámicos y complejos. "
            "Diseña tres políticas ABAC para una empresa que permita el acceso a sus sistemas solo bajo ciertas condiciones "
            "(combina atributos de usuario, recurso y contexto). "
            "¿Cuáles son las principales dificultades de implementar ABAC y cómo se pueden mitigar?"
        ),
        "puntos": 15,
    },
]
