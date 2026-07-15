def validate_file_extension(filename):
    return filename.endswith('.pt')

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
