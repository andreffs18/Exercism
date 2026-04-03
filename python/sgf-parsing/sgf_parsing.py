class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True


def parse(input_string):
    s = input_string.strip()

    if not s:
        raise ValueError("tree missing")
    if not s.startswith("(") or not s.endswith(")"):
        raise ValueError("tree missing")

    tree, pos = _parse_tree(s, 0)
    return tree


def _parse_tree(s, pos):
    if pos >= len(s) or s[pos] != "(":
        raise ValueError("tree missing")

    pos += 1  # skip '('

    if pos >= len(s) or s[pos] != ";":
        raise ValueError("tree with no nodes")

    nodes = []

    # Parse all nodes and sub-trees
    while pos < len(s) and s[pos] != ")":
        if s[pos] == ";":
            node, pos = _parse_node(s, pos)
            nodes.append(node)
        elif s[pos] == "(":
            subtree, pos = _parse_tree(s, pos)
            if nodes:
                nodes[-1].children.append(subtree)
        else:
            break

    if pos >= len(s) or s[pos] != ")":
        raise ValueError("tree missing")

    pos += 1  # skip ')'

    # Chain nodes: each node is the child of the previous
    for i in range(len(nodes) - 1):
        nodes[i].children.insert(0, nodes[i + 1])

    return nodes[0], pos


def _parse_node(s, pos):
    if s[pos] != ";":
        raise ValueError("tree with no nodes")

    pos += 1  # skip ';'
    properties = {}

    while pos < len(s) and s[pos] not in (";", ")", "("):
        # Parse key
        key_start = pos
        while pos < len(s) and s[pos].isalpha():
            pos += 1
        key = s[key_start:pos]

        if not key:
            break
        if not key.isupper():
            raise ValueError("property must be in uppercase")
        if pos >= len(s) or s[pos] != "[":
            raise ValueError("properties without delimiter")

        # Parse values
        values = []
        while pos < len(s) and s[pos] == "[":
            pos += 1  # skip '['
            value, pos = _parse_value(s, pos)
            values.append(value)

        properties[key] = values

    return SgfTree(properties), pos


def _parse_value(s, pos):
    chars = []

    while pos < len(s) and s[pos] != "]":
        ch = s[pos]
        if ch == "\\":
            pos += 1
            if pos >= len(s):
                break
            next_ch = s[pos]
            if next_ch == "\n":
                pos += 1
                continue  # escaped newline is removed
            else:
                # whitespace other than newline -> space
                if next_ch in (" ", "\t", "\r"):
                    chars.append(" ")
                else:
                    chars.append(next_ch)
                pos += 1
        else:
            if ch in (" ", "\t", "\r"):
                chars.append(" ")
            else:
                chars.append(ch)
            pos += 1

    if pos >= len(s) or s[pos] != "]":
        raise ValueError("properties without delimiter")

    pos += 1  # skip ']'
    return "".join(chars), pos
