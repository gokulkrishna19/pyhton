# matrix_transpose.py
# Program to find the transpose of a matrix

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    return transpose

def main():
    print("=== Matrix Transpose ===")
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print("Enter elements of the matrix:")
        matrix = [[int(input(f"m[{i}][{j}]: ")) for j in range(cols)] for i in range(rows)]

        result = transpose_matrix(matrix)

        print("\nOriginal Matrix:")
        for row in matrix:
            print(row)

        print("\nTranspose Matrix:")
        for row in result:
            print(row)
    except ValueError:
        print("⚠️ Please enter valid integers!")

if __name__ == "__main__":
    main()
