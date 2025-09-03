row = int(input("Enter row: "))
col = int(input("Enter column: "))
search = int(input("Search: "))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        val = i * j
        if val == search:
            print(f"[{val}]", end="\t")
        else:
            print(val, end="\t")
    print()

