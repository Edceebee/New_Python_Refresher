def numbers():
    squares = ["One", "Two", "Three", "Four", "Five"]
    values = [1, 2, 3, 4, 5]
    squared_values = [each_number ** 2 for each_number in values]

    print(dict(zip(squares, squared_values)))


numbers()
