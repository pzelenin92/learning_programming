"""Minimum union of points which lay down on given sections"""


def union_points(inner_section_list):
    """Takes list with sections, prints quantity of points and points themselves"""
    inner_section_list.sort(key=lambda x: x[1])

    point = [inner_section_list[0][1]]

    for section in inner_section_list[1:]:
        if section[0] > point[-1:][0]:
            point.append(section[1])

    print(len(point))
    for i in point:
        print(i, end=' ')


def main():
    """main function"""
    n, section_list, i = int(input()), [], 0

    while i < n:
        section_list.append([int(i) for i in input().split()])
        i += 1

    union_points(section_list)


if __name__ == '__main__':
    main()
