#item = (1, "Bob", "New York")
#item = [1, "Bob", "New York", "New York"]
item = (1, "Bob", "purple", "white")
print(type(item))
print(item)

id, name, *color = item
print(id)
print(name)
print(color)

new_colors = ["red", "blue", *color]
print(new_colors)

# -- Packing
def my_func(*args) -> None:
    print("hello")

# -- Unpacking
my_func(*["a", 1, True])

