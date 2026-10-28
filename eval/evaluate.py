"""Retrieval evaluation (run from project root).
  python -m eval.evaluate gen --collection biomed --n 40   # synthetic test set
  python -m eval.evaluate run --collection biomed          # Hit@k and MRR
Hand-review eval/testset.json: synthetic questions skew easy.
"""
import argparse
import json
import random
from pathlib import Path

from app.ingest import get_store
from app.rag import _text, llm, retrieve

TESTSET = Path("eval/testset.json")
GEN_PROMPT = ("Write ONE specific question that can be answered using only this passage. "
              "Do not mention 'the passage' or 'the text'. Return only the question.\n\n{c}")


def gen(collection, n):
    data = get_store(collection).get(include=["documents", "metadatas"])
    items = [(d, m) for d, m in zip(data["documents"], data["metadatas"]) if len(d) > 300]
    random.seed(42)
    rows = []
    for doc, meta in random.sample(items, min(n, len(items))):
        q = _text(llm.invoke(GEN_PROMPT.format(c=doc))).strip()
        rows.append({"question": q, "source": meta["source"], "page": meta["page"]})
    TESTSET.write_text(json.dumps(rows, indent=2))
    print(f"Wrote {len(rows)} questions to {TESTSET}")


def run(collection, ks=(1, 3, 5)):
    rows = json.loads(TESTSET.read_text())
    hits = {k: 0 for k in ks}
    rr = 0.0
    for r in rows:
        res = retrieve(r["question"], collection, k=max(ks))
        rank = next((i + 1 for i, (d, _) in enumerate(res)
                     if d.metadata["source"] == r["source"] and d.metadata["page"] == r["page"]), None)
        if rank:
            rr += 1 / rank
            for k in ks:
                hits[k] += rank <= k
    n = len(rows)
    print(f"Questions: {n}")
    for k in ks:
        print(f"Hit@{k}: {hits[k] / n:.1%}")
    print(f"MRR: {rr / n:.3f}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["gen", "run"])
    p.add_argument("--collection", default="default")
    p.add_argument("--n", type=int, default=40)
    a = p.parse_args()
    gen(a.collection, a.n) if a.cmd == "gen" else run(a.collection)
