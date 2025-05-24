<h2>Task Tracker CLI</h2>

This project is my 2nd exercise in learning Python. The project features a simple CLI todo list application. The tool allows you to add, update and remove tasks to and from a todo list. The list is persistant and is stored inside a JSON file in the application's root directory (the JSON file is automatically created upon launching the tool for the first time).

This project mainly thought me how to use the native module argparse to create a CLI tool, and also thought me alot about handling and working with python dictionaries since the JSON todo list is really just a python dictionary.

<h3>How to use:</h3>
1. Store the script in a new folder somewhere on your pc.
2. Cd into this folder on your terminal.
3. Run the script by running the command: python tasktracker.py followed by the commands you want to use.
4. Check out the help documentation using the following commands to learn how the tool works:
    - python tasktracker.py list -h
    - python tasktracker.py add -h
    - python tasktracker.py update -h
    - python tasktracker.py delete -h
    - python tasktracker.py mark-done -h
    - python tasktracker.py mark-notdone -h
    - python tasktracker.py mark-inprogress -h


Roadmap.sh project link: https://roadmap.sh/projects/task-tracker 