# Medallion Architecture

This document outlines the medallion (raw/bronze/silver/gold) architecture used for data processing.

- Raw: raw ingested data, immutable
- Bronze: cleaned and parsed data
- Silver: enriched and deduplicated
- Gold: business-level aggregates and models

Use `src/pipeline.py` or `notebooks/dummy_pipeline.ipynb` to explore the flow.
