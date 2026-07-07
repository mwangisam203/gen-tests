from learning_lab.tree_nodes import Node, count_nodes, leaf_names


def test_count_nodes_includes_descendants():
    root = Node("root", [Node("left"), Node("right", [Node("leaf")])])

    assert count_nodes(root) == 4


def test_leaf_names_returns_terminal_nodes():
    root = Node("root", [Node("left"), Node("right", [Node("leaf")])])

    assert leaf_names(root) == ["left", "leaf"]
