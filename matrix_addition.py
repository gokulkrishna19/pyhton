# matrix_addition.py
# Program to add two matrices of the same size

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def main():
    print("=== Matrix Addition ===")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("Enter elements of first matrix:")
        matrix1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

        print("Enter elements of second matrix:")
        matrix2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

        result = add_matrices(matrix1, matrix2)
        print("\nResultant Matrix:")
        for row in result:
            print(row)
    except ValueError:
        print("⚠️ Please enter valid integers!")

if __name__ == "__main__":
    main()
