import os

# List of restricted author names
restricted_authors = [
    'Microsoft Corporation',
    'Windows',
    'Administrators',
    'SYSTEM',
    'TrustedInstaller',
    'Local Service',
    'Network Service',
]

# List of restricted file types
rb_type = [
    '1.jpg', '1.jpeg', '1.png ', '1.gif', '1.bmp', '1.tiff', '.jfif',
    '1.mp3', '1.wav', '1.flac', '1.aac', '1.mp4', '1.avi', '1.mkv',
    '1.mov', '1.exe', '1.bin', '1.dll', '1.app', '1.pdf', '1.zip',
    '1.rar', '1.tar', '1.iso', '1.sqlite', '1.img', '1.blend',
    '1.obj', '1.usd', '1.fbx', '1.abc'
]

# List of allowed file types
r_type = [
    '1.txt', '1.csv', '1.json', '1.xml', '1.html', '1.md',
    '1.py', '1.c', '1.cpp', '1.sh'
]

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1

    encoding += str(count) + prev_char
    return encoding

# Input for file location and author name
file_location = input('File location to convert to rawcf (tip for Windows 11 users, go to the file and right click it and copy it as path): ').strip('"')
file_author = input('Set some random author name: ')

# Check if the author name is restricted
if file_author in restricted_authors:
    print(f'{file_author} is not accepted as an author name due to privileges.')
else:
    # Proceed with the conversion process
    print(f'Author name {file_author} accepted.')
    # Your conversion logic here

file_description = input('Insert a description: ')
file_name = 'new_rawcf_file'
file_ext = '1' + os.path.splitext(file_location)[1]

if file_ext in r_type:
    file_type = 'r'
    file_type_write = 'w'
elif file_ext in rb_type:
    file_type = 'rb'
    file_type_write = 'wb'
else:
    print('file not supported')
    print(file_ext)
    exit()

# Read the file content based on the file type
if file_type == 'r':
    with open(file_location, file_type, encoding='ANSI') as file:
        file_data = file.read()  # Read the entire content of the file
else:
    with open(file_location, file_type) as file:
        file_data = file.read()  # Read the entire content of the file

comp_data = rle_encode(file_data)

output_file = ['header', file_description, file_author, file_name, file_type, file_ext, 'file', comp_data]

# Join the output file list with {enter} as the separator
decoded_output = '{enter}'.join(output_file)

# Write the decoded output to a new file
with open(file_name + '.rawcf', file_type_write, encoding='ansi') as output:
    output.write(decoded_output)