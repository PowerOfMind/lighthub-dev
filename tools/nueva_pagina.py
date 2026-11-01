#!/usr/bin/env python3
"""Crea una página nueva (ES y EN) a partir de una plantilla de plantillas/.

Uso:
  python tools/nueva_pagina.py <seccion> <slug> [--tipo guia|error] [--titulo "Título"] [--solo-es]

Ejemplos:
  python tools/nueva_pagina.py react-native notificaciones-locales --tipo guia
  python tools/nueva_pagina.py react hydration-error --tipo error --titulo "Hydration failed"

Usa el siguiente número libre de la carpeta en español y el mismo para la versión EN. Si la
sección no existe, crea la carpeta, pero recuerda registrarla en build.py (ver plantillas/LEEME.md).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def siguiente_numero(*carpetas):
    numeros = [int(m.group(1)) for c in carpetas for f in c.glob("*.md") if (m := re.match(r"(\d+)-", f.name))]
    return max(numeros, default=0) + 1


def plantilla(tipo, idioma):
    sufijo = ".en" if idioma == "en" else ""
    return (ROOT / "plantillas" / f"{tipo}{sufijo}.md").read_text(encoding="utf-8")


def crear(carpeta, nombre, texto, titulo):
    carpeta.mkdir(parents=True, exist_ok=True)
    destino = carpeta / nombre
    if destino.exists():
        sys.exit(f"{destino.relative_to(ROOT)} ya existe")
    if titulo:
        texto = re.sub(r"^title:.*$", lambda _: f"title: {titulo}", texto, count=1, flags=re.M)
    destino.write_text(texto, encoding="utf-8", newline="\n")
    return destino


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seccion", help="carpeta de content/ (minúsculas y guiones)")
    ap.add_argument("slug", help="nombre del fichero sin número ni .md (minúsculas y guiones)")
    ap.add_argument("--tipo", choices=["guia", "error"], default="guia")
    ap.add_argument("--titulo")
    ap.add_argument("--solo-es", action="store_true", help="no crear la versión EN")
    a = ap.parse_args()
    for valor in (a.seccion, a.slug):
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", valor):
            sys.exit(f"«{valor}» solo admite minúsculas, números y guiones.")
    es, en = ROOT / "content" / a.seccion, ROOT / "content" / "en" / a.seccion
    nombre = f"{siguiente_numero(es, en):02d}-{a.slug}.md"
    creados = [crear(es, nombre, plantilla(a.tipo, "es"), a.titulo)]
    if not a.solo_es:
        creados.append(crear(en, nombre, plantilla(a.tipo, "en"), a.titulo))
    for c in creados:
        print("Creado", c.relative_to(ROOT))
    print("Rellena los TODO y ejecuta: python tools/validar.py")


if __name__ == "__main__":
    main()
