class Tree:
    def tree_data(self, n, c, q, r, v):
        self._name = n
        self._colour = c
        self._quantity = q
        self._root = r
        self._venation = v

    def print_data(self):
        print(self._name)
        print(self._colour)
        print(self._quantity)
        print(self._root)
        print(self._venation)

tree = Tree()
tree.tree_data("Banyan", "green", 1, "tap root", "reticulate venation")
tree.print_data()