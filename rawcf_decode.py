import os

def rle_decode(data):
    decoding = ''
    i = 0
    while i < len(data):
        count = ''
        while data[i].isdigit():
            count += data[i]
            i += 1
        decoding += data[i] * int(count)
        i += 1
    return decoding

# Function to decode rawcf file
def decode_rawcf(file_path):
    with open(file_path, 'r', encoding='ansi') as file:
        content = file.read()
    
    # Replace {enter} with real newline character
    content = content.replace('{enter}', '\n')

    # Split content by newline character
    lines = content.split('\n')
    
    # Extract header information
    file_description = lines[1]
    file_author = lines[2]
    file_name = lines[3]
    file_type = lines[4]
    file_ext = lines[5].strip('.')  # Remove extra dot
    encoded_data = lines[7]
    
    # Decode the data
    original_data = rle_decode(encoded_data)
    
    # Write the decoded data to a new file
    output_file_path = f"{file_name}{file_ext}"
    with open(output_file_path, file_type.replace("r", "w"), encoding='ansi') as output_file:
        output_file.write(original_data)

    print(f"Decoded file saved as {output_file_path}")

# Path to rawcf file
rawcf_file_path = input("File location to convert to rawcf (tip for Windows 11 users, go to the file and right click it and copy it as path): ").strip('"')

# Check if the .rawcf file exists
if os.path.exists(rawcf_file_path):
    decode_rawcf(rawcf_file_path)
else:
    print(".rawcf file not found")