# local scope
# cannot access outside of it
# think of like public/private in java????

# local scope
def square(value):
    new_val = value ** 2
    return new_val
square(3)

new_val

'''
==> ERROR!
Traceback (most recent call last):
  File "<string>", line 6, in <module>
NameError: name 'new_val' is not defined
'''

# global 
new_val = 10

def square(value):
    new_val = value ** 2
    return new_val
square(3)
# ==> 9
new_val
# ==> 10


