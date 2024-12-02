def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    left_list, right_list = [], []
    for left_num, right_num in (line.split("   ") for line in data):
        left_list.append(int(left_num))
        right_list.append(int(right_num))

    total_dist = sum([abs(left_num - right_num) for left_num, right_num in zip(sorted(left_list), sorted(right_list))])
    print(total_dist)


if __name__ == "__main__":
    main()