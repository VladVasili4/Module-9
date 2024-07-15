def apply_all_func(int_list, *functions):
    reuslts = {}
    for i in functions:
        funk = i(int_list)
        reuslts += funk     # немного не то, что надо
