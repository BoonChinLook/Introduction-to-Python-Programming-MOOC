# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count_matching = 0
    for row in my_matrix:
        count_matching += row.count(element)
    return count_matching

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))
            