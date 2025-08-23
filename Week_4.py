# Assignment: File Read & Write with Error Handling!

input_filename = input("Enter the name of the file you want to read (e.g., my_text.txt): ")

output_filename = input_filename.replace(".txt", "") + "_UPPER.txt"

# Error Handling Section
try:
    with open(input_filename, 'r') as file:
        
        original_content = file.read()
        print(f"\n--- Original content from '{input_filename}' ---")
        print(original_content)
        print("-------------------------------------------")

    # 2. Modify the content (make it all uppercase!).

    modified_content = original_content.upper()

    # 3. Write the modified content to a new file.
   
    with open(output_filename, 'w') as file:
        file.write(modified_content)
    
    print(f"Success! Content from '{input_filename}' converted to uppercase and saved to '{output_filename}'.")

except FileNotFoundError:
    print(f"Oops! I couldn't find a file named '{input_filename}'. Please make sure it's in the same folder as this script and you typed the name correctly.")

