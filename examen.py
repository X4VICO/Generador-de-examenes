#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
examen.py — Runner principal del simulacro de examen
=====================================================
Carga automáticamente todos los archivos de temas desde la carpeta /temas.

Para añadir un tema nuevo:
  1. Crea un archivo en temas/  (ej: tema4_routing.py)
  2. Define en él las variables TEMA, TEST y REDACCION con el formato indicado
  3. Listo — el runner lo detectará solo en el próximo arranque

Formato esperado en cada archivo de tema:

    TEMA = {
        "id":         4,           # número único del tema
        "nombre":     "Routing",   # nombre que aparece en el menú
        "asignatura": "Redes III", # agrupación (para futuros filtros)
    }

    TEST = [
        {
            "enunciado": "texto de la pregunta",
            "opciones": [
                ("texto opción A", False),
                ("texto opción B", True),   ← True = correcta (solo una)
                ("texto opción C", False),
                ("texto opción D", False),
            ]
        },
        ...
    ]

    REDACCION = [
        {
            "titulo":   "Título corto",
            "enunciado": "Enunciado completo de la pregunta.",
            "puntos":   15,
        },
        ...
    ]
"""

import os
import sys
import importlib.util
import random
import textwrap
from datetime import datetime

# ─────────────────────────────────────────────
#  COLORES ANSI
# ─────────────────────────────────────────────
V  = "\033[92m"   # verde
R  = "\033[91m"   # rojo
AM = "\033[93m"   # amarillo
CY = "\033[96m"   # cyan
BL = "\033[97m"   # blanco
N  = "\033[1m"    # negrita
GR = "\033[90m"   # gris
RE = "\033[0m"    # reset

# ─────────────────────────────────────────────
#  CARGA DINÁMICA DE TEMAS
# ─────────────────────────────────────────────

def cargar_temas():
    """
    Escanea la carpeta temas/ y carga todos los archivos .py
    que definan las variables TEMA, TEST y REDACCION.
    Devuelve una lista de dicts ordenada por tema["id"].
    """
    carpeta = os.path.join(os.path.dirname(__file__), "temas")
    temas_cargados = []

    for archivo in sorted(os.listdir(carpeta)):
        if not archivo.endswith(".py") or archivo.startswith("_"):
            continue

        ruta = os.path.join(carpeta, archivo)
        spec = importlib.util.spec_from_file_location(archivo[:-3], ruta)
        modulo = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(modulo)
        except Exception as e:
            print(f"{R}Error cargando {archivo}: {e}{RE}")
            continue

        # Validar que el archivo tiene las variables necesarias
        if not all(hasattr(modulo, attr) for attr in ("TEMA", "TEST", "REDACCION")):
            print(f"{AM}Aviso: {archivo} ignorado (faltan TEMA, TEST o REDACCION){RE}")
            continue

        # Validar que cada pregunta test tiene exactamente 1 correcta
        errores = _validar_test(modulo.TEST, archivo)
        if errores:
            for e in errores:
                print(f"{R}{e}{RE}")
            continue

        temas_cargados.append({
            "meta":      modulo.TEMA,
            "test":      modulo.TEST,
            "redaccion": modulo.REDACCION,
            "archivo":   archivo,
        })

    temas_cargados.sort(key=lambda t: t["meta"].get("id", 0))
    return temas_cargados

def _validar_test(preguntas, archivo):
    errores = []
    for i, p in enumerate(preguntas):
        correctas = sum(1 for _, c in p.get("opciones", []) if c)
        if correctas != 1:
            errores.append(f"  [{archivo}] Pregunta {i+1}: tiene {correctas} respuestas correctas (debe ser 1)")
    return errores

# ─────────────────────────────────────────────
#  UTILIDADES DE TERMINAL
# ─────────────────────────────────────────────

def limpiar():
    os.system("clear" if os.name != "nt" else "cls")

def wrap(texto, ancho=70):
    return textwrap.fill(str(texto), width=ancho)

def titulo(texto):
    linea = "═" * 62
    print(f"\n{CY}{N}{linea}{RE}")
    print(f"{CY}{N}  {texto}{RE}")
    print(f"{CY}{N}{linea}{RE}\n")

def separador():
    print(f"{GR}{'─' * 62}{RE}")

def pedir_int(prompt, minimo, maximo):
    while True:
        try:
            valor = int(input(prompt).strip())
            if minimo <= valor <= maximo:
                return valor
            print(f"{R}Introduce un número entre {minimo} y {maximo}.{RE}")
        except ValueError:
            print(f"{R}Por favor introduce un número.{RE}")

def leer_multilinea():
    """Lee texto libre hasta que el usuario escribe '---' solo en una línea."""
    print(f"{GR}(Escribe tu respuesta. Cuando termines escribe '---' en una línea nueva){RE}\n")
    lineas = []
    while True:
        try:
            linea = input()
            if linea.strip() == "---":
                break
            lineas.append(linea)
        except EOFError:
            break
    return "\n".join(lineas)

# ─────────────────────────────────────────────
#  MENÚS DE CONFIGURACIÓN
# ─────────────────────────────────────────────

def menu_temas(temas_disponibles):
    """Permite al usuario elegir qué temas incluir en el examen."""
    titulo("Selección de temas")

    for t in temas_disponibles:
        meta = t["meta"]
        print(f"  {CY}{meta['id']}{RE}  {meta['nombre']}"
              f"  {GR}({len(t['test'])} test · {len(t['redaccion'])} redacción){RE}")

    ids = [str(t["meta"]["id"]) for t in temas_disponibles]
    print(f"\n  {CY}0{RE}  Todos los temas")
    print()

    while True:
        entrada = input(
            f"{AM}Elige tema(s) separados por coma, o 0 para todos "
            f"(ej: 1,3): {RE}"
        ).strip()

        if entrada == "0":
            return temas_disponibles

        seleccionados_ids = {x.strip() for x in entrada.split(",")}
        if seleccionados_ids.issubset(set(ids)):
            return [t for t in temas_disponibles
                    if str(t["meta"]["id"]) in seleccionados_ids]

        print(f"{R}IDs no válidos. Usa los números del menú.{RE}")

def menu_cantidad(temas_sel):
    """Pregunta cuántas preguntas de cada tipo quiere el usuario."""
    total_test = sum(len(t["test"]) for t in temas_sel)
    total_red  = sum(len(t["redaccion"]) for t in temas_sel)

    limpiar()
    titulo("Cantidad de preguntas")
    print(f"  Preguntas test disponibles:      {BL}{total_test}{RE}")
    print(f"  Preguntas redacción disponibles: {BL}{total_red}{RE}\n")

    num_test = pedir_int(
        f"{AM}¿Cuántas preguntas tipo test? (0-{total_test}): {RE}",
        0, total_test
    )
    num_red = pedir_int(
        f"{AM}¿Cuántas preguntas de redacción? (0-{total_red}): {RE}",
        0, total_red
    )

    if num_test == 0 and num_red == 0:
        print(f"{R}No has seleccionado ninguna pregunta. Saliendo.{RE}")
        sys.exit(0)

    return num_test, num_red

# ─────────────────────────────────────────────
#  LÓGICA DEL EXAMEN
# ─────────────────────────────────────────────

def hacer_test(preguntas, pts_por_pregunta):
    resultados = []
    total = len(preguntas)
    letras = ["a", "b", "c", "d"]

    for i, preg in enumerate(preguntas, 1):
        limpiar()
        titulo(f"TIPO TEST  —  {i} / {total}  [{preg['_tema_nombre']}]")

        print(f"{BL}{N}{wrap(preg['enunciado'])}{RE}\n")
        separador()

        # Mezclar opciones aleatoriamente
        opciones = list(preg["opciones"])
        random.shuffle(opciones)

        for j, (texto, _) in enumerate(opciones):
            print(f"  {CY}{letras[j]}{RE}) {wrap(texto, 66)}")

        print()
        while True:
            resp = input(f"{AM}Tu respuesta ({'/'.join(letras[:len(opciones)])}): {RE}").strip().lower()
            if resp in letras[:len(opciones)]:
                break
            print(f"{R}Opción no válida.{RE}")

        idx = letras.index(resp)
        texto_elegido, es_correcta = opciones[idx]
        correcta_texto = next(t for t, c in opciones if c)
        correcta_letra = letras[[t for t, c in opciones].index(correcta_texto)]

        if es_correcta:
            print(f"\n{V}{N}✓  Correcto{RE}  (+{pts_por_pregunta:.1f} pts)")
        else:
            print(f"\n{R}{N}✗  Incorrecto{RE}")
            print(f"   Correcta → {V}{correcta_letra}) {correcta_texto}{RE}")

        resultados.append({
            "tema":              preg["_tema_nombre"],
            "enunciado":         preg["enunciado"],
            "correcta":          es_correcta,
            "tu_respuesta":      texto_elegido,
            "respuesta_correcta": correcta_texto,
            "pts":               pts_por_pregunta if es_correcta else 0,
        })

        input(f"\n{GR}Pulsa Enter para continuar...{RE}")

    return resultados

def hacer_redaccion(preguntas):
    respuestas = []
    total = len(preguntas)

    for i, preg in enumerate(preguntas, 1):
        limpiar()
        titulo(f"REDACCIÓN  —  {i} / {total}  [{preg['_tema_nombre']}]")
        print(f"{N}{BL}{preg['titulo']}{RE}  {GR}({preg['puntos']} puntos){RE}\n")
        separador()
        print(f"{wrap(preg['enunciado'], 70)}\n")
        separador()
        print()

        texto = leer_multilinea()

        respuestas.append({
            "tema":       preg["_tema_nombre"],
            "titulo":     preg["titulo"],
            "enunciado":  preg["enunciado"],
            "puntos_max": preg["puntos"],
            "respuesta":  texto,
        })

        print(f"\n{V}✓  Respuesta guardada.{RE}")
        input(f"{GR}Pulsa Enter para continuar...{RE}")

    return respuestas

# ─────────────────────────────────────────────
#  RESULTADO FINAL
# ─────────────────────────────────────────────

def mostrar_resultado(resultados_test, respuestas_red, pts_test_max):
    limpiar()
    titulo("RESULTADO DEL EXAMEN")

    # ── Test ──
    correctas  = sum(1 for r in resultados_test if r["correcta"])
    total_test = len(resultados_test)
    pts_test   = sum(r["pts"] for r in resultados_test)

    if total_test > 0:
        print(f"{N}PARTE A — TIPO TEST{RE}")
        print(f"  Correctas : {V}{correctas}{RE} / {total_test}")
        print(f"  Puntos    : {V}{pts_test:.1f}{RE} / {pts_test_max:.1f}")
        separador()

        errores = [r for r in resultados_test if not r["correcta"]]
        if errores:
            print(f"\n{R}Preguntas falladas:{RE}")
            for e in errores:
                print(f"\n  {GR}[{e['tema']}]{RE} {wrap(e['enunciado'], 64)}")
                print(f"    Tu respuesta : {R}{e['tu_respuesta']}{RE}")
                print(f"    Correcta     : {V}{e['respuesta_correcta']}{RE}")
        else:
            print(f"\n{V}¡Todas las preguntas test correctas!{RE}")
        separador()

    # ── Redacción ──
    if respuestas_red:
        pts_red_max = sum(r["puntos_max"] for r in respuestas_red)
        print(f"\n{N}PARTE B — REDACCIÓN{RE}")
        print(f"  {AM}⚠  Pendiente de corrección manual  ({pts_red_max} puntos posibles){RE}\n")

        bloque = _generar_bloque(respuestas_red)
        separador()
        print(bloque)
        separador()

        print(f"\n{AM}Nota parcial (solo test) : {pts_test:.1f} / {pts_test_max:.1f}{RE}")
        print(f"{AM}Nota final = nota test + corrección de redacción{RE}")

    else:
        total_max = pts_test_max
        pct = (pts_test / total_max * 100) if total_max > 0 else 0
        color = V if pct >= 50 else R
        print(f"\n{N}NOTA FINAL: {color}{pts_test:.1f} / {total_max:.1f}  ({pct:.0f}%){RE}")

    print()

def _generar_bloque(respuestas):
    """Genera el bloque de texto para pegar al corrector."""
    sep = "=" * 62
    lineas = [
        sep,
        "BLOQUE PARA CORRECCIÓN — REDACCIÓN",
        f"Generado: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        sep,
    ]
    for i, r in enumerate(respuestas, 1):
        lineas += [
            f"\n[PREGUNTA {i} — {r['tema']} — {r['puntos_max']} puntos]",
            f"Título   : {r['titulo']}",
            f"Enunciado: {r['enunciado']}",
            f"\nRespuesta del alumno:\n{r['respuesta']}",
            "\n" + "─" * 62,
        ]
    lineas += [
        "\nPuntúa cada pregunta sobre su máximo.",
        "Nota global = puntuación test ya calculada + suma de redacción.",
    ]
    return "\n".join(lineas)

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

def main():
    limpiar()
    titulo("Simulacro de Examen — Runner Universal")

    # 1. Cargar temas
    temas = cargar_temas()
    if not temas:
        print(f"{R}No se encontraron temas en la carpeta /temas. Saliendo.{RE}")
        sys.exit(1)

    asignaturas = {t["meta"].get("asignatura", "Sin asignatura") for t in temas}
    print(f"  Asignatura(s) : {BL}{', '.join(sorted(asignaturas))}{RE}")
    print(f"  Temas cargados: {BL}{len(temas)}{RE}")
    print(f"  Total preguntas test     : {BL}{sum(len(t['test']) for t in temas)}{RE}")
    print(f"  Total preguntas redacción: {BL}{sum(len(t['redaccion']) for t in temas)}{RE}\n")
    input(f"{AM}Pulsa Enter para configurar el examen...{RE}")

    # 2. Selección de temas
    limpiar()
    temas_sel = menu_temas(temas)

    # 3. Cantidad de preguntas
    num_test, num_red = menu_cantidad(temas_sel)

    # 4. Calcular puntos
    pts_red_total  = num_red * 15
    pts_test_total = 100 - pts_red_total
    pts_por_preg   = (pts_test_total / num_test) if num_test > 0 else 0

    # 5. Resumen antes de empezar
    limpiar()
    titulo("Resumen del examen")
    nombres = ", ".join(t["meta"]["nombre"] for t in temas_sel)
    print(f"  Temas        : {BL}{nombres}{RE}")
    print(f"  Test         : {BL}{num_test} preguntas{RE}  ({pts_por_preg:.1f} pts cada una)")
    print(f"  Redacción    : {BL}{num_red} preguntas{RE}  (15 pts cada una)")
    print(f"  Total puntos : {BL}{num_test * pts_por_preg + num_red * 15:.0f}{RE}\n")
    input(f"{AM}Pulsa Enter para empezar...{RE}")

    # 6. Construir pool de preguntas (aplanado con metadato de tema)
    pool_test = []
    for t in temas_sel:
        for p in t["test"]:
            pool_test.append({**p, "_tema_nombre": t["meta"]["nombre"]})

    pool_red = []
    for t in temas_sel:
        for p in t["redaccion"]:
            pool_red.append({**p, "_tema_nombre": t["meta"]["nombre"]})

    preguntas_test_sel = random.sample(pool_test, num_test)
    preguntas_red_sel  = random.sample(pool_red,  num_red)

    # 7. Ejecutar examen
    resultados_test = hacer_test(preguntas_test_sel, pts_por_preg) if num_test > 0 else []
    respuestas_red  = hacer_redaccion(preguntas_red_sel)            if num_red  > 0 else []

    # 8. Resultado
    mostrar_resultado(resultados_test, respuestas_red, num_test * pts_por_preg)

if __name__ == "__main__":
    main()
