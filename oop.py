# class Fruits:
#     def __init__(self):
#         self.name = "watermelon"
#         self.color = "red"
# Fruits = Fruits()
# Fruits.name = "mango"
# Fruits.color = "yellow"
# # print(Fruits)
# print(Fruits.name)
# print(Fruits.color)


class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color


Fruits1 = Fruits("apple", "red")
Fruits2 = Fruits("mango", "yellow")
Fruits3 = Fruits("watermellon", "red")

print(f"fruit1 name : {Fruits1.name}")
print(f"fruit1 color: {Fruits1.color}")

print(f"fruit2 name :{Fruits2.name}")
print(f"fruit2 color :{Fruits2.color}")

print(f"fruit3 name :{Fruits3.name}")
print(f"fruit3 color :{Fruits3.color}")