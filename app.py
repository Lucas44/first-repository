def find_element(a_list, element):
    for item in a_list:
        if item == element:
            return True
    return False

print find_element([1,2,3,4], 5)