total = 0
while True:
    n = input()
    try:
        n = float(n)
        if n == 0:
            print(f"The grand total is {total}")
            break
        else:
            total += n
            print(f"The total is now {total}")
    except ValueError:
        print("That wasn’t a number.")