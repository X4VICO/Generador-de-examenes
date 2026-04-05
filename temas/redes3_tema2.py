# ─────────────────────────────────────────────
#  TEMA 2 — Ataques en Redes y Mitigación
#  Asignatura: Redes III
# ─────────────────────────────────────────────

TEMA = {
    "id":         2,
    "nombre":     "Ataques en Redes y Mitigación",
    "asignatura": "Redes III",
}

TEST = [
    {
        "enunciado": "¿Cuál es la diferencia principal entre un ataque DoS y un DDoS?",
        "opciones": [
            ("El DoS usa paquetes UDP y el DDoS usa paquetes TCP", False),
            ("El DoS proviene de una única máquina; el DDoS proviene de múltiples máquinas simultáneamente", True),
            ("El DDoS solo afecta a servidores web; el DoS puede afectar a cualquier servicio", False),
            ("El DoS es detectable y el DDoS no lo es nunca", False),
        ]
    },
    {
        "enunciado": "¿En qué capa del modelo OSI opera un ataque SYN Flood?",
        "opciones": [
            ("Capa 2 — Enlace de datos", False),
            ("Capa 3 — Red", False),
            ("Capa 4 — Transporte", True),
            ("Capa 7 — Aplicación", False),
        ]
    },
    {
        "enunciado": "En un SYN Flood, ¿qué ocurre con las IPs de origen de los paquetes SYN?",
        "opciones": [
            ("Son IPs reales del atacante, que acepta los SYN-ACK del servidor", False),
            ("Son IPs falsificadas (spoofed), por lo que el SYN-ACK nunca llega a nadie que responda", True),
            ("Son IPs de la propia red interna obtenidas mediante ARP Spoofing previo", False),
            ("Son siempre la IP de loopback 127.0.0.1", False),
        ]
    },
    {
        "enunciado": "¿Qué recurso del servidor queda agotado en un ataque SYN Flood?",
        "opciones": [
            ("El espacio en disco del sistema de logs", False),
            ("El ancho de banda del enlace de red", False),
            ("La backlog queue — tabla de conexiones semi-abiertas en estado SYN_RECEIVED", True),
            ("La caché DNS del sistema operativo", False),
        ]
    },
    {
        "enunciado": "¿Cómo funciona la mitigación SYN Cookies?",
        "opciones": [
            ("El firewall bloquea todas las IPs que envíen más de 10 SYN por segundo", False),
            ("El servidor no reserva estado hasta recibir el ACK final, usando una cookie criptográfica en el SYN-ACK", True),
            ("El router descarta los paquetes SYN que no tienen TTL máximo", False),
            ("El IPS reenvía los SYN al servidor solo si la IP origen tiene reputación positiva", False),
        ]
    },
    {
        "enunciado": "¿En qué capa opera un ataque ICMP Flood?",
        "opciones": [
            ("Capa 7 — Aplicación", False),
            ("Capa 4 — Transporte", False),
            ("Capa 3 — Red", True),
            ("Capa 2 — Enlace de datos", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los siguientes es un síntoma típico de un ataque ICMP Flood en la red víctima?",
        "opciones": [
            ("Los usuarios no pueden autenticarse en el Active Directory", False),
            ("Latencia muy alta, pérdida de paquetes generalizada y enlace de red saturado", True),
            ("El servidor web devuelve errores 500 de forma intermitente", False),
            ("La tabla ARP del gateway se llena con entradas duplicadas", False),
        ]
    },
    {
        "enunciado": "¿Por qué un HTTP Flood es más difícil de detectar que un SYN Flood?",
        "opciones": [
            ("Porque opera en capa 2 y los firewalls no inspeccionan esa capa", False),
            ("Porque usa cifrado TLS que impide cualquier análisis de tráfico", False),
            ("Porque completa el three-way handshake y las peticiones son válidas a nivel de protocolo", True),
            ("Porque solo puede lanzarse desde una única IP que rota constantemente", False),
        ]
    },
    {
        "enunciado": "¿Qué recursos agota principalmente un ataque HTTP Flood en el servidor víctima?",
        "opciones": [
            ("La backlog queue TCP y la memoria del stack de red", False),
            ("CPU y recursos de aplicación: hilos de trabajo, conexiones a base de datos, memoria", True),
            ("El ancho de banda del enlace físico de red", False),
            ("La tabla de enrutamiento del sistema operativo", False),
        ]
    },
    {
        "enunciado": "Un atacante lanza un HTTP Flood al endpoint /buscar?q= de una tienda online. ¿Por qué es especialmente devastador?",
        "opciones": [
            ("Porque el puerto 80 no está protegido por ningún firewall", False),
            ("Porque las búsquedas implican consultas a base de datos y lógica de negocio costosa de procesar", True),
            ("Porque ese endpoint no aparece en los logs del servidor web", False),
            ("Porque HTTP GET no requiere autenticación y el firewall siempre lo permite", False),
        ]
    },
    {
        "enunciado": "¿Qué vulnerabilidad de diseño del protocolo ARP permite el ARP Spoofing?",
        "opciones": [
            ("ARP usa cifrado simétrico débil que puede romperse en tiempo real", False),
            ("ARP depende de un servidor centralizado que puede ser comprometido", False),
            ("ARP no autentica las respuestas y acepta ARP Replies no solicitados (gratuitos)", True),
            ("ARP solo funciona en redes con menos de 254 hosts", False),
        ]
    },
    {
        "enunciado": "En un ataque de ARP Spoofing para hacer MitM, ¿a quién envía ARP Replies falsos el atacante?",
        "opciones": [
            ("Solo al router/gateway de la red", False),
            ("Solo a la máquina víctima", False),
            ("Tanto a la víctima como al router/gateway, engañando a ambos simultáneamente", True),
            ("A todos los hosts de la red en broadcast", False),
        ]
    },
    {
        "enunciado": "¿Qué función de los switches gestionables valida los ARP Replies contra la tabla de DHCP Snooping?",
        "opciones": [
            ("STP (Spanning Tree Protocol)", False),
            ("DAI (Dynamic ARP Inspection)", True),
            ("LACP (Link Aggregation Control Protocol)", False),
            ("802.1Q trunking", False),
        ]
    },
    {
        "enunciado": "¿Por qué el ARP Spoofing solo afecta a hosts dentro del mismo dominio de broadcast?",
        "opciones": [
            ("Porque ARP usa TCP y los routers filtran ese tráfico", False),
            ("Porque ARP es un protocolo de capa 2 y los routers no reenvían tramas de broadcast entre segmentos", True),
            ("Porque los switches modernos cifran el tráfico ARP entre VLANs", False),
            ("Porque ARP Spoofing requiere acceso físico al cable de red", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes herramientas se usa en laboratorio para generar tráfico de ataque con control sobre cabeceras TCP/IP?",
        "opciones": [
            ("Wireshark", False),
            ("ss", False),
            ("hping3", True),
            ("arpwatch", False),
        ]
    },
    {
        "enunciado": "¿Qué hace la herramienta arpwatch en el contexto de seguridad de red?",
        "opciones": [
            ("Genera ARP Replies falsos para testear la resiliencia de la red", False),
            ("Monitoriza la caché ARP y alerta cuando una IP cambia de MAC de forma inesperada", True),
            ("Bloquea automáticamente los paquetes ARP no solicitados en el switch", False),
            ("Escanea la red en busca de hosts con ARP Spoofing activo", False),
        ]
    },
    {
        "enunciado": "¿En qué consiste el proceso de hardening de un sistema?",
        "opciones": [
            ("Instalar el firewall perimetral más potente disponible en el mercado", False),
            ("Reducir la superficie de ataque eliminando servicios, usuarios, puertos y permisos innecesarios", True),
            ("Realizar copias de seguridad diarias de la configuración de todos los dispositivos", False),
            ("Cifrar todo el tráfico de red con TLS 1.3", False),
        ]
    },
    {
        "enunciado": "¿Cuál de las siguientes es una medida de hardening válida para un servidor web?",
        "opciones": [
            ("Habilitar todos los módulos del servidor web para mayor compatibilidad", False),
            ("Mantener la cuenta de administrador por defecto con la contraseña del fabricante", False),
            ("Deshabilitar Telnet y usar SSH con autenticación por clave pública", True),
            ("Desactivar los logs de acceso para reducir la carga de disco", False),
        ]
    },
    {
        "enunciado": "¿Para qué se usa tcpdump en el contexto de análisis de ataques?",
        "opciones": [
            ("Para generar tráfico de prueba y simular ataques DoS en laboratorio", False),
            ("Para capturar tráfico de red en línea de comandos y guardar PCAPs para análisis posterior", True),
            ("Para bloquear automáticamente IPs que superen un umbral de paquetes por segundo", False),
            ("Para gestionar y actualizar las firmas del IDS/IPS", False),
        ]
    },
    {
        "enunciado": "Un atacante lanza un SYN Flood desde una sola máquina con IP real. ¿Qué contramedida lo mitigaría de forma más inmediata?",
        "opciones": [
            ("Activar SYN Cookies en el servidor víctima", False),
            ("Desplegar un segundo servidor web en modo balanceo de carga", False),
            ("Bloquear la IP origen en el firewall o mediante rate limiting", True),
            ("Aumentar el tamaño del enlace de red del servidor", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Mecanismo del SYN Flood",
        "enunciado": (
            "Describe el mecanismo detallado de un SYN Flood: qué hace el atacante, qué estado TCP "
            "se acumula en el servidor, qué recurso se agota y cuáles son las consecuencias. "
            "Explica cómo funciona la mitigación con SYN Cookies."
        ),
        "puntos": 15,
    },
    {
        "titulo": "SYN Flood vs HTTP Flood",
        "enunciado": (
            "Compara el SYN Flood con el HTTP Flood en términos de: capa OSI, recursos que agotan "
            "en el servidor víctima y dificultad de detección. "
            "¿Por qué el SYN Flood es efectivo con pocos recursos del atacante?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Contramedidas HTTP Flood",
        "enunciado": (
            "Propón tres contramedidas para mitigar un HTTP Flood. "
            "Para cada una indica: en qué capa OSI actúa, cómo funciona exactamente "
            "y qué limitación tiene frente a un DDoS distribuido real con miles de IPs distintas."
        ),
        "puntos": 15,
    },
    {
        "titulo": "ARP Spoofing y MitM",
        "enunciado": (
            "Explica el mecanismo del ARP Spoofing: qué vulnerabilidad del protocolo explota, "
            "cómo consigue el atacante posicionarse como MitM, cómo se detecta con Wireshark "
            "y cómo se mitiga con DAI y DHCP Snooping."
        ),
        "puntos": 15,
    },
]
