class InventoryHashTable:
    """
    Custom hash table for product inventory.

    Rules:
    - Use a list of buckets (self.table)
    - Each bucket is a list (separate chaining)
    - Product data: sku, name, quantity
    """

    def __init__(self, size=10):
        self.size = size
        # Create list of empty buckets
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        Simple hash function:
        - Sum ASCII values of characters
        - Modulo table size
        """
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def set_item(self, sku, name, quantity):
        """
        Add new product or update existing one.
        """
        index = self._hash(sku)
        bucket = self.table[index]

        # Check if SKU already exists → update
        for item in bucket:
            if item["sku"] == sku:
                item["name"] = name
                item["quantity"] = quantity
                print(f"Updated product {sku}")
                return

        # Otherwise add new item
        bucket.append({
            "sku": sku,
            "name": name,
            "quantity": quantity
        })
        print(f"Added product {sku}")

    def get_item(self, sku):
        """
        Return product if found, else None.
        """
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                return item

        return None

    def remove_item(self, sku):
        """
        Remove product by SKU.
        """
        index = self._hash(sku)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item["sku"] == sku:
                del bucket[i]
                return True

        return False

    def print_table(self):
        """
        Print all buckets and contents.
        """
        print("\n=== Inventory Hash Table ===")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


# =========================
# FOR TESTING
# =========================

inv = InventoryHashTable(size=7)

inv.set_item("A101", "USB Cable", 25)
inv.set_item("B205", "Keyboard", 12)
inv.set_item("C333", "Mouse", 18)
inv.set_item("A101", "USB Cable", 30)  # update

inv.print_table()

print("Search B205:", inv.get_item("B205"))
print("Remove C333:", inv.remove_item("C333"))

inv.print_table()