# Алгоритм RLE (англ. Run-length encoding) — простой алгоритм сжатия данных, который оперирует сериями данных, т. е.
# последовательностями, в которых один и тот же символ встре­
# чается несколько раз подряд. При кодировании строка одинаковых символов,
# составляющих серию, заменяется строкой, которая содержит сам повторяющийся символ и количество его
# повторов.

def rle(s):
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]
    lastpos = 0
    ans = []

    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))

    return ''.join(ans)


data = input()
result = rle(data)
print(result)
