list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

def merge_lists(list1, list2):
    return list1 + list2

print("Merged List:", merge_lists(list1, list2))