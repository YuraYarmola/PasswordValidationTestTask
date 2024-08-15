import re


def parse_line(line):
    pattern = re.compile(r'(\w) (\d+)-(\d+): (\w+)')
    match = pattern.match(line.strip())
    if match:
        char, min_count, max_count, password = match.groups()
        return char, int(min_count), int(max_count), password
    return None


def is_valid_password(char, min_count, max_count, password):
    char_count = password.count(char)
    return min_count <= char_count <= max_count


def count_valid_passwords(file_name):
    valid_passwords_count = 0

    with open(file_name, 'r') as file:
        for line in file:
            parsed = parse_line(line)
            if parsed:
                char, min_count, max_count, password = parsed
                if is_valid_password(char, min_count, max_count, password):
                    valid_passwords_count += 1

    return valid_passwords_count


file_name = 'test_file.txt'
print("Number of valid passwords:", count_valid_passwords(file_name))
