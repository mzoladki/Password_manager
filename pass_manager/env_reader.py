import os


def read_from_env_file():
    variables = {}
    with open('.env', 'r') as f:
        for line in f:
            split_line = line.split(' = ')
            variables[split_line[0].strip()] = split_line[1].strip()
    return variables
