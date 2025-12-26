def heuristic_mapping(columns):
    mapping = {}

    for c in columns:
        cl = c.lower()
        if "date" in cl or "bill" in cl or "txn" in cl:
            mapping[c] = "date"
        elif "qty" in cl or "unit" in cl or "sold" in cl:
            mapping[c] = "units_sold"
        elif "sku" in cl or "item" in cl or "product" in cl:
            mapping[c] = "sku"

    confidence = len(set(mapping.values())) / 3
    return mapping, confidence
