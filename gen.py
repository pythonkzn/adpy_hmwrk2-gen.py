import hashlib


def my_md5_gen(path):
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            hash_line = hashlib.md5()
            hash_line.update(line.encode('utf8'))
            yield line


my_gen = my_md5_gen('example.txt')

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))





