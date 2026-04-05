# ─────────────────────────────────────────────
#  TEMA 1 — Firewall y DMZ
#  Asignatura: Redes III
# ─────────────────────────────────────────────
#
#  FORMATO DE PREGUNTA TEST:
#  {
#      "enunciado": "texto de la pregunta",
#      "opciones": [
#          ("texto opción", True/False),   ← True = correcta (solo una)
#          ...
#      ]
#  }
#
#  FORMATO DE PREGUNTA REDACCIÓN:
#  {
#      "titulo":   "título corto",
#      "enunciado": "enunciado completo",
#      "puntos":   15,
#  }
# ─────────────────────────────────────────────

TEMA = {
    "id":         1,
    "nombre":     "Firewall y DMZ",
    "asignatura": "Redes III",
}

TEST = [
    {
        "enunciado": "¿En qué capas del modelo OSI opera un firewall stateful inspection?",
        "opciones": [
            ("Capa 2 y 3", False),
            ("Capa 3 y 4", True),
            ("Capa 5 y 6", False),
            ("Capa 7 únicamente", False),
        ]
    },
    {
        "enunciado": "Un firewall stateful mantiene una tabla de estado. ¿Qué información contiene?",
        "opciones": [
            ("Las direcciones MAC de todos los hosts conectados", False),
            ("Los logs de acceso de los últimos 30 días", False),
            ("La 5-tupla de cada conexión activa: IP origen, IP destino, puerto origen, puerto destino y protocolo", True),
            ("Las rutas de la tabla de enrutamiento del router adyacente", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la regla implícita que todo firewall aplica al final de su lista de reglas?",
        "opciones": [
            ("Permit all — permite todo el tráfico no clasificado", False),
            ("Log all — registra todo el tráfico sin bloquearlo", False),
            ("Deny all — bloquea todo el tráfico que no coincidió con ninguna regla anterior", True),
            ("Forward all — reenvía el tráfico no clasificado al siguiente dispositivo", False),
        ]
    },
    {
        "enunciado": "¿Por qué las reglas de un firewall deben ordenarse de más específica a más genérica?",
        "opciones": [
            ("Para reducir el consumo de CPU al procesar paquetes", False),
            ("Porque las reglas genéricas al principio pueden tapar reglas específicas y nunca evaluarlas", True),
            ("Porque los firewalls solo leen las primeras 10 reglas de la lista", False),
            ("Para facilitar la exportación de la configuración a otros dispositivos", False),
        ]
    },
    {
        "enunciado": "¿Qué tipo de firewall podría detectar un ataque de inyección SQL dentro de una petición HTTP válida?",
        "opciones": [
            ("Packet filter", False),
            ("Circuit-level gateway", False),
            ("Stateful inspection", False),
            ("Application layer firewall (NGFW)", True),
        ]
    },
    {
        "enunciado": "En una arquitectura DMZ con doble firewall, ¿qué zonas separa el firewall interno?",
        "opciones": [
            ("Internet y la DMZ", False),
            ("La DMZ y la LAN interna", True),
            ("La LAN interna y la VLAN de gestión", False),
            ("Dos segmentos de DMZ diferentes", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes servicios es típico desplegar en una DMZ?",
        "opciones": [
            ("El servidor de base de datos con datos de clientes", False),
            ("El directorio activo (Active Directory) corporativo", False),
            ("El servidor web público (HTTP/HTTPS)", True),
            ("El servidor de ficheros interno de la empresa", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja aporta usar firewalls de distinto fabricante en una arquitectura de doble firewall?",
        "opciones": [
            ("Reducen el coste total de la infraestructura", False),
            ("Simplifican la gestión centralizada de reglas", False),
            ("Evitan que una vulnerabilidad afecte a ambos firewalls simultáneamente", True),
            ("Permiten mayor velocidad de inspección del tráfico", False),
        ]
    },
    {
        "enunciado": "¿Qué protocolo usa un enlace troncal (trunk link) para identificar a qué VLAN pertenece cada trama?",
        "opciones": [
            ("STP (Spanning Tree Protocol)", False),
            ("802.1Q", True),
            ("802.11", False),
            ("LACP", False),
        ]
    },
    {
        "enunciado": "¿Cuál es el principal beneficio de seguridad de segmentar la red con VLANs?",
        "opciones": [
            ("Cifrar el tráfico entre hosts de distintas VLANs automáticamente", False),
            ("Eliminar la necesidad de un firewall perimetral", False),
            ("Limitar el radio de acción de ataques de capa 2 al dominio de broadcast de la VLAN", True),
            ("Aumentar el ancho de banda disponible para cada host", False),
        ]
    },
    {
        "enunciado": "¿Qué ataque explota la ausencia de autenticación en ARP para comprometer una VLAN?",
        "opciones": [
            ("SYN Flood", False),
            ("VLAN Hopping", False),
            ("ARP Spoofing", True),
            ("MAC Flooding", False),
        ]
    },
    {
        "enunciado": "¿Qué función tiene el DHCP Snooping en la seguridad de una red con VLANs?",
        "opciones": [
            ("Asignar IPs estáticas a los servidores de la DMZ", False),
            ("Registrar qué IP ha sido asignada a qué MAC en qué puerto, sirviendo de base para DAI", True),
            ("Bloquear el tráfico DHCP entre VLANs diferentes", False),
            ("Cifrar las comunicaciones entre el servidor DHCP y los clientes", False),
        ]
    },
    {
        "enunciado": "¿Qué ocurre si un enlace troncal entre dos switches queda saturado?",
        "opciones": [
            ("Solo se ve afectada la VLAN con mayor prioridad configurada", False),
            ("El switch redirige automáticamente el tráfico por otro enlace físico", False),
            ("Todas las VLANs que atraviesan ese enlace sufren degradación simultáneamente", True),
            ("El tráfico de gestión tiene prioridad y el resto se descarta", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la diferencia entre una regla con acción deny y una con acción drop en un firewall?",
        "opciones": [
            ("Deny bloquea solo tráfico TCP; drop bloquea solo tráfico UDP", False),
            ("Deny notifica al emisor con un mensaje de rechazo; drop descarta el paquete silenciosamente", True),
            ("Son sinónimos, ambas hacen exactamente lo mismo", False),
            ("Drop es más lento que deny porque requiere procesamiento adicional", False),
        ]
    },
    {
        "enunciado": "¿Cómo se mitiga el ataque de VLAN Hopping?",
        "opciones": [
            ("Saturando el enlace troncal con QoS", False),
            ("Desactivando el auto-trunking en puertos de acceso y usando una VLAN nativa sin tráfico de usuario", True),
            ("Activando STP en todos los switches", False),
            ("Aplicando ACLs entre VLANs en el router", False),
        ]
    },
    {
        "enunciado": "¿Qué significa aplicar el principio de mínimo privilegio en el diseño de reglas de un firewall?",
        "opciones": [
            ("Usar el firewall con menos funcionalidades para reducir su superficie de ataque", False),
            ("Permitir únicamente el tráfico estrictamente necesario y denegar todo lo demás", True),
            ("Asignar la gestión del firewall al usuario con menos permisos del sistema", False),
            ("Configurar el menor número posible de reglas para simplificar la gestión", False),
        ]
    },
    {
        "enunciado": "Un servidor web en la DMZ es comprometido. ¿Qué impide al atacante acceder directamente a la LAN?",
        "opciones": [
            ("El propio servidor web tiene un firewall local que bloquea el acceso a la LAN", False),
            ("El firewall interno entre DMZ y LAN bloquea el tráfico no autorizado desde la DMZ hacia la LAN", True),
            ("Las VLANs cifran automáticamente el tráfico impidiendo el movimiento lateral", False),
            ("El router de borde descarta el tráfico que no viene de Internet", False),
        ]
    },
    {
        "enunciado": "¿En qué se diferencia un packet filter de un stateful firewall ante un paquete TCP ACK sin sesión previa?",
        "opciones": [
            ("Ambos lo bloquean porque el flag ACK indica una sesión no iniciada", False),
            ("El packet filter lo permite si el puerto está abierto en las reglas; el stateful lo bloquea porque no hay sesión activa", True),
            ("El stateful lo permite siempre que venga de una IP de confianza; el packet filter lo bloquea", False),
            ("No hay diferencia, ambos toman la misma decisión", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes es una buena práctica en la gestión continua de reglas de un firewall?",
        "opciones": [
            ("Añadir nuevas reglas siempre al final de la lista para no alterar el orden existente", False),
            ("Revisar y eliminar periódicamente reglas obsoletas para no aumentar la superficie de ataque", True),
            ("Deshabilitar el logging para reducir la carga de procesamiento del firewall", False),
            ("Usar reglas any/any como base y añadir excepciones específicas", False),
        ]
    },
    {
        "enunciado": "¿Qué capa del modelo OSI inspeccionan las ACLs aplicadas entre VLANs en un router o switch de capa 3?",
        "opciones": [
            ("Capa 2 — analizan direcciones MAC", False),
            ("Capa 3 — analizan direcciones IP, protocolo y puerto", True),
            ("Capa 7 — analizan el contenido de los paquetes", False),
            ("Capa 1 — analizan la señal física del enlace", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Firewall stateful vs NGFW",
        "enunciado": (
            "Explica la diferencia entre un firewall stateful y un NGFW de capa 7. "
            "¿Qué información analiza cada uno y en qué capa OSI opera? "
            "Pon un ejemplo de ataque que el stateful NO detectaría pero el NGFW SÍ."
        ),
        "puntos": 15,
    },
    {
        "titulo": "Arquitectura DMZ doble firewall",
        "enunciado": (
            "Explica por qué una arquitectura DMZ con doble firewall aporta mayor seguridad "
            "que una de un solo firewall. Usa el concepto de defensa en profundidad. "
            "Indica qué zonas separa cada firewall y qué ocurre si el firewall externo es comprometido."
        ),
        "puntos": 15,
    },
    {
        "titulo": "VLANs y segmentación de red",
        "enunciado": (
            "Explica qué son las VLANs, qué es el dominio de broadcast y cómo la segmentación "
            "con VLANs limita el impacto de un ARP Spoofing. "
            "¿Qué medida técnica complementaria usarías en el switch para reforzar la seguridad ARP?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Caso práctico: auditoría de firewall",
        "enunciado": (
            "Un auditor encuentra esta configuración: un único firewall packet filter con una regla "
            "'permit any any' al inicio, la base de datos de clientes en la DMZ junto al servidor web, "
            "y sin VLANs internas. Identifica todos los problemas de seguridad y propón una arquitectura mejorada."
        ),
        "puntos": 15,
    },
]
