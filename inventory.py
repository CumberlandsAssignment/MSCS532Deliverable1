from hash_table import HashTable
from avl_tree import AVLTree
from min_heap import MinHeap


class Product:
    def __init__(self, sku, name, category, price, quantity):
        self.sku = sku
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity


class InventoryManager:

    def __init__(self):
        self.products = HashTable()
        self.category_trees = {}
        self.heap = MinHeap()

    def add_product(self, product):
        self.products.insert(product.sku, product)

        if product.category not in self.category_trees:
            self.category_trees[product.category] = {
                "tree": AVLTree(),
                "root": None
            }

        tree_data = self.category_trees[product.category]
        tree = tree_data["tree"]

        tree_data["root"] = tree.insert(
            tree_data["root"],
            product.price,
            product
        )

        self.heap.push(product.quantity, product.sku)

    def get_product(self, sku):
        return self.products.get(sku)

    def reorder_alerts(self, k):
        return self.heap.get_top_k(k)

    def list_by_price(self, category, low, high):
        if category not in self.category_trees:
            return []

        tree_data = self.category_trees[category]
        result = []

        tree_data["tree"].range_query(
            tree_data["root"],
            low,
            high,
            result
        )

        return result