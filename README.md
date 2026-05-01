# 14-paper-reproducibility-kit

Repositorio final del paper y punto de enlace entre el desarrollo del sistema,
los experimentos y el articulo cientifico.

## Objetivo

Este kit organiza los artefactos necesarios para que el paper sea reproducible:

- manuscrito LaTeX modularizado en `paper/`;
- protocolo experimental y definicion de metricas en `reproducibility/`;
- notebooks de analisis en `notebooks/`;
- resultados exportados en `results/`;
- material suplementario en `appendices/`.

## Estructura

```text
14-paper-reproducibility-kit/
├── README.md
├── AGENTS.md
├── paper/
│   ├── main.tex
│   ├── sections/
│   ├── figures/
│   ├── tables/
│   └── references.bib
├── reproducibility/
├── notebooks/
├── results/
└── appendices/
```

## Uso recomendado

1. Documentar cada experimento antes de ejecutarlo en
   `reproducibility/experiment-protocol.md`.
2. Guardar notebooks exploratorios o de analisis final en `notebooks/`.
3. Exportar metricas, tablas y figuras generadas a `results/`, `paper/tables/`
   y `paper/figures/`.
4. Actualizar las secciones del manuscrito en `paper/sections/`.
5. Mantener la checklist de artefactos al dia en
   `reproducibility/artifact-checklist.md`.

## Compilacion del paper

Desde la carpeta `paper/`, compilar con una distribucion LaTeX compatible:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```
