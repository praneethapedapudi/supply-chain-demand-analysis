from src.loaders.file_loader import load_file
from src.metadata.extractor import extract_metadata
from src.schema.heuristics import heuristic_mapping
from src.schema.llm_resolver import resolve_schema
from src.cleaning.standardize import standardize
from src.cleaning.validator import validate
from src.analytics.basic_analytics import compute_basic_metrics, top_products


def ingest(file, llm_client=None):
    df = load_file(file)
    metadata = extract_metadata(df)

    heuristic_map, confidence = heuristic_mapping(metadata["columns"])
    heuristic_map = {v: k for k, v in heuristic_map.items()}

    if confidence >= 0.8:
        # Use heuristic mapping directly, do not call LLM
        mapping = heuristic_map
    elif llm_client:
        # Attempt LLM schema inference, fall back to heuristic if it fails
        try:
            mapping = resolve_schema(metadata, llm_client)
        except (RuntimeError, Exception):
            # Fall back to heuristic mapping if LLM fails
            mapping = heuristic_map
    else:
        # No LLM client provided, use heuristic mapping
        mapping = heuristic_map

    df_clean = standardize(df, mapping)
    df_clean = validate(df_clean)

    metrics = compute_basic_metrics(df_clean)
    top_items = top_products(df_clean)

    return df_clean, metrics, top_items
