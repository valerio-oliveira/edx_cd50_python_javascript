# Create an empty set
s = set()

# add elements to the set

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)

# repeated elements are ignored if we try to add it to de set
s.add(3)
s.add(4)

# removing an item
s.remove(3)

print (s)

print (f"The set has {len(s)} elements")