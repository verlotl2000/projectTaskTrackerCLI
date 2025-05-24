<h2>Task Tracker CLI</h2>

This project is my 2nd exercise in learning Python. The project features a simple CLI todo list application. The tool allows you to add, update and remove tasks to and from a todo list. The list is persistant and is stored inside a JSON file in the application's root directory (the JSON file is automatically created upon launching the tool for the first time).

This project mainly thought me how to use the native module argparse to create a CLI tool, and also thought me alot about handling and working with python dictionaries since the JSON todo list is really just a python dictionary.

<h3>How to use:</h3>
<ol>
<li>Store the script in a new folder somewhere on your pc.</li>
<li>Cd into this folder on your terminal.</li>
<li>Run the script by running the command: python tasktracker.py followed by the commands you want to use.</li>
<li>Check out the help documentation using the following commands to learn how the tool works:
<ul>
    <li>python tasktracker.py list -h</li>
    <li>python tasktracker.py add -h</li>
    <li>python tasktracker.py update -h</li>
    <li>python tasktracker.py delete -h</li>
    <li>python tasktracker.py mark-done -h</li>
    <li>python tasktracker.py mark-notdone -h</li>
    <li>python tasktracker.py mark-inprogress -h</li>
</ul>
</ol>

Roadmap.sh project link: https://roadmap.sh/projects/task-tracker 