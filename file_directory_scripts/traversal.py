import os
import platform


def getFolderSize(folder):
	total_size = os.path.getsize(folder)
	for item in os.listdir(folder):
		itempath = os.path.join(folder, item)
		print itempath
		try:
			if os.path.isfile(itempath):
				total_size += os.path.getsize(itempath)
			elif os.path.isdir(itempath):
				total_size += getFolderSize(itempath)
		except:
			pass
	return total_size
	
def gssd(root_path, desired_size):
    os.chdir(root_path)
	if platform.system == "nt"
		if getFolderSize(root_path) < desired_size:
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
	elif platform.system == "posix":
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
	else: 
				if getFolderSize(root_path) < desired_size:
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
	
print gssd("D:/", 1024*1024*1024)
print 1024*1024*1024
print getFolderSize(gssd("D:/", 1024*1024*1024))