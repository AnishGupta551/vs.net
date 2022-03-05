from database import Simpledb


db = Simpledb('recipes.txt')
print(db)
print()
db.insert('relish', 'Pickled cucumber and sugar')
db.insert('pesto', 'Basil and olive oil')
print(db.select_one('pesto'))
db.delete('pesto')
db.update('relish', 'Pickled cucumber and sugar AND OREGANO')
