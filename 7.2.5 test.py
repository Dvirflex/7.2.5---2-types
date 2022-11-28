def sequence_del(my_str):
    l = []
    for ch in my_str:
        if ch not in l:
            l.append(ch)
    print("".join(l))

sequence_del("ppyyyyythhhhhooonnnnn")