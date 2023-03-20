def check_str(seq):

    summa = 0
    left = 0
    answer = None

    while not answer:
        while left < len(seq) and seq[left] == '(':
            summa += 1
            left += 1

        if summa == 0:
            answer = "NO"
            return answer

        right = left

        while right < len(seq) and seq[right] == ')':
            summa -= 1
            right += 1

        left = right

        if right == len(seq):
            answer = "YES" if summa == 0 else "NO"

    return answer
