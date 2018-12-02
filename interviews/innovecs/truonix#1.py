class CategoryTree:

    def __init__(self):
        self.categories = {}

    def add_category(self, category, parent):
        if category in self.categories:
            raise KeyError
        if parent is not None:
            self.categories[parent].append(category)
        self.categories[category] = []

    def get_children(self, parent):
        return self.categories[parent]


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A') or []))
