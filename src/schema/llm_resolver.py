import json

def resolve_schema(metadata, llm_client):
    prompt = f"""
You are a data engineer.

Your task:
Map input dataset columns to a canonical retail schema.

Canonical fields:
- date (required)
- sku (optional - only include if product/item identifier exists)
- units_sold OR sales_amount (required - choose whichever exists)

Rules:
- Return a JSON object
- Keys MUST be canonical fields
- Values MUST be exact input column names
- Do not invent columns
- If both quantity and sales exist, prefer units_sold
- SKU is optional - only include if a product/item identifier column exists
- Return JSON only

Metadata:
{json.dumps(metadata, indent=2)}
"""

    response = llm_client(prompt)

    try:
        mapping = json.loads(response)
    except json.JSONDecodeError:
        raise RuntimeError("LLM schema inference failed")

    # ---- VALIDATION (CRITICAL) ----
    if "date" not in mapping:
        raise RuntimeError("LLM schema inference failed")

    # SKU is optional - do not require it
    # if "sku" not in mapping:
    #     raise RuntimeError("LLM schema inference failed")

    if not any(k in mapping for k in ("units_sold", "sales_amount")):
        raise RuntimeError("LLM schema inference failed")

    return mapping
