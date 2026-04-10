# ─────────────────────────────────────────────
#  TEMA 3 — IDS/IPS y SIEM
#  Asignatura: Redes III
# ─────────────────────────────────────────────

TEMA = {
    "id":         3,
    "nombre":     "IDS/IPS y SIEM",
    "asignatura": "Redes III",
}

TEST = [
    {
        "enunciado": "¿Cuál es la diferencia fundamental entre un IDS y un IPS en cuanto a su posición en la red?",
        "opciones": [
            ("El IDS se despliega en la nube y el IPS siempre on-premise", False),
            ("El IDS actúa fuera de banda y solo genera alertas; el IPS actúa en línea y puede bloquear tráfico", True),
            ("El IDS analiza tráfico cifrado y el IPS solo tráfico en claro", False),
            ("El IDS usa firmas y el IPS solo detección por anomalía", False),
        ]
    },
    {
        "enunciado": "¿Qué tipo de IPS protege un host individual en lugar de un segmento de red?",
        "opciones": [
            ("NIPS (Network IPS)", False),
            ("WIPS (Wireless IPS)", False),
            ("HIPS (Host IPS)", True),
            ("Cloud IPS", False),
        ]
    },
    {
        "enunciado": "¿Qué método de detección compara el tráfico contra una base de datos de patrones de ataques conocidos?",
        "opciones": [
            ("Detección por anomalía", False),
            ("Detección por política", False),
            ("Detección por firma (signature-based)", True),
            ("Detección híbrida", False),
        ]
    },
    {
        "enunciado": "¿Cuál de los métodos de detección es más efectivo ante un exploit de día cero?",
        "opciones": [
            ("Detección por firma", False),
            ("Detección por lista negra de IPs", False),
            ("Detección por política", False),
            ("Detección por anomalía", True),
        ]
    },
    {
        "enunciado": "¿Por qué la detección por anomalía genera más falsos positivos en una red universitaria que en una corporativa?",
        "opciones": [
            ("Porque las universidades tienen más ancho de banda y el IPS no puede procesarlo todo", False),
            ("Porque el tráfico universitario es muy variado e impredecible, dificultando establecer una línea base de comportamiento normal", True),
            ("Porque los estudiantes usan protocolos cifrados que el IPS no puede analizar", False),
            ("Porque las universidades no tienen presupuesto para hacer el tuning inicial correctamente", False),
        ]
    },
    {
        "enunciado": "¿En qué consiste el método de detección por política en un IPS?",
        "opciones": [
            ("Aprender el comportamiento normal del tráfico y alertar ante desviaciones", False),
            ("Definir explícitamente qué está permitido y bloquear todo lo que no cumple esas reglas", True),
            ("Comparar el tráfico con firmas de ataques conocidos en una base de datos", False),
            ("Combinar firma y anomalía para reducir falsos positivos y negativos", False),
        ]
    },
    {
        "enunciado": "Un IPS desplegado entre el router de borde e Internet, ¿cómo se denomina?",
        "opciones": [
            ("IPS de segmentación interna", False),
            ("IPS perimetral", True),
            ("IPS en modo TAP", False),
            ("HIPS perimetral", False),
        ]
    },
    {
        "enunciado": "¿Qué es un puerto SPAN y para qué se usa en el despliegue de un IDS?",
        "opciones": [
            ("Un puerto de alta velocidad reservado para tráfico de gestión del switch", False),
            ("Una configuración del switch que copia el tráfico de uno o varios puertos a un puerto de monitorización donde está conectado el IDS", True),
            ("Un puerto físico especial que permite al IDS bloquear tráfico en línea", False),
            ("Un enlace redundante entre switches para alta disponibilidad", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la diferencia entre un TAP de red y un puerto SPAN?",
        "opciones": [
            ("El TAP es software y el SPAN es hardware", False),
            ("El TAP copia el tráfico a nivel físico sin depender del switch, garantizando que no se pierden paquetes; el SPAN puede descartar paquetes si el switch está saturado", True),
            ("El SPAN puede capturar tráfico cifrado y el TAP no", False),
            ("No hay diferencia práctica entre ambos métodos", False),
        ]
    },
    {
        "enunciado": "¿En qué situación es preferible desplegar un IDS en lugar de un IPS?",
        "opciones": [
            ("Cuando la red tiene poco tráfico y es fácil definir políticas de bloqueo", False),
            ("Cuando se necesita bloqueo automático e inmediato de amenazas conocidas", False),
            ("Cuando no se puede asumir el riesgo de que un falso positivo corte tráfico legítimo crítico", True),
            ("Cuando el presupuesto no permite adquirir un IPS", False),
        ]
    },
    {
        "enunciado": "¿Qué es el despliegue en modo activo/pasivo con failover automático?",
        "opciones": [
            ("Dos IPS activos que procesan el tráfico simultáneamente repartiéndolo entre ambos", False),
            ("Un IPS principal que procesa todo el tráfico y un IPS secundario en espera que toma el relevo automáticamente si el principal falla", True),
            ("Un IPS que alterna entre modo IDS e IPS según la carga de tráfico", False),
            ("Dos IPS conectados en paralelo que se sincronizan cada 24 horas", False),
        ]
    },
    {
        "enunciado": "¿Qué es un bypass hardware en un IPS y cuándo es prioritario usarlo?",
        "opciones": [
            ("Un módulo que acelera el procesamiento de firmas mediante hardware dedicado", False),
            ("Un mecanismo físico que, si el IPS falla, permite que el tráfico fluya directamente sin inspección, manteniendo la conectividad", True),
            ("Una configuración que permite al IPS ignorar cierto tráfico para reducir la carga", False),
            ("Un puerto de gestión fuera de banda para administrar el IPS remotamente", False),
        ]
    },
    {
        "enunciado": "¿Qué es el tuning inicial de un IPS y por qué es necesario?",
        "opciones": [
            ("La actualización de firmas que se realiza tras la instalación del IPS", False),
            ("El proceso de ajuste de reglas tras un periodo de observación en modo IDS, para eliminar falsos positivos antes de activar el bloqueo", True),
            ("La configuración inicial de las interfaces de red del IPS", False),
            ("El proceso de integración del IPS con el SIEM corporativo", False),
        ]
    },
    {
        "enunciado": "¿Qué consecuencia tiene no realizar el tuning inicial correctamente en un IPS?",
        "opciones": [
            ("El IPS no puede actualizarse automáticamente con nuevas firmas", False),
            ("El IPS puede generar tantos falsos positivos que bloquee tráfico legítimo, o tantos falsos negativos que deje pasar ataques reales", True),
            ("El IPS pierde la capacidad de detectar ataques de día cero", False),
            ("El IPS no puede integrarse con Wireshark para análisis de tráfico", False),
        ]
    },
    {
        "enunciado": "¿Cuál es la principal ventaja de Suricata sobre Snort v2 en redes de alto tráfico?",
        "opciones": [
            ("Suricata soporta más protocolos de capa 2 que Snort", False),
            ("Suricata es multihilo de forma nativa y aprovecha todos los núcleos de CPU; Snort v2 es monohilo", True),
            ("Suricata incluye un SIEM integrado que Snort no tiene", False),
            ("Suricata puede actuar como IPS y Snort solo como IDS", False),
        ]
    },
    {
        "enunciado": "En una regla de Suricata, ¿qué parte define la acción a ejecutar cuando hay una coincidencia?",
        "opciones": [
            ("El campo msg entre comillas", False),
            ("El campo sid al final de la regla", False),
            ("La primera palabra de la regla: alert, drop, pass o reject", True),
            ("El campo classtype dentro de las opciones", False),
        ]
    },
    {
        "enunciado": "¿Qué es Emerging Threats (ET) en el contexto de Suricata?",
        "opciones": [
            ("Un tipo de ataque avanzado persistente que Suricata detecta de forma nativa", False),
            ("Un conjunto de reglas open-source mantenido por la comunidad, actualizado varias veces al día", True),
            ("Una herramienta de línea de comandos para gestionar Suricata", False),
            ("Un módulo de Suricata para detección de amenazas en tráfico cifrado", False),
        ]
    },
    {
        "enunciado": "¿Para qué se usa suricata-update?",
        "opciones": [
            ("Para actualizar el sistema operativo del servidor donde corre Suricata", False),
            ("Para gestionar y actualizar los conjuntos de reglas de Suricata desde fuentes como Emerging Threats", True),
            ("Para reiniciar el servicio de Suricata tras un cambio de configuración", False),
            ("Para exportar los logs de Suricata al SIEM en formato JSON", False),
        ]
    },
    {
        "enunciado": "¿Qué es un SIEM y cuál es su función principal?",
        "opciones": [
            ("Un sistema de prevención de intrusos de última generación con IA integrada", False),
            ("Un sistema que centraliza, normaliza y correlaciona eventos de seguridad de múltiples fuentes para detectar amenazas y generar alertas", True),
            ("Una herramienta de captura de tráfico avanzada que sustituye a Wireshark", False),
            ("Un firewall de aplicación con capacidad de aprendizaje automático", False),
        ]
    },
    {
        "enunciado": "¿Qué ventaja aporta el SIEM respecto a un IDS/IPS actuando de forma aislada?",
        "opciones": [
            ("El SIEM puede bloquear tráfico en tiempo real, algo que el IDS no puede hacer", False),
            ("El SIEM puede correlacionar eventos de múltiples fuentes distintas y detectar ataques que individualmente parecen inocentes", True),
            ("El SIEM analiza el tráfico a mayor velocidad que cualquier IDS/IPS", False),
            ("El SIEM elimina la necesidad de mantener reglas de firmas actualizadas", False),
        ]
    },
]

REDACCION = [
    {
        "titulo": "Métodos de detección IPS",
        "enunciado": (
            "Describe los cuatro métodos de detección de un IPS (firma, anomalía, política, híbrido). "
            "¿Cuál detectaría antes un exploit de día cero y por qué? "
            "Justifica por qué la detección por anomalía genera más falsos positivos en una red universitaria."
        ),
        "puntos": 15,
    },
    {
        "titulo": "IDS vs IPS: cuándo usar cada uno",
        "enunciado": (
            "¿En qué situaciones concretas es preferible un IDS en lugar de un IPS? ¿Y al revés? "
            "Da al menos dos situaciones para cada caso. "
            "¿Cuál recomendarías en un hospital con sistemas críticos de monitorización de pacientes?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "Tuning inicial y alta disponibilidad",
        "enunciado": (
            "Explica qué es el tuning inicial de un IPS, por qué es necesario y qué consecuencias "
            "tiene no realizarlo (falsos positivos y falsos negativos). "
            "¿Qué es el bypass hardware y por qué es importante en entornos críticos?"
        ),
        "puntos": 15,
    },
    {
        "titulo": "SIEM: componentes y correlación",
        "enunciado": (
            "¿Qué es un SIEM, cuáles son sus componentes principales y de qué fuentes recopila datos? "
            "Explica el pipeline típico de un SIEM y cómo complementa al IDS/IPS "
            "en la detección de ataques que usan múltiples vectores simultáneos."
        ),
        "puntos": 15,
    },
]
