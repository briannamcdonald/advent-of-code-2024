def get_diff(report):
    return [abs(report[i] - report[i - 1]) for i in range(1, len(report))]

def main():
    data = open("input.txt", "r")
    data = [line.strip() for line in data]

    safe_count = 0
    for report in data:
        levels = [int(level) for level in report.split(" ")]

        for i in range(len(levels)):
            # try removing one of the levels
            modified_levels = levels.copy()
            del modified_levels[i]

            diff = get_diff(modified_levels)
            if (modified_levels == sorted(modified_levels) or modified_levels == sorted(modified_levels, reverse=True)) and max(diff) <= 3 and min(diff) >= 1:
                safe_count += 1
                break

    print(safe_count)


if __name__ == "__main__":
    main()