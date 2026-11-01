#!/usr/bin/env python3
"""Revisa que todas las páginas de content/ cumplan las reglas del sitio.

Uso: python tools/validar.py        (sale con código 1 si hay errores)

Comprueba: cabecera con title y desc, desc de 120-155 caracteres y única, sin BOM, sin TODO
sin rellenar, === esquema y === test (con respuesta marcada con * en cada pregunta),
pareja ES/EN con el mismo nombre de fichero y enlaces internos (@/seccion/slug) existentes.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SIN_TEST = {"privacidad.md"}


def paginas():
    return sorted(CONTENT.rglob("*.md"))


def idioma(p):
    return "en" if p.relative_to(CONTENT).parts[0] == "en" else "es"


def clave(p):
    partes = list(p.relative_to(CONTENT).parts)
    if partes[0] == "en":
        partes = partes[1:]
    return "/".join(partes)


def main():
    errores = []
    descs = {}
    slugs = set()
    for p in paginas():
        r = p.relative_to(ROOT).as_posix()
        if idioma(p) == "es":
            slugs.add("/".join(clave(p).split("/")[:-1] + [re.sub(r"^\d+-", "", p.stem)]))
    for p in paginas():
        r = p.relative_to(ROOT).as_posix()
        raw = p.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            errores.append(f"{r}: tiene BOM (guárdalo como UTF-8 sin BOM)")
        t = raw.decode("utf-8-sig").replace(chr(13) + chr(10), chr(10))
        m = re.match(r"---\n(.*?)\n---\n", t, re.S)
        if not m:
            errores.append(f"{r}: falta la cabecera --- ... ---")
            continue
        meta = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
        if not meta.get("title"):
            errores.append(f"{r}: falta title")
        d = meta.get("desc", "").strip()
        if not 120 <= len(d) <= 155:
            errores.append(f"{r}: desc de {len(d)} caracteres (debe estar entre 120 y 155)")
        if d in descs:
            errores.append(f"{r}: desc repetida de {descs[d]}")
        descs[d] = r
        if "TODO" in re.sub(r"```.*?```", "", t, flags=re.S):
            errores.append(f"{r}: quedan TODO sin rellenar")
        if p.name not in SIN_TEST:
            if "=== esquema" not in t:
                errores.append(f"{r}: falta === esquema")
            test = t.split("=== test", 1)
            if len(test) < 2:
                errores.append(f"{r}: falta === test")
            else:
                cuerpo = re.split(r"^=== ", test[1], flags=re.M)[0]
                preguntas = re.split(r"^\? ", cuerpo, flags=re.M)[1:]
                if len(preguntas) < 3:
                    errores.append(f"{r}: el test tiene {len(preguntas)} preguntas (mínimo 3)")
                for q in preguntas:
                    if len(re.findall(r"^\* ", q, re.M)) != 1:
                        errores.append(f"{r}: cada pregunta necesita exactamente una respuesta con * ({q.splitlines()[0][:40]})")
        if "=== prueba" in t and not re.search(r"^## ", t.split("=== prueba", 1)[1], re.M):
            errores.append(f"{r}: === prueba necesita cada ejemplo bajo un título ## ")
        for destino in re.findall(r"\(@/([^)]+)\)", t):
            if destino.strip("/") not in slugs and not destino.endswith("/"):
                errores.append(f"{r}: enlace interno roto (@/{destino})")
    es = {clave(p) for p in paginas() if idioma(p) == "es"}
    en = {clave(p) for p in paginas() if idioma(p) == "en"}
    for f in sorted(es - en):
        errores.append(f"content/{f}: falta la versión EN")
    for f in sorted(en - es):
        errores.append(f"content/en/{f}: falta la versión ES")
    for e in errores:
        print("ERROR", e)
    print(f"{len(paginas())} páginas revisadas, {len(errores)} errores")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
