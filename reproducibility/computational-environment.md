# Computational Environment

## Python Environment

| Package | Version | Purpose |
|---------|---------|---------|
| Python | 3.11 | Runtime |
| numpy | >= 1.26 | Numerical computation |
| pandas | >= 2.1 | Data manipulation |
| matplotlib | >= 3.8 | Figure generation |
| seaborn | >= 0.13 | Statistical visualisation |
| scipy | >= 1.11 | Statistical tests |
| pyyaml | >= 6.0 | YAML parsing |
| pytest | >= 7.4 | Testing |
| jupyter | >= 1.0 | Notebook execution |

## LaTeX Environment

| Package | Version | Purpose |
|---------|---------|---------|
| TeX Live | 2023+ | LaTeX distribution |
| latexmk | >= 4.79 | Build automation |
| booktabs | — | Publication-quality tables |
| graphicx | — | Figure inclusion |
| hyperref | — | PDF links |

## Docker Image

```
FROM python:3.11-slim
+ texlive-latex-base
+ texlive-latex-extra
+ texlive-fonts-recommended
+ latexmk
```

See `Dockerfile` for the full specification.
