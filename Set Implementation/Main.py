from BSTNode import Set


def show_set(set, set_name):
    print(set_name + ": ", end="")
    for element in set:
        print(element, end=" ")
    print("")


def even_predicate(element):
    return (element % 2) == 0


def over50_predicate(element):
    return element > 50


def map_times_10(element):
    return element * 10


def map_mod_10(element):
    return element % 10


setA = Set()
setA.add(95)
setA.add(64)
setA.add(19)
setA.add(67)
setA.add(-24)
setA.add(90)
setB = Set()
setB.add(67)
setB.add(90)
setB.add(67)
setB.add(42)
setB.add(-84)

# Display the 2 sets
show_set(setA, "Set A")
show_set(setB, "Set B")

# Perform union, intersection, and difference of 2 sets
show_set(setA.union(setB), "A union B")
show_set(setA.intersection(setB), "A intersect B")
show_set(setA.difference(setB), "A \ B")
show_set(setB.difference(setA), "B \ A")

# Perform various filter operations
show_set(setA.filter(even_predicate), "Set A filtered for evens")
show_set(setB.filter(even_predicate), "Set B filtered for evens")
show_set(setA.filter(over50_predicate), "Set A filtered for elements > 50")
show_set(setB.filter(over50_predicate), "Set B filtered for elements > 50")

# Perform various map operations
show_set(setA.map(map_times_10), "Set A mapped * 10")
show_set(setB.map(map_times_10), "Set B mapped * 10")
show_set(setA.map(map_mod_10), "Set A mapped % 10")
show_set(setB.map(map_mod_10), "Set B mapped % 10")
