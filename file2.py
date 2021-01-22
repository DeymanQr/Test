import os


def find_file(path, file):
    for i in os.listdir(path):
        new_path = os.path.join(path, i)
        if os.path.isdir(new_path):
            res = find_file(new_path, file)
            if res:
                return res
        elif path == file:
            return os.path.abspath(new_path)


if __name__ == '__main__':
    find_file('test', 'file1.py')
