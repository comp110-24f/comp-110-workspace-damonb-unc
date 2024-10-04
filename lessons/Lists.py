# my_numbers: list[float] = list()

# my_numbers.append(1.5)

game_points: list[int] = [102, 86, 94]
print(game_points)
print(game_points[0])

game_points[1] = 72
print(game_points)

print(len(game_points))

game_points.append(94)
print(game_points)

game_points.pop(1)
print(game_points)


def display(int_list: list[int]) -> None:

    index: int = 0

    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
