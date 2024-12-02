def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    left_list, right_list = [], []
    for left_num, right_num in (line.split("   ") for line in data):
        left_list.append(int(left_num))
        right_list.append(int(right_num))

    similarity_score = sum([(num * right_list.count(num)) for num in left_list])
    print(similarity_score)


if __name__ == "__main__":
    main()