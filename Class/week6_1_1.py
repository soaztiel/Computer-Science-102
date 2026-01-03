library = {}

library  ['The Catcher in the Rye'] = 5
library  ['To Kill a Mockingbird'] = 3
library  ['1984'] = 6

print(library)

print(library.get('1984'))

library  ['The Catcher in the Rye'] = 6

print(library)

del library['To Kill a Mockingbird']

print(library)
