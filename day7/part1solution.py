file = open("input.txt").read().split("\n")

directories = {}

current_directory_tree = [directories]
current_directory = directories

for line in file:
    if line.startswith('$'):
        parts = line.split(' ')
        if parts[1] == 'cd':
            if parts[2] == '..':
                current_directory = current_directory_tree.pop()
            elif parts[2] != '/':
                if parts[2] not in current_directory:
                    current_directory[parts[2]] = {}
                current_directory_tree.append(current_directory)
                current_directory = current_directory[parts[2]]
    else:
        line_info = line.split(' ')
        if line_info[0] != 'dir':
            current_directory[line_info[1]] = int(line_info[0])


def calculate_dir_sizes(dir_name, directory):
    sizes = []
    current_dir_size = 0
    for item in directory:
        if type(directory[item]) is dict:
            inner_size = calculate_dir_sizes(item, directory[item])
            sizes.extend(inner_size[0])
            current_dir_size = current_dir_size + inner_size[1]
        else:
            current_dir_size = current_dir_size + directory[item]
    sizes.append({dir_name: current_dir_size})
    return [sizes, current_dir_size]


total = 0
sizes = calculate_dir_sizes('/', directories)[0]
for element in sizes:
    size = list(element.values())[0]
    if size <= 100000:
        total = total + size

print(total)