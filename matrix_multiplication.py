# matrix_multiplication.py
# Program to multiply two matrices

def multiply_matrices(m1, m2):
    rows_m1, cols_m1 = len(m1), len(m1[0])
    rows_m2, cols_m2 = len(m2), len(m2[0])

    if cols_m1 != rows_m2:
        raise ValueError("Matrix multiplication not possible! Columns of first != Rows of second")

    result = [[0 for _ in range(cols_m2)] for _ in range(rows_m1)]

    for i in range(rows_m1):
        for j in range(cols_m2):
            for k in range(cols_m1):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def main():
    print("=== Matrix Multiplication ===")
    try:
        r1 = int(input("Enter rows of first matrix: "))
        c1 = int(input("Enter columns of first matrix: "))
        r2 = int(input("Enter rows of second matrix: "))
        c2 = int(input("Enter columns of second matrix: "))

        print("Enter elements of first matrix:")
        m1 = [[int(input(f"m1[{i}][{j}]: ")) for j in range(c1)] for i in range(r1)]

        print("Enter elements of second matrix:")
        m2 = [[int(input(f"m2[{i}][{j}]: ")) for j in range(c2)] for i in range(r2)]

        result = multiply_matrices(m1, m2)

        print("\nResultant Matrix:")
        for row in result:
            print(row)
    except ValueError as e:
        print("⚠️", e)

if __name__ == "__main__":
    main()
