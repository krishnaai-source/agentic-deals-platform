import json
from agentic_ai.src.db.mongo_client import _db  # adjust import if needed

def load_collection(name, path):
    with open(path, "r") as f:
        docs = json.load(f)
    col = _db[name]
    col.delete_many({})
    col.insert_many(docs)
    print(f"Seeded {name} with {len(docs)} docs")

if __name__ == "__main__":
    base = "data/nosql"
    load_collection("skus", f"{base}/skus.json")
    load_collection("inventory", f"{base}/inventory.json")
    load_collection("pricing", f"{base}/pricing.json")
    load_collection("region_config", f"{base}/region_config.json")
