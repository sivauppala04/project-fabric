# Fabric Medallion Project

This repository contains a medallion (raw/bronze/silver/gold) project scaffold for a Fabric data pipeline.

Structure:

- data/
  - raw/           # Ingested raw files
  - bronze/        # Cleaned / parsed data
  - silver/        # Enriched / deduplicated data
  - gold/          # Business-ready aggregated datasets
- notebooks/       # Example and exploratory notebooks
- src/             # Pipeline and helpers
- docs/            # Architecture and design notes

See `notebooks/dummy_pipeline.ipynb` for a minimal runnable notebook pipeline.

License: Unspecified
