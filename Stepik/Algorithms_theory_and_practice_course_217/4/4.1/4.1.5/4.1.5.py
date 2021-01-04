"""Maximum nonintersecting sections"""


def nonintersecting_sections(inner_section_list):
    """Takes list with sections, prints quantity of nonintersecting sections and
     sections themselves"""
    inner_section_list.sort(key=lambda x: x[1])  # sort by the length of the right ends
    chosen_sections = [inner_section_list[0]]

    for section in inner_section_list[1:]:
        if section[0] > chosen_sections[-1][1]:  # add the first nonintersecting section
            chosen_sections.append(section)

    print(len(chosen_sections))
    for i in chosen_sections:
        print(i, end=' ')


def main():
    """main function"""
    n, section_list, i = int(input()), [], 0

    while i < n:
        section_list.append([int(i) for i in input().split()])
        i += 1

    nonintersecting_sections(section_list)


if __name__ == '__main__':
    main()
