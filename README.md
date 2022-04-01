# User I/O Tools

> Helper scripts for Python projects related to user input or output

## Table of Contents
1. Python Module Function Listing
    1. [progress_bar](#p#rogress_bar())
    2. [choose_from_list](##choose_from_list())
    3. [query_yes_no](##query_yes_no())
    4. [validation functions](##validation-functions)

![](user_io.png) 
> TODO replace the above with fontawesome

## Getting Started

### Prerequisites

- Python 3

### Installation

There is no formal installation process at this time, but using [git subtrees](https://www.atlassian.com/git/tutorials/git-subtree) is strongly recommended.  Unfortunately there is no 'helper' integration for git subtrees in VS Code, so using the actual git commands are necessary:

```bash
git subtree add --prefix tools/user_io https://github.com/GitHub_Org/tools_user_io main --squash
git fetch https://github.com/GitHub_Org/tools_user_io main

# Breaking the above down, the following command creates the subtree and the connection to the remote repo
'''
git subtree add --prefix <dest-path> <source-repo> <branch> --squash
    --prefix <path>         specify the destination folder (relative to current working directory).
    <source-repo>           the repository that is being pulled from
    <branch>                branch to be pulled (usually 'main', may be 'master' if migrated from outside GitHub)
    --squash                optional but recommended command to discard the commit history of the source repo
'''
#The following command fetches the content of that repo so it will be available for use
'''
git fetch <source-repo> <branch>
    <source-repo>           the repository that is being pulled from
    <branch>                branch to be pulled (usually 'main', may be 'master' if migrated from outside GitHub)
'''
```

But what if the remote tool repo gets updated?  Pulling the latest changes is super easy: just use the same command above with 'git subtree add' instead of 'git subtree pull':
```
git subtree pull --prefix tools/user_io https://github.com/GitHub_Org/tools_user_io main --squash
```

Alternately git submodules can also be used; however, git submodules are not as easy to maintain and keep updated.  The recommendation is only to use git submodules if the tools repo is also going to be developed as part of the project, instead of just used as a static library by the main project.

The differences between git subtrees and git submodules are described in depth [in this article](https://martowen.com/2016/05/01/git-submodules-vs-git-subtrees/#:~:text=The%20simplest%20way%20to%20think,specific%20commit%20in%20another%20repository.&text=Subtrees%20are%20easier%20to%20pull,copies%20of%20the%20original%20repository).

# user_io Module Function Listing
Each of the below code excerpts assume you are using the repo as a subtree as described above.  Note this will require creating a empty `__init__.py` file in the 'tools' folder if there is not one present already in order for Python's import function to traverse the directories to get to the tools.

## progress_bar()

### Capabilities
* Displays a progress bar during operations when a loop is wrapped in the provided function

### Usage

```python
from tools.user_io import progress_bar

'''@params:
    iteration   - Required  : current iteration (Int)
    total       - Required  : total iterations (Int)
    prefix      - Optional  : prefix string (Str)
    suffix      - Optional  : suffix string (Str)
    decimals    - Optional  : positive number of decimals in percent complete (Int)
    length      - Optional  : character length of bar (Int)
    fill        - Optional  : bar fill character (Str)
    printEnd    - Optional  : end character (e.g. "\r", "\r\n", or "") (Str)
'''

objs_list = [obj1, obj2, obj3]
l = len(objs_list)
progress_bar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50, printEnd = '') # initial empty prog bar

for i, obj in enumerate(objs_list):     # any type of loop so long as counter is included
    obj.any_function()  # include any actions here
    time.sleep(0.01)    # gives the visual time to render
    progress(i + 1, l, prefix = "Progress:", suffix = "Complete", length = 50, , printEnd = '')
```

## query_yes_no()

### Capabilities
Returns `True` or `False` based on question, with defaults and error handling

### Usage

```python
from tools.user_io import query_yes_no

'''@params:
    question    - Required  : string question to be used as prompt for user (Str)
    default     - Optional  : the default answer, can be "yes", "no", or "". defaults to "yes" (Str)
'''
if user_io.query_yes_no("Are you sure you want to do this thing?"):
    do_the_thing()
```

## choose_from_list()

### Capabilities
Asks user a question with options, default, returns str or int as desired

### Usage
```python
from tools.user_io import choose_from_list

'''@params:
    question    - Required  : question to be used as prompt for user (Str)
    options     - Required  : list of strings presented to the user.  Will be given numerical representatives ([Str])
    default     - Optional  : presumed answer when user provides no entry (Str or Int)
                                Must be a number <= number of list items starting at 1, eg "1"
                                Even though arrays start at 0, users don't 
    output      - Optional  : format of the returned value.  Options are 'str' or 'int' (Str)
'''

choice = user_io.choose_from_list("Is this a question?", ["Yes", "No", "Maybe", "Quit"], output='int')
    if choice == 1:
        print("Sensible")
    elif choice == 2:
        print("There is no question")
    elif choice == 3:
        print("Indecisive much?")
    elif choice == 4:
        sys.exit('User quit the application')
```

## validation functions

This is a variety of functions that can be used to validate various input or output formats or attributes.

### Capabilities
* valid_filepath - checks to see if a string represents a valid filepath on the current system (returns filepath or False)
* valid_dirpath - checks to see if a string represents a valid directory on the current system (returns dirpath or False)
* valid_csv - checks to see if a string represents a valid CSV file on the current system (returns True or False)

### Usage
```python
from tools.user_io import valid_{thing_to_validate}

'''@params:
    thing_to_validate   - Required  : question to be used as prompt for user (Str)

'''

if valid_csv(valid_filepath(csv_filepath)): # if a valid path, and if a valid CSV
    with open(csv_filepath, 'rb') as csv_file:
        reader = csv.DictReader(csv_file, delimeter=',')
        # do things with the rows here
else:
    print("Invalid CSV file or filepath, please try again.")

```

## Release History
* 0.1.1
    * validation functions added
* 0.1.0
    * The first proper release with documentation uploaded to Github. 
    * progress_bar - stable, documented
    * choose_from_list 
    * query_yes_no
* 0.0.1
    * Work in progress, local dev

## Metadata

### Authors

* [**epopisces**](https://github.com/epopisces/) - Compiled the module initially.

For a full list of contributors, see each function's docstring

### Acknowledgments

* [epopisces](https://github.com/epopisces) created the project template and boilerplate code used for this project
* Thanks to [PurpleBooth](https://gist.github.com/PurpleBooth/) & [dbader](https://github.com/dbader/readme-template) for the README Template
