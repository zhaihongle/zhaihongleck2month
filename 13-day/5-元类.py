def show(self):
    print("dasb")
Cat = type("Cat",(),{"name":"tom","show":show})
cat = Cat()
cat.show()

