def check_bench(bench_length_and_legs_count, legs):
    bench_length, legs_count = map(int, bench_length_and_legs_count.split())
    legs = list(map(int, legs.split()))

    center = bench_length // 2

    for i, leg in enumerate(legs):
        if leg == center:
            if bench_length % 2 == 0:
                l_leg = legs[i - 1]
                r_leg = leg
                return [l_leg, r_leg]
            return leg
        elif leg > center:
            l_leg = legs[i - 1]
            r_leg = leg
            return [l_leg, r_leg]


# left_index = legs[:center]
# right_index = legs[center:]
#
# if center not in left_index and center not in right_index:
#
