import random
import string

AMOUNT_OF_BLOCKS = 10
LENGTH_OF_BLOCK = 1000
INDEX_LENGTH = 5
STR_LENGTH = 20
LINE_LENGTH = 30
INDEX_LINE_LENGTH = 13
DATA_FILE = "data_file.txt"
INDEX_FILE = "index_file"


# ASSIST FUNCTIONS
def hash_func(index):
    return index // LENGTH_OF_BLOCK


def generate_random_string(length=STR_LENGTH):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def line_modify(record):
    line = str(record.is_deleted) + ";"
    str_index = str(record.index)
    while len(str(str_index)) < INDEX_LENGTH:
        str_index = "_" + str_index
    line += str_index + ";" + record.data + "\n"
    return line


def index_line_modify(index, data_index):
    str_index = str(index)
    while len(str(str_index)) < INDEX_LENGTH:
        str_index = "_" + str_index

    str_data_index = str(data_index)
    while len(str(str_data_index)) < INDEX_LENGTH:
        str_data_index = "_" + str_data_index

    return str_index + ";" + str_data_index + "\n"


def get_index(line_to_compare:str):
    index_line = int(line_to_compare.split(";")[0].strip('_'))
    return index_line


def create_files():
    for i in range(AMOUNT_OF_BLOCKS):
        f = open(INDEX_FILE + str(i) + ".txt", "x")
        f.close()


# MAIN FUNCTIONS
class Record:
    def __init__(self, is_deleted:int, index:int):
        self.is_deleted = is_deleted
        self.index = index
        self.data = generate_random_string()


def add_record(record):
    f = open(DATA_FILE, "a")
    f.write(line_modify(record))
    data_line_index = f.tell() // LINE_LENGTH
    f.close()

    index = hash_func(record.index)
    f_index = open(INDEX_FILE + str(index) + ".txt", "r")
    f_index.seek(0,2)
    f_index_length = f_index.tell() // INDEX_LINE_LENGTH

    left, right = 0, f_index_length
    while left < right:
        mid = left + (right - left) // 2
        f_index.seek(mid * INDEX_LINE_LENGTH)
        line = f_index.readline()
        if get_index(line) < record.index:
            left = mid + 1  # Move to the right half
        else:
            right = mid  # Move to the left half
    insert_index = left
    f_index.close()

    file = open(INDEX_FILE + str(index) + ".txt", "r+")
    file.seek(insert_index * INDEX_LINE_LENGTH)
    lines_after_insert = file.read()
    file.seek(insert_index * INDEX_LINE_LENGTH)
    file.write(index_line_modify(record.index, data_line_index) + lines_after_insert)
    file.close()


rec1 = Record(is_deleted=0, index=6)
add_record(rec1)