names = ["Luna", "Grisha", "Leo"]

for a in names:
    print(a)

library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95),
           ('Hamilton', 'Mythology', 144)]
for book in library:
    print(f'{book[0]:{10}} {book[1]:{9}} {book[2]:{7}}')
