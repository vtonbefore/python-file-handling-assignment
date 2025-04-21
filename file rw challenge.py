def modify_file_content(input_file, output_file):
    """
    Reads content from input_file, modifies it, and writes to output_file.
    Converts text to uppercase as an example modification.
    """
    try:
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"File successfully modified and saved as {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: Could not read {input_file} or write to {output_file}")

# Example usage:
# modify_file_content('input.txt', 'output.txt')