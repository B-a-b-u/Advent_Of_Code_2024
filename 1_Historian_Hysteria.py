# Problem
# https://adventofcode.com/2024/day/1


def find_total_distance():
    left, right = list(),list()
    n = 0
    with open("1_input.txt","r") as file:
        for line in file.readlines():
            # print(f"line : {line}")
            l,r = map(int,line.split())
            left.append(l)
            right.append(r)
            n += 1

    # print(f"l : {left} r:{right}")

    total_distance = 0
    left.sort()
    right.sort()
    for i in range(n):
        total_distance += abs(left[i] - right[i])

    return total_distance


def find_similarity_score():
    similarity_score = 0
    left = list()
    right_freq = dict()
    n = 0
    with open("1_input.txt","r") as file:
        for line in file.readlines():
            # print(f"line : {line}")
            l,r = map(int,line.split())
            left.append(int(l))
            if right_freq.get(r):
                right_freq[r] += 1
            else:
                right_freq[r] = 1
            n += 1
    print(right_freq)
    for i in range(n):
        print(f"l : {left[i]} r:{right_freq.get(left[i],0)}")
        similarity_score += left[i] * right_freq.get(left[i],0)
    return similarity_score

# print(find_total_distance())
print(find_similarity_score())