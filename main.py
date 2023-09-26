import numpy


def get_house_by_value(row: int, value: int) -> int:
    try:
        return numpy.where(matrix[row] == value)[0][0]
    except IndexError:
        raise Exception()


def get_empty_house(row: int) -> int:
    try:
        return numpy.where(matrix[row] == 0)[0][0]
    except IndexError:
        raise Exception()


def add_constraint(val1: tuple[int, int], val2: tuple[int, int]):
    """val: tuple(row,value)"""
    if val1[1] not in matrix[val1[0]] and val2[1] not in matrix[val2[0]]:
        empty_house = 0
        constraint_ok = False
        while not constraint_ok:
            if empty_house > 4:
                raise Exception()
            if matrix[val1[0]][empty_house] == 0 and matrix[val2[0]][empty_house] == 0:
                matrix[val1[0]][empty_house] = val1[1]
                matrix[val2[0]][empty_house] = val2[1]
                constraint_ok = True
            else:
                empty_house += 1
    elif val1[1] in matrix[val1[0]]:
        house = get_house_by_value(val1[0], val1[1])
        matrix[val2[0]][house] = val2[1]
    elif val2[1] in matrix[val2[0]]:
        house = get_house_by_value(val2[0], val2[1])
        matrix[val1[0]][house] = val1[1]


def add_constraint_next_house(val1: tuple[int, int], val2: tuple[int, int], house: int):
    """val: tuple(row,value)"""
    matrix[val1[0]][house] = val1[1]

    if matrix[val2[0]][house - 1] == val2[1] or matrix[val2[0]][house + 1] == val2[1]:
        return

    if matrix[val2[0]][house - 1] == 0 and house - 1 > 0:
        matrix[val2[0]][house - 1] = val2[1]
    elif matrix[val2[0]][house + 1] == 0 and house + 1 < 5:
        matrix[val2[0]][house + 1] = val2[1]
    else:
        raise Exception()


def move_constraint(val: tuple[int, int], from_house: int, to_house: int):
    """val: tuple(row 1, row 2)"""
    if matrix[val[0]][to_house] == 0 and matrix[val[1]][to_house] == 0:
        matrix[val[0]][to_house] = matrix[val[0]][from_house]
        matrix[val[1]][to_house] = matrix[val[1]][from_house]

        matrix[val[0]][from_house] = 0
        matrix[val[1]][from_house] = 0
    else:
        raise Exception()


color_set = ["red", "yellow", "ivory", "green", "blue"]
national_set = ["english", "spanish", "ukraine", "norwegian", "japanese"]
drink_set = ["coffee", "tea", "milk", "water", "orange juice"]
cigarette_set = ["kools", "chesterfield", "old gold", "lucky strike", "parliaments"]
pet_set = ["dog", "snails", "fox", "hourse", "zebra"]

print(f"colors: {list(enumerate(color_set, 1))}")
print(f"nationals: {list(enumerate(national_set, 1))}")
print(f"drinks: {list(enumerate(drink_set, 1))}")
print(f"cigarettes: {list(enumerate(cigarette_set, 1))}")
print(f"pets: {list(enumerate(pet_set, 1))}")
print(
    """
|house 1|house 2|house 3|house 4|house 5|
-----------------------------------------
row 0: color
row 1: national
row 2: drink
row 3: cigarette
row 4: pet
"""
)

matrix = numpy.zeros((5, 5))

# Milk is drunk in the middle house.
matrix[2][2] = 3

# The Norwegian lives in the first house.
matrix[1][0] = 4

# The Norwegian lives next to the blue house.
matrix[0][1] = 5

# The Englishman lives in the red house
add_constraint((1, 1), (0, 1))

# The Ukrainian drinks tea
add_constraint((1, 3), (2, 2))

# The Spaniard owns the dog
add_constraint((1, 2), (4, 1))

# Coffee is drunk in the green house
add_constraint((2, 1), (0, 4))

# The green house is immediately to the right of the ivory house
move_constraint((2, 0), 0, 4)
add_constraint_next_house((0, 3), (0, 4), 3)

# Kools are smoked in the yellow house.
add_constraint((3, 1), (0, 2))

# The Old Gold smoker owns snails.
add_constraint((3, 3), (4, 2))

# Kools are smoked in the house next to the house where the horse is kept.
move_constraint((4, 3), 1, 2)
add_constraint_next_house((4, 4), (3, 1), 1)

# The man who smokes Chesterfields lives in the house next to the man with the fox.
add_constraint_next_house((4, 3), (3, 2), 0)

# The Lucky Strike smoker drinks orange juice.
add_constraint((3, 4), (2, 5))

# The Japanese smokes Parliaments.
add_constraint((1, 5), (3, 5))

# add zebra and water
empty_house = get_empty_house(4)
matrix[4][empty_house] = 5

empty_house = get_empty_house(2)
matrix[2][empty_house] = 4

print(f"result table:\n{matrix}")
print(f"the zebra is in house: {get_house_by_value(4, 5) + 1}")
print(f"the water drinks in house: {get_house_by_value(2, 4) + 1}")
