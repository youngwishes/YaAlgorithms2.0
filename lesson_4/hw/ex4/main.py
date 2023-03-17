with open('input.txt', 'r') as f:
    parties = []
    total_voices = 0

    for line in f:
        splited = line.split()
        name, voices = ' '.join(splited[:-1]), int(splited[-1])
        parties.append((name, voices))
        total_voices += voices

coefficient = total_voices / 450

parliamentary_seats = {}

coef_info = {}
for party_name, voices in parties:
    parliamentary_seats[party_name] = voices // coefficient
    particial = voices % coefficient
    coef_info[party_name] = (float(particial), voices)

summa = sum(parliamentary_seats.values())

while summa < 450:
    for party_name, coeff in sorted(coef_info.items(), key=lambda x: x[1], reverse=True):

        parliamentary_seats[party_name] += 1
        summa += 1
        if summa == 450:
            break

for party in parties:
    print(party[0], int(parliamentary_seats.get(party[0])))
