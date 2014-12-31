python-invert
=============
This is a silly project. I feel that's something importent to state up front.

One day I was thinking about how python 3 allows variable names to be unicode, and it got me thinking about ways to abuse it. I them remembered that unicode includes characters that look like upside-down versions of the standard alphabet, which leads to the obvious question: What should happen when you type a variable name upside-down? I present the following code:
```
mystring = 'Hello World!'
add_inverts(mystring)

print(ɯʎsʇɹᴉuƃ)
# Prints 'Hǝllo Moɹlp¡'
```
I think this is an entirely reasonable answer. What's more, we can extend this simple concept to arrays and matricies, and we cansupport backwards text along with upside-down text. This allows us to perform matrix transformations with ease:
```
matrix = numpy.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
add_inverts(matrix)

print(matrix)
# [ 1 2 3 ]
# [ 4 5 6 ]
# [ 7 8 9 ]

print(ɯɐʇɹᴉx)
# [ 7 8 9 ]
# [ 4 5 6 ]
# [ 1 2 3 ]

print(xᴉɹʇɐɯ)
# [ 9 8 7 ]
# [ 6 5 4 ]
# [ 3 2 1 ]

print(xirtam)
# [ 3 2 1 ]
# [ 6 5 4 ]
# [ 9 8 7 ]
```
I wish I could make the namespace pollution happen automatically when a variable is created, but unfortunatly I can't find a way to do that without modifying python itself, so the add_inverts call is necessary. If you have a way, let me know.
