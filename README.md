#**Project**'AirBnB clone - The console'
 <p><img src="https://github.com/matternstsr/holbertonschool-AirBnB_clone/blob/42b75e0b511b2480417c468073c834a7c9385dfe/hbnb.jpg" alt="" loading='lazy' style="" /></p>

## Introduction
> This README is for the AirBnB clone - The console at Holberton. It countains the requirements, list of files, and Examples on how use.

### Requirements
- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using python3
- First line of all files should be '#!/usr/bin/python3'
- Repo should contain a README
- Code should use pycodestyle (version 2.7.*)
- All files must be executable
- Length of files will be tested with wc
- All modules should be documented
- All classes should be documented
- All functions should be documented
- Python 3.4.3 or later

#### Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start with test_
- our file organization in the tests folder should be the same as your project: ex: for models/base.py, unit tests must be in: tests/test_models/test_base.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base.py

### Repo Files
| **File** | *__Description__* |
|----------|----------------:|
|tests| Contains all Unit Test files|
|test_engine| Contains an init file and file_storage.py|
|test_models| Test files for all models|
|test_amenity.py| Contains Unit Tests for Class amenity|
|test_base_model| Contains Unit Tests for Class base_model|
|test_city.py| Contains Unit Tests for Class city|
|test_place.py| Contains Unit Tests for Class place|
|test_review.py| Contains Unit Tests for Class review|
|test_state.py| Contains Unit Tests for Class state|
|test_user.py| Contains Unit Tests for Class user|
|models| Contains all files for models|
|engine| Contains file_storage.py file|
|amenity.py| Contains all attribute and methods for Class amenity|
|base_models.py| Contains all attribute and methods for Class base_model|
|city.py|Contains all attribute and methods for Class city|
|review.py| Contains all attribute and methods for Class review.py|
|state.py| Contains all attribute and methods for Class state|
|user.py| Contains all attribute and methods for Class user|
|console.py| File for creating and running an interactive console|
|AUTHORS| File containing authors of the project|
|commands.txt| File containing commands that run using the console in Non-interactive mode|



### Interactive mode

To run the console in *interactive* mode type:

```$ ./console.py```

This prompt will appear:

```(hbnb) ```

where you can type commands and get output. For example:

```bash
(hbnb) all
["[User] (00155f6d-b153-4740-bb49-a00abf2863b6) {'id': '00155f6d-b153-4740-bb49-a00abf2863b6', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451703), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451710), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (8d277805-bae6-4279-8e5e-7c80ca608e02) {'id': '8d277805-bae6-4279-8e5e-7c80ca608e02', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451946), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451951), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

### Non-interactive mode

The same commands can be used to run non-interactive mode with some modifications will produce the same results as above:

```bash
$ echo "all" | ./console.py
(hbnb) ["[User] (00155f6d-b153-4740-bb49-a00abf2863b6) {'id': '00155f6d-b153-4740-bb49-a00abf2863b6', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451703), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451710), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (8d277805-bae6-4279-8e5e-7c80ca608e02) {'id': '8d277805-bae6-4279-8e5e-7c80ca608e02', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451946), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451951), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

You can also use a file that contains the commands you want to run:
```bash
$ cat commands.txt
all User
```

```bash
$ cat commands.txt | ./console.py
(hbnb) ["[User] (00155f6d-b153-4740-bb49-a00abf2863b6) {'id': '00155f6d-b153-4740-bb49-a00abf2863b6', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451703), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451710), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (8d277805-bae6-4279-8e5e-7c80ca608e02) {'id': '8d277805-bae6-4279-8e5e-7c80ca608e02', 'created_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451946), 'updated_at': datetime.datetime(2023, 10, 10, 11, 3, 21, 451951), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```

### Storage

Instances of classes are serialized into a JSON string format and stored in a file named "file.json" located in the project's root directory. Any changes made to these objects, whether they are additions, deletions, or updates, are automatically reflected in this JSON file. Essentially, this JSON file acts as a basic database, allowing the data to persist and be accessible across different sessions or executions of the program.

### Tests
[unittest module].(https://docs.python.org/3.4/library/unittest.html)

Testing is essential when developing a robust program. That's why we've incorporated a comprehensive testing suite using Python's 

To run the entire unittest suite do this command from the root directory:

If you want to run tests individually, an example would be:

```bash
$ python3 -m unittest tests/test_models/test_base_model.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK
```

```bash
$ python3 -m unittest discover tests
............................................................
----------------------------------------------------------------------
Ran 60 tests in 0.017s

OK
```

### Supported Commands

Name | Description | Use
-------- | ----------- |-------- |
help | Displays help information for a command | help [command]
quit | Exits/quits the program | quit
EOF | Exits the program when files are passed into the program | N/A
create | Creates a new instance of a specified class | create [class_name]
show | Prints the string representation of an instance | show [class_name] [id]
destroy | Deletes an instance | destroy [class_name] [id]
all | Prints the string representation of all instances of a class| all or all [class_name] [id]
update | Adds or modifies attributes of an instance | update [class_name] [id] [attribute] [value]

