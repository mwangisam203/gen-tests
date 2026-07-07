"""Tree node practice helpers."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Node:
    name: str
    children: list["Node"] = field(default_factory=list)


def count_nodes(node: Node) -> int:
    """Count a node and all descendants."""
    return 1 + sum(count_nodes(child) for child in node.children)


def leaf_names(node: Node) -> list[str]:
    """Return names of nodes with no children."""
    if not node.children:
        return [node.name]
    return [name for child in node.children for name in leaf_names(child)]
