def list_ends(a_list):
    n = a_list[0]
    m = a_list[len(a_list)-1]
    new_list = [n, m]
    return new_list

a = [5, 10, 15, 20, 25]
print(list_ends(a))
