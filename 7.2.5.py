def sequence_del(my_str):
    result = ''
    for i in range(len(my_str)):
        if (i == 0 or my_str[i] != my_str[i - 1]):
            result += my_str[i]
    print(result)

sequence_del('ppyyyyythhhhhooonnnnn')
