import pathlib

from anytree import Node

with open(pathlib.Path(__file__).parent / "example.txt") as inf:
    notes = inf.read()

notes_as_dict = {
    name: children.split(",")
    for name, children in map(lambda node: node.split(":"), notes.split("\n"))
}

nodes: dict[str, Node] = {}

for parent_name, children in notes_as_dict.items():
    nodes[parent_name] = nodes.get(parent_name) or Node(parent_name)
    for child_name in children:

        if child_name != "@":
            nodes[child_name] = nodes.get(child_name) or Node(child_name)
            child = nodes[child_name]
        else:
            child = Node(child_name)

        child.parent = nodes[parent_name]

root = nodes["RR"]
depths = {}

for leaf in root.leaves:
    depth = leaf.depth
    if leaf.name == "@":
        depths[leaf.depth] = depths.get(leaf.depth, []) + [leaf]

target = min(depths.values(), key=len)[0]

print("".join(n.name[0] for n in target.path))
