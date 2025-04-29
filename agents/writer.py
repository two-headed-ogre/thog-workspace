"""Writer - Knowledge Writer Agent (Stub)"""

import json
import time
from pathlib import Path
from typing import List, Dict, Any

GRAPH_PATH = Path("graphs/world_model.graphml")
MEMORY_DIR = Path("memory")
MEMORY_DIR.mkdir(exist_ok=True)


def _get_next_node_id() -> str:
    """Return a unique node id based on timestamp."""
    return f"c{int(time.time() * 1000)}"


def _append_graphml_nodes(validated: List[Dict[str, Any]]):
    # Read existing content
    graphml = GRAPH_PATH.read_text(encoding="utf-8")

    # Build nodes to insert
    nodes_xml = "\n".join(
        f'    <node id="{_get_next_node_id()}" label="{item["claim"]}"/>'
        for item in validated
    )

    # Insert before closing tag
    updated = graphml.replace("</graph>", f"{nodes_xml}\n  </graph>")
    GRAPH_PATH.write_text(updated, encoding="utf-8")


def write(validated: List[Dict[str, Any]]):
    """Write validated claims to memory JSON and GraphML."""
    timestamp = int(time.time())
    json_path = MEMORY_DIR / f"claims_{timestamp}.json"

    print(f"[writer] writing {len(validated)} claims -> {json_path}")
    json_path.write_text(json.dumps(validated, indent=2), encoding="utf-8")

    print("[writer] appending claims to world model graphml")
    _append_graphml_nodes(validated)
