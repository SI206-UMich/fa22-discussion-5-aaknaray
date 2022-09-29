import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for char in sentence:
		if char == 'a':
			total += 1
	return total

# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)
		pass

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = item[0][2]
		for item in self.items:
			if item[0][2] > max_stock:
				max_stock = item[0][2]
		return item

	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = item[0][1]
		for item in self.items:
			if item[0][1] > max_price:
				max_price = item[0][1]
		return item	

# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(4, count_a("I am a student at the University of Michigan."))
		self.assertEqual(1, count_a("Urban Technology."))
		self.assertTrue(type(self.item1[0]) == str)
		self.assertEqual(0, count_a(self.item1[0]))
		pass


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.add_item(Warehouse, self.item1)
		self.add_item(Warehouse, self.item2)
		self.add_item(Warehouse, self.item3)
		self.add_item(Warehouse, self.item4)
		self.add_item(Warehouse, self.item5)
		self.assertTrue(type(Warehouse) == list)
		self.assertTrue(len(Warehouse == 5))
		self.assertEqual(Warehouse == [("Beer", 6, 20), ("Cider", 5, 25), ("Water", 1, 100), ("Fanta", 2, 60), ("CocaCola", 3, 40) ])
		pass


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		self.assertEqual(Warehouse.get_max_stock(self.items) == "Water")
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(Warehouse.get_max_price(self.items) == "Beer")
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()