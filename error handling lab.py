def read_file_with_handling():
    """
    Asks user for a filename and attempts to read it with proper error handling.
    """
    while True:
        filename = input("Enter the filename you want to read (or 'quit' to exit): ")
        
        if filename.lower() == 'quit':
            break
            
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Please try another file.")
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory, not a file. Please enter a filename.")
        except UnicodeDecodeError:
            print(f"Error: Could not decode '{filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

# Example usage:
# read_file_with_handling()