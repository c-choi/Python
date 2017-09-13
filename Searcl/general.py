import os


# each website will be a separate project

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project' + directory)
        os.makedirs(directory)


# create queue (for all the sites not crawled) and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# create a new file (w = write)
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# add data onto an existing file (a = append , \n = new line)
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# delete the contents of a file (open new file to write and do nothing to delete contents)
def delete_file_contents(path):
    open(path, 'w').close()

# speeding up crawler by storing data in set by creating a unique element to remove duplicates in queue and written file


# read a file and convert each line to set items (rt = read text)
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results


#iterate through a set, each item will be a new line in the file (links = set)
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l + '\n')
