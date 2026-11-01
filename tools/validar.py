#!/usr/bin/env python3
"""Revisa que todas las páginas de content/ cumplan las reglas del sitio.

Uso: python tools/validar.py        (sale con código 1 si hay errores)

Reutiliza el parseo de build.py (cabecera y secciones) y añade lo que el build no exige:
desc de 120-155 caracteres y única, sin BOM, sin TODO sin rellenar, esquema y test (mínimo 3
preguntas), cada ejemplo de === prueba bajo un título, y pareja ES/EN con el mismo nombre.
Que haya exactamente una respuesta marcada con * y que los enlaces internos existan lo
comprueba build.py y hace fallar el build.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build  # noqa: E402

CONTENT = ROOT / "content"
SIN_TEST = {"privacidad.md"}


def clave(p):
    partes = list(p.relative_to(CONTENT).parts)
    return "/".join(partes[1:] if partes[0] == "en" else partes)


def idioma(p):
    return "en" if p.relative_to(CONTENT).parts[0] == "en" else "es"


def revisar(p, descs):
    r = p.relative_to(ROOT).as_posix()
    errores = []
    if p.read_bytes().startswith(b"\xef\xbb\xbf"):
        errores.append(f"{r}: tiene BOM (guárdalo como UTF-8 sin BOM)")
    meta, body = build.parse(p)
    if not meta.get("title"):
        errores.append(f"{r}: falta title")
    desc = meta.get("desc", "")
    if not 120 <= len(desc) <= 155:
        errores.append(f"{r}: desc de {len(desc)} caracteres (debe estar entre 120 y 155)")
    if desc in descs:
        errores.append(f"{r}: desc repetida de {descs[desc]}")
    descs[desc] = r
    if "TODO" in re.sub(r"```.*?```", "", body, flags=re.S):
        errores.append(f"{r}: quedan TODO sin rellenar")
    if p.name in SIN_TEST:
        return errores
    sec = build.split_sections(body)
    if "esquema" not in sec:
        errores.append(f"{r}: falta === esquema")
    if "test" not in sec:
        errores.append(f"{r}: falta === test")
    elif len(re.findall(r"^\? ", sec["test"], re.M)) < 3:
        errores.append(f"{r}: el test necesita al menos 3 preguntas")
    if "prueba" in sec and not re.search(r"^## ", sec["prueba"], re.M):
        errores.append(f"{r}: === prueba necesita cada ejemplo bajo un título ##")
    return errores


def main():
    paginas = sorted(CONTENT.rglob("*.md"))
    errores, descs = [], {}
    for p in paginas:
        errores += revisar(p, descs)
    es = {clave(p) for p in paginas if idioma(p) == "es"}
    en = {clave(p) for p in paginas if idioma(p) == "en"}
    errores += [f"content/{f}: falta la versión EN" for f in sorted(es - en)]
    errores += [f"content/en/{f}: falta la versión ES" for f in sorted(en - es)]
    for e in errores:
        print("ERROR", e)
    print(f"{len(paginas)} páginas revisadas, {len(errores)} errores")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
