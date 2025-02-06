# ws 1
# 1

def odd_values(n:int) -> list[int]:
    if n <= 0:
        return []

    list = []
    min = 13

    while len(list) < n:
        list.append(min)
        min += 2

    return list

print(odd_values(10))

############################################################################################################
# 2
def rectangle_area(width:int, height:int) -> int:

    if width > 0 and height > 0:
        area = width * height
        print(area)

    elif width <= 0 or height <= 0:
        print(0)

area = rectangle_area(-1,3)

