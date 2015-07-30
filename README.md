# Search Replace 
This script helps in mass search replace of strings in files. Following is the usage


	NAME
	    searchReplace.py 

	SYNOPSIS
		searchReplace.py [-s source] source_folder [-c csv] csv_file [-e extensions] file_extensions

	DESCRIPTION
		searchReplace.py does mass find and replace across files of given extension in a given folder.
		It parses csv file to get key value pairs, where key is replaced with value in files

	OPTIONS
	     -s source 	
	     	Location of the source folder. By default current folder is used.

	     -c csv
	     	Location of csv file which contains key value pairs. Key will be replaced by value.
	     	Key should be a valid regular expression. By default changeKV.csv is parsed in the 
	     	current location of script.

	     -e extensions
	     	Comma separated extensions of files in which find replace needs to be done. By default
	     	.jsp is used

	EXAMPLE
	     searchReplace.py -e .text
	     
	     will look for changeKV.csv file in the same folder as searchReplace.py and perform find replace
	     in files of .text extension