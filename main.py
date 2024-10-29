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


def data_modify(data):
    if len(data) > STR_LENGTH:
        return data[:STR_LENGTH]
    elif len(data) < STR_LENGTH:
        while len(data) < STR_LENGTH:
            data = data + '_'
    return data


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


def binary_search_to_insert(left, right, file, index):
    while left < right:
        mid = left + (right - left) // 2
        file.seek(mid * INDEX_LINE_LENGTH)
        line = file.readline()
        if get_index(line) < index:
            left = mid + 1  # Move to the right half
        else:
            right = mid  # Move to the left half
    return left


def binary_search(file, left, right, index):
    while left <= right:
        mid = left + (right - left) // 2  # Calculate the midpoint
        file.seek(mid * INDEX_LINE_LENGTH)
        line = file.readline()
        index_of_line = get_index(line)
        if index_of_line == index:
            return mid  # Target found
        elif index_of_line < index:
            left = mid + 1  # Discard left half
        else:
            right = mid - 1  # Discard right half
    return -1  # Target not found


def add_record(record):
    f = open(DATA_FILE, "a")
    f.write(line_modify(record))
    data_line_index = f.tell() // LINE_LENGTH
    f.close()

    index = hash_func(record.index)
    f_index = open(INDEX_FILE + str(index) + ".txt", "r+")
    f_index.seek(0,2)
    f_index_length = f_index.tell() // INDEX_LINE_LENGTH

    insert_index = binary_search_to_insert(0, f_index_length, f_index, record.index)

    f_index.seek(insert_index * INDEX_LINE_LENGTH)
    lines_after_insert = f_index.read()
    f_index.seek(insert_index * INDEX_LINE_LENGTH)
    f_index.write(index_line_modify(record.index, data_line_index) + lines_after_insert)
    f_index.close()


def edit_record(rec_index, data):
    index = hash_func(rec_index)
    file_search = open(INDEX_FILE + str(index) + ".txt", "r")
    file_search.seek(0, 2)
    f_index_length = file_search.tell() // INDEX_LINE_LENGTH

    editing_index = binary_search(file_search, 0, f_index_length, rec_index)

    file_search.seek(editing_index * INDEX_LINE_LENGTH)
    editing_line = file_search.readline()
    editing_line_data_index = int(editing_line.split(';')[1].strip('_')) - 1
    file_search.close()

    file_edit = open(DATA_FILE, "r+")
    file_edit.seek(editing_line_data_index * LINE_LENGTH)
    lines_edit = file_edit.readlines()
    lines_edit[0] = ';'.join(line_to_edit := lines_edit[0].split(';')[:2] + [data_modify(data)]) + '\n'
    file_edit.seek(editing_line_data_index * LINE_LENGTH)
    file_edit.writelines(lines_edit)
    file_edit.close()


def delete_record(rec_index):
    index = hash_func(rec_index)
    index_file_delete = open(INDEX_FILE + str(index) + ".txt", "r+")
    index_file_delete.seek(0, 2)
    f_index_length = index_file_delete.tell() // INDEX_LINE_LENGTH

    deleting_index = binary_search(index_file_delete, 0, f_index_length, rec_index)
    index_file_delete.seek(deleting_index * INDEX_LINE_LENGTH)
    deleting_line = index_file_delete.readline()
    deleting_line_data_index = int(deleting_line.split(';')[1].strip('_')) - 1

    remaining_lines = index_file_delete.read()
    index_file_delete.seek(deleting_index * INDEX_LINE_LENGTH)
    index_file_delete.write(remaining_lines)
    index_file_delete.truncate()
    index_file_delete.close()

    file_edit = open(DATA_FILE, "r+")
    file_edit.seek(deleting_line_data_index * LINE_LENGTH)
    lines_edit = file_edit.readlines()
    line_to_edit = lines_edit[0].split(';')
    line_to_edit[0] = '1'
    lines_edit[0] = ';'.join(line_to_edit)
    file_edit.seek(deleting_line_data_index * LINE_LENGTH)
    file_edit.writelines(lines_edit)
    file_edit.close()


rec1 = Record(is_deleted=0, index=4)
delete_record(6)
