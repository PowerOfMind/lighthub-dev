#!/usr/bin/env python3
"""Crea una página nueva (ES y EN) a partir de una plantilla de plantillas/.

Uso:
  python tools/nueva_pagina.py <seccion> <slug> [--tipo guia|error] [--titulo "Título"] [--solo-es]

Ejemplos:
  python tools/nueva_pagina.py react-native notificaciones-locales --tipo guia
  python tools/nueva_pagina.py react hydration-error --tipo error --titulo "Hydration failed"

Usa el siguiente número libre de la carpeta (01, 02, ...). Si la sección no existe, la crea,
pero recuerda registrarla en build.py (ver plantillas/LEEME.md).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def siguiente_numero(carpeta):
    numeros = [int(m.group(1)) for f in carpeta.glob("*.md") if (m := re.match(r"(\d+)-", f.name))]
    return max(numeros, default=0) + 1


def crear(carpeta, slug, plantilla, titulo):
    carpeta.mkdir(parents=True, exist_ok=True)
    destino = carpeta / f"{siguiente_numero(carpeta):02d}-{slug}.md"
    texto = plantilla
    if titulo:
        texto = re.sub(r"^title:.*$", f"title: {titulo}", texto, count=1, flags=re.M)
    destino.write_text(texto, encoding="utf-8", newline="\n")
    return destino


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seccion")
    ap.add_argument("slug", help="nombre del fichero sin número ni .md (minúsculas y guiones)")
    ap.add_argument("--tipo", choices=["guia", "error"], default="guia")
    ap.add_argument("--titulo")
    ap.add_argument("--solo-es", action="store_true", help="no crear la versión EN")
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        sys.exit("El slug solo admite minúsculas, números y guiones.")
    plantilla = (ROOT / "plantillas" / f"{a.tipo}.md").read_text(encoding="utf-8")
    creados = [crear(ROOT / "content" / a.seccion, a.slug, plantilla, a.titulo)]
    if not a.solo_es:
        creados.append(crear(ROOT / "content" / "en" / a.seccion, a.slug, plantilla, a.titulo))
    for c in creados:
        print("Creado", c.relative_to(ROOT))
    print("Rellena los TODO y ejecuta: python tools/validar.py")


if __name__ == "__main__":
    main()
