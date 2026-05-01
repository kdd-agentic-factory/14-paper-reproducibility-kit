# AGENTS.md

Guia operativa para agentes y colaboradores que trabajen en este repositorio.

## Proposito del repositorio

Este repositorio es el paquete final de reproducibilidad del articulo. Su tarea
principal es conectar el manuscrito con los artefactos ejecutables, los
protocolos experimentales, las metricas y los resultados reportados.

## Reglas de trabajo

- Mantener la estructura del repositorio estable.
- No sobrescribir resultados sin conservar trazabilidad de fecha, version o
  configuracion experimental.
- Registrar cambios metodologicos en `reproducibility/experiment-protocol.md`.
- Definir o actualizar metricas en `reproducibility/metrics-definition.md`
  antes de reportarlas en el paper.
- Las figuras finales deben vivir en `paper/figures/`.
- Las tablas finales deben vivir en `paper/tables/`.
- Los artefactos suplementarios extensos deben vivir en `appendices/`.

## Convenciones

- Usar nombres descriptivos y ordenables para resultados:
  `YYYY-MM-DD_experiment-name_metric.csv`.
- Incluir semillas, versiones de dependencias y configuracion de hardware cuando
  afecten a la reproducibilidad.
- Mantener notebooks limpios, ejecutables de arriba abajo y con salidas
  relevantes.

## Antes de cerrar una contribucion

- Verificar que el paper compila.
- Verificar que las rutas citadas desde el manuscrito existen.
- Actualizar la checklist de artefactos.
- Documentar cualquier limitacion conocida.
