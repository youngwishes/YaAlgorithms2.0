def palindrome(s):
    print('-' * 10, 'START WITH', s, '-' * 10)
    mid = len(s) // 2

    left_side = []
    for sym in s[:mid]:
        left_side.append(sym)

    right_side = []

    if len(s) % 2 != 0:
        mid += 1

    for sym in s[mid:]:
        right_side.append(sym)

    money_to_pay = 0

    for i, sym in enumerate(left_side[::-1]):
        if sym != right_side[i]:
            money_to_pay += 1

    return money_to_pay

