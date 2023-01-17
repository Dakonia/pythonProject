print("  Привествуем вас в игре  ")
print("     Крестики-нолики      ")
print(" Первый ввод номер строки ")
print(" Второй ввод номер столбца")
print("     Начинает крестик     ")

field= [['-']*3 for _ in range(3)]
def show_field():
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i),*field[i])
def game():
    while True:
        num = input("Ваш ход:").split()
        if len(num) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = num
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Таких клеток нет! ")
            continue

        if field[x][y] != "-":
            print(" Клетка занята! ")
            continue

        return x, y

def win():
    win_num= (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for nums in win_num:
        symbols = []
        for l in nums:
            symbols.append(field[l[0]][l[1]])
        if symbols == ["X", "X", "X"]:
            print("Win X")
            return True
        if symbols == ["0", "0", "0"]:
            print("Win 0")
            return True
    return False

count = 0
while True:
    count += 1
    show_field()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")
    x, y = game()
    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"
    if win():
        break
    if count == 9:
        print(" Ничья!")
        break


