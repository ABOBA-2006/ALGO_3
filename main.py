AMOUNT_OF_BLOCKS = 10
LENGTH_OF_BLOCK = 1000
DATA_FILE = "data_file.txt"
INDEX_FILE = "index_file"


class Record:
    def __init__(self, is_deleted:int, index:int, data:str):
        self.is_deleted = is_deleted
        self.index = index
        self.data = data


def create_files():
    for i in range(AMOUNT_OF_BLOCKS):
        f = open(INDEX_FILE + str(i) + ".txt", "x")
        f.close()


def hash_func(index):
    return index // LENGTH_OF_BLOCK


def get_index(line_to_compare:str):
    index_line = int(line_to_compare.split(";")[1].strip())
    return index_line


def add_record(record):
    f = open(DATA_FILE, "a")
    f.write(str(record.is_deleted) + ';' + str(record.index) + ';' + record.data + '\n')
    f.close()

    hash_result = hash_func(record.index)
    f = open(INDEX_FILE + str(hash_result) + ".txt", "r")
    new_record_pos_found = False
    current_pos = 0
    lines = []
    for line in f:
        lines.append(line)

        if not new_record_pos_found:
            line_index = get_index(line)
            current_pos += 1
            if record.index < line_index:
                current_pos -= 1
                new_record_pos_found = True
    f.close()

    lines.insert(current_pos, str(record.is_deleted) + ';' + str(record.index) + ';' + record.data + '\n')
    f = open(INDEX_FILE + str(hash_result) + ".txt", "w")
    f.writelines(lines)
    f.close()



rec1 = Record(is_deleted=0, index=2001, data="ABOBA")
add_record(rec1)