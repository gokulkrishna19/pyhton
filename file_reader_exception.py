# file_reader_exception.py
# Program to demonstrate exception handling in file operations

def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "⚠️ Error: File not found."
    except PermissionError:
        return "⚠️ Error: Permission denied while accessing the file."
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"

def main():
    print("=== File Reader with Exception Handling ===")
    filename = input("Enter filename to read: ")
    content = read_file(filename)
    print("\nFile Content / Error:\n", content)

if __name__ == "__main__":
    main()
