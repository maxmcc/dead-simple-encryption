import os


def gssd(root_path, desired_size):
    os.chdir(root_path)
    if os.path.getsize(root_path) < desired_size:
        return None

    children = map(lambda child: os.path.abspath(child), os.listdir(root_path))
    no_dots = filter(lambda child: os.path.basename(child)[0] is not '.', children)
    no_files = filter(lambda child: os.path.isdir(child), no_dots)

    def cmp_by_size(a, b):
        a_size = os.path.getsize(a)
        b_size = os.path.getsize(b)
        return cmp(a_size, b_size)

    sorted_children = sorted(no_files, cmp=cmp_by_size)
    for child in sorted_children:
        if gssd(child, desired_size) is not None:
            return child

    return root_path