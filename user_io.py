#! /usr/bin/python3

__doc__ = """

User Input/Output Toolkit

This is a collection of various User interaction I/O functions useful in other programs

Included Functions:
    help                - display this docstring
    choose_from_list    - from a list, get user response in int or str form (w/defaults)
    query_yes_no        - from a question, get user response as True/False (w/defaults)
    progress_bar        - progress bar to display loop progress to terminal output
    valid_filepath      - checks if a string is a valid path to a file
    valid_dirpath       - checks if a string is a valid path to a dir
    valid_csvpath       - checks if a string is a valid path to a CSV
    list_folders        - list the folders located in a given directory

Usage:
    from user_io import <function>

See README.md for complete details

"""
__author__ = "Various, compiled by epopisces"
__date__ = "2020.11.03"
__version__ = 0.1

import sys, os

def help():
    print(__doc__)

def choose_from_list(question, options, default='1', output='str'):
    """
    Author: epopisces (https://github.com/epopisces)
    
    Ask user which from a list is the correct option and return their answer.
    @params:
        question    - Required  : question to be used as prompt for user (Str)
        options     - Required  : list of strings presented to the user.  Will be given numerical representatives ([Str])
        default     - Optional  : presumed answer when user provides no entry (Str or Int)
                                    Must be a number <= number of list items starting at 1, eg "1"
                                    Even though arrays start at 0, users don't 
        output      - Optional  : format of the returned value.  Options are 'str' or 'int' (Str)

    If output='str', returns the selected string from the list: if output='int', returns the position of the selected item
    """
    if default is None:
        prompt = " "
    elif isinstance(default, str) or isinstance(default, int):
        prompt = " [default: '" + str(default) + "'] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)
    
    while True:
        sys.stdout.write(question + prompt + "\n")
        for num, name in enumerate(options, start=1):
            sys.stdout.write(str(num) + ". " + name + "\n")
        choice = input()
        if choice.isnumeric():
            choice = int(choice)
        if isinstance(choice, str):
            choice = choice.lower()

        if default is not None and choice == '':
            return default
        elif isinstance(choice, int) and choice <= num:
            if output == 'int':
                return choice
            else:
                return options[choice]
        elif isinstance(choice, str) and choice in options:
            if output == 'str':
                return choice
            else:
                return options.index(choice)
        else:
            sys.stdout.write("Please respond with a valid number or write out the full string\n")

def query_yes_no(question, default="yes"):
    """
    Author: fmark
    Edited by: Jake
    https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input

    Ask a yes/no question via raw_input() and return their answer.

    @params:
        question    - Required  : string question to be used as prompt for user (Str)
        default     - Optional  : the default answer, can be "yes", "no", or "". defaults to "yes" (Str)

    Returns True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " + "(or 'y' or 'n').\n")

def progress_bar (
    iteration,
    total,
    prefix = '',
    suffix = '',
    decimals = 1,
    length = 100,
    fill = '█',
    printEnd = "\r\n"
    ):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        
    Example Usage:
    l = len(objs_list)
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd="\r\n")
    for i, obj in enumerate(list):
            <do something with obj>
            time.sleep(0.01)
            printProgressBar(i + 1, l, prefix = "Progress:", suffix = "Complete", length = 50, printEnd="\r\n")

    Author: Greenstick @ https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    
    # Print New Line on Complete
    if iteration == total:
        print()

def valid_filepath(filepath):
    """
    Author: nikhilaggarwal3 on geeksforgeeks.com (https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/)
    Modified by: epopisces (https://github.com/epopisces)
    
    Validate whether a filepath is valid
    @params:
        filepath    - Required  : The filepath to validate (Str)

    Will output either the filepath or False
    """
    filedir = os.path.dirname(filepath)
    if not os.path.isdir(filedir):
        #logger.error(f"Folder not found at '{filedir}'.")
        return False
    if not os.path.isfile(filepath):
        #logger.error(f"File not found at '{filepath}'.")
        return False
    return filepath

def valid_dirpath(dirpath):
    """
    Author: nikhilaggarwal3 on geeksforgeeks.com (https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists-2/)
    Modified by: epopisces (https://github.com/epopisces)
    
    Validate whether a directory path is valid

    @params:
        dirpath     - Required  : The filepath to validate (Str)

    Will output either the dirpath or False
    """
    filedir = os.path.dirname(dirpath)
    if not os.path.isdir(filedir):
        #logger.error(f"Folder not found at '{filedir}'.")
        return False
    return dirpath

def valid_csvpath(filepath):
    import csv
    """
    Author: gotgenes on stackoverflow.com (https://stackoverflow.com/questions/2984888/check-if-file-has-a-csv-format-with-python)
    
    Validate whether a file is a valid CSV file

    @params:
        filepath     - Required  : The path to the file in question (Str)

    Will output either True or False
    """
    if filepath:
        with open(filepath, 'rb') as csv_fileh:
            try:
                dialect = csv.Sniffer().sniff(csv_fileh.read(1024))
                csv_fileh.seek(0)
                return True
            except csv.Error:
                return False
    else:
        return False

def list_folders(dirpath):
    """
    Author: Blair Conrad at stackoverflow.com (https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory)
    Modified by: epopisces (https://github.com/epopisces)
    
    Returns a list of directories in a given path (not recursively)

    @params:
        dirpath     - Required  : The filepath to validate,eg. 'C:\\Temp' (Str)

    Will output a list object (will be empty if there are no directories found)
    """
    if valid_dirpath(dirpath):
        dir_list = next(os.walk(dirpath))[1]
        print(dir_list)
        return dir_list
    else:
        return False

if __name__ == '__main__':
    print("Module not intended to be executed solo.  Use tests.py to see test functions")
