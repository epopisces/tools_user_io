import time, sys, csv

from user_io import choose_from_list
from user_io import query_yes_no
from user_io import progress_bar
from user_io import list_folders
from user_io import valid_dirpath, valid_filepath, valid_csv



class TestClass:
    generic_attrib = 'totally generic'

    def wait_a_bit(self, length):
        time.sleep(length)

def test_query_yes_no():
    if query_yes_no("Are you sure you want this to print 'Supercalifragilisticexpealidocious'?"):
        print("Supercalifragilisticexpealidocious")
    return

def test_choose_from_list():
    choice = choose_from_list("How do you like your eggs?", ["Sunny-side up", "Scrambled", "Boiled", "Quit"],default='2',output='int')
    if choice == 1:
        print("Glass half full, eh?")
    elif choice == 2:
        print("The generic option")
    elif choice == 3:
        print("You monster!")
    elif choice == 4:
        sys.exit('User quit the application')
    return

def test_progress_bar():
    objs_list = []
    
    for _ in range(10):
        obj = TestClass()
        objs_list.append(obj)

    l = len(objs_list)
    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, obj in enumerate(objs_list):
        obj.wait_a_bit(0.25)
        time.sleep(0.01)
        progress_bar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
    return

def test_progress_bar_inline():
    objs_list = []
    
    for _ in range(10):
        obj = TestClass()
        objs_list.append(obj)

    l = len(objs_list)
    progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd = '')
    for i, obj in enumerate(objs_list):
        obj.wait_a_bit(0.25)
        time.sleep(0.01)
        progress_bar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd = '')
    
    return

def test_progress_bar_inline_for_csv(csv_filepath):
    with open(csv_filepath, 'r') as f:
        l = sum(1 for row in f) - 1 # use generator cuz len() doesn't work on CSV objects
        f.seek(0)                   # return to the start of the file for following ops
        csv_reader = csv.reader(f, delimiter=',')
        progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd = '')
        for j, row in enumerate(csv_reader):
            time.sleep(0.1)
            progress_bar(j, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd = '')
    return

def test_validation_functions(csv_filepath):
    if valid_csv(valid_filepath(csv_filepath)):
        with open(csv_filepath, 'rb') as csv_file:
            reader = csv.DictReader(csv_file, delimeter=',')
            # do things with the rows here
        
    else:
        print(f"{csv_filepath} is not a valid CSV file or path, please try again.")

    return

def list_folders_test(dirpath):
    folder_list = list_folders(dirpath)
    return folder_list


print()
print("A progress bar that advances lines")
test_progress_bar()

print()
print("A progress bar that advances inline")
test_progress_bar_inline()

print()
print("A progress bar that advances inline while doing ops on a CSV row")
csv_filepath = 'C:/Temp/example.csv'
test_progress_bar_inline_for_csv(csv_filepath)

print()
test_choose_from_list()

print()
test_validation_functions('C:/Temp/example.csv')

dirpath = 'C:\\Temp\\Certificates'
folder_list = test_list_folders(dirpath)
print(folder_list)
