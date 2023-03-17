# Вердикт чекера и интерактора - целые числа от 0 до 7
# Код завершения задачи - целое число от -128 до 127

code = int(input())
interactor = int(input())
checker = int(input())


if interactor == 0:
    if code != 0:
        verdict = 3
    else:
        verdict = checker
elif interactor == 1:
    verdict = checker
elif interactor == 4:
    if code != 0:
        verdict = 3
    else:
        verdict = 4
elif interactor == 6:
    verdict = 0
elif interactor == 7:
    verdict = 1
else:
    verdict = interactor

print(verdict)
