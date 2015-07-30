#!/usr/bin/python
import sys, os, csv, re, getopt

# constants
##################################################
TMP_FILE_EXTENSION = '.tmp'
DEFAULT_FILE_EXTENSIONS = '.jsp,'
DEFAULT_CSV_FILE_NAME = 'changeKV.csv'
DEFAULT_SOURCE_FOLDER = '.'

def process_csv(csv_file):
	search_replace_array = []
	with open(csv_file, 'rU') as f:
		reader = csv.reader(f)
		for row in reader:
			regex = re.compile(row[0])
			search_replace_array.append([regex, row[1]])
	return search_replace_array
    	
def process_line(line, search_replace_array):
	for search_replace_item in search_replace_array:
		line = re.sub(search_replace_item[0],search_replace_item[1], line)
	return line


def process_file(path, search_replace_array):
	with open(path) as f:
		tmp_path = path + ".tmp"
		f_out = open(tmp_path, "w")
		for l in f:
			l_out = process_line(l, search_replace_array)
			f_out.write(l_out)
		f_out.close()
		os.rename(tmp_path, path)


def process_dir(path, csv_file_name, file_extensions):
	search_replace_array = process_csv(csv_file_name)
	for dirpath, dirnames, filenames in os.walk(path):
		for fname in filenames:
			fext = os.path.splitext(fname)[1]
			if fext != '' and fext in file_extensions.split(','):
				fpath = os.path.join(dirpath, fname)
				print '####### Processing file ' + fpath
				process_file(fpath, search_replace_array)

def main(argv):
	source_folder = DEFAULT_SOURCE_FOLDER
	csv_file_name = DEFAULT_CSV_FILE_NAME
	file_extensions = DEFAULT_FILE_EXTENSIONS
	try:
		opts, args = getopt.getopt(argv,"hs:c:e:",["source=","csv=","extensions="])
	except getopt.GetoptError:
		print 'searchReplace.py -s <source folder> -c <csv file> -e <comma separated file extensions>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'searchReplace.py -s <source folder> -c <csv file> -e <comma separated file extensions>'
			sys.exit()
		elif opt in ('-s', '--source'):
			source_folder = arg
		elif opt in ('-c', '--csv'):
			csv_file_name = arg
		elif opt in ('-e', '--extensions'):
			file_extensions = arg
	process_dir(source_folder, csv_file_name, file_extensions)

main(sys.argv[1:])