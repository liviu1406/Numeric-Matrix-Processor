import numpy as np


def start_menu():
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")


def addition():
    row, col = input('Enter size of first matrix: ').split(" ")
    print('Enter first matrix: ')
    matrix = [list(map(float, input().split())) for i in range(int(row))]

    row2, col2 = input('Enter size of second matrix: ').split(" ")
    print('Enter second matrix: ')
    other_matrix = [list(map(float, input().split())) for j in range(int(row2))]

    if len(matrix) != len(other_matrix):
        print('The operation cannot be performed.')
    else:
        result = [[matrix[i][j] + other_matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        print('The result is:')
        for r in result:
            print(*r, sep=' ')


def multiplication_by_const():
    row, col = input('Enter size of matrix: ').split(" ")
    print('Enter matrix: ')
    matrix = [list(map(float, input().split())) for i in range(int(row))]
    a = np.array(matrix)
    print('Enter constant: ')
    const = float(input())
    multi_matrix = [element * const for element in a]
    print('The result is: ')
    for r in multi_matrix:
        print(*r, sep=' ')


def multiplication_by_matrix():
    rows, cols = input('Enter size of first matrix: ').split(" ")
    print('Enter first matrix: ')
    matrix = [list(map(float, input().split())) for i in range(int(rows))]

    row2, col2 = input('Enter size of second matrix: ').split(" ")
    print('Enter second matrix: ')
    other_matrix = [list(map(float, input().split())) for j in range(int(row2))]

    if cols != row2:
        print('The operation cannot be performed.')
    else:
        print('The result is: ')
        resultant = np.dot(matrix, other_matrix)
        for r in resultant:
            print(*r, sep=' ')


def transpose():
    choice = input('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line\n''')
    if choice == '1':
        rows, cols = input('Enter matrix size: ').split(" ")
        print('Enter matrix: ')
        matrix = [list(map(float, input().split())) for i in range(int(rows))]
        print('The result is:')
        res = np.transpose(matrix)
        for r in res:
            print(*r, sep=' ')
    elif choice == '2':
        rows, cols = input('Enter matrix size: ').split(" ")
        print('Enter matrix: ')
        matrix = [list(map(float, input().split())) for i in range(int(rows))]
        # res = matrix([::-1]).transpose()[::-1]
        res = np.transpose(matrix[::-1])
        re = np.transpose(res[::-1])
        t = np.transpose(re)
        print('The result is:')
        for r in t:
            print(*r, sep=' ')
    elif choice == '3':
        rows, cols = input('Enter matrix size: ').split(" ")
        print('Enter matrix: ')
        matrix = [list(map(float, input().split())) for i in range(int(rows))]
        res = np.fliplr(matrix)
        print('The result is:')
        for r in res:
            print(*r, sep=' ')
    elif choice == '4':
        rows, cols = input('Enter matrix size: ').split(" ")
        print('Enter matrix: ')
        matrix = [list(map(float, input().split())) for i in range(int(rows))]
        res = np.flipud(matrix)
        print('The result is:')
        for r in res:
            print(*r, sep=' ')


def matrix_determinant():
    rows, cols = input('Enter matrix size: ').split(" ")
    print('Enter matrix: ')
    matrix = [list(map(float, input().split())) for i in range(int(rows))]
    print('The result is:')
    res = np.linalg.det(matrix)
    print(res)


def matrix_inverse():
    rows, cols = input('Enter matrix size: ').split(" ")
    print('Enter matrix: ')
    matrix = [list(map(float, input().split())) for i in range(int(rows))]
    print('The result is:')
    try:
        res = np.linalg.inv(matrix)
        for r in res:
            print(*r, sep=' ')
    except np.linalg.LinAlgError:
        print("This matrix doesn't have an inverse.")


def matrix_processor():
    while True:
        print()
        start_menu()
        user = input()
        if user == '1':
            addition()
        elif user == '2':
            multiplication_by_const()
        elif user == '3':
            multiplication_by_matrix()
        elif user == '4':
            transpose()
        elif user == '5':
            matrix_determinant()
        elif user == '6':
            matrix_inverse()
        elif user == '0':
            exit()


matrix_processor()
