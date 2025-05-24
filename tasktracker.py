import argparse
import json
import datetime
import os

# Setting some program-wide variables
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

# Create the list command
listcmd = subparsers.add_parser('list')
listcmd.add_argument('-dn', action='store_true', help='Filter by tasks with status: Done. Can be combined with -nd and/or -ip.')
listcmd.add_argument('-nd', action='store_true', help='Filter by tasks with status: Not Done. Can be combined with -dn and/or -ip.')
listcmd.add_argument('-ip', action='store_true', help='Filter by tasks with status: In Progress. Can be combined with -dn and/or -nd.')

# Create the add command
addcmd = subparsers.add_parser('add')
addcmd.add_argument('tasktoadd', help='Provide the description / task name of the task you want to add.')

# Create the update command
updatecmd = subparsers.add_parser('update')
updatecmd.add_argument('idtoupdate', help='Provide the task ID nr of the task you want to update.')
updatecmd.add_argument('-t', help="-t DESCRIPTION Lets you update the selected task's name / description to DESCRIPTION.")
updatecmd.add_argument('-dn', action='store_true', help='Updates the status of the selected task to: Done. By itself, this does the same as the mark-done command. However it is also provided as an option with the update command in case you want to also change the task status when updating its description.')
updatecmd.add_argument('-nd', action='store_true', help='Updates the status of the selected task to: Not Done. By itself, this does the same as the mark-notdone command. However it is also provided as an option with the update command in case you want to also change the task status when updating its description.')
updatecmd.add_argument('-ip', action='store_true', help='Updates the status of the selected task to: In Progress. By itself, this does the same as the mark-inprogress command. However it is also provided as an option with the update command in case you want to also change the task status when updating its description.')

# Create the delete command
deletecmd = subparsers.add_parser('delete')
deletecmd.add_argument('taskidtodelete', help='Provide the task ID nr of the task you want to delete.')

# Create the mark-done command
donecmd = subparsers.add_parser('mark-done')
donecmd.add_argument('idtodone', help='Provide the task ID nr of the task you want to mark as: Done.')

# Create the mark-notdone command
notdonecmd = subparsers.add_parser('mark-notdone')
notdonecmd.add_argument('idtonotdone', help='Provide the task ID nr of the task you want to mark as: Not Done.')

# Create the mark-inprogress command
inprogresscmd = subparsers.add_parser('mark-inprogress')
inprogresscmd.add_argument('idtoinprogress', help='Provide the task ID nr of the task you want to mark as: In Progress.')

# Parse arguments and store in variable args
args = parser.parse_args()

# Opening the todolist.json file and storing in variable todolist
if 'todolist.json' in os.listdir("."):
    with open('todolist.json', 'r') as infile:
        todolist = json.load(infile)
else:
    with open('todolist.json', 'w') as infile:
        emptyDump = json.dumps({})
        infile.write(emptyDump)
    with open('todolist.json', 'r') as infile:
        todolist = json.load(infile)
        
# Creating the list function
def list(listdone=False, listnotdone=False, listinprogress=False):
    idWidth = 5
    maxTaskWidth = 0
    for i in todolist:
        if len(todolist[i]['taskname']) > maxTaskWidth:
            maxTaskWidth = len(todolist[i]['taskname'])
    if maxTaskWidth > 30:
        taskWidth = maxTaskWidth + 5
        print(taskWidth)
    else:
        taskWidth = 30
    statusWidth = 15
    createdWidth = 25
    updatedWidth = 25
    print(f"{'ID':<{idWidth}}{'Task':<{taskWidth}}{'Status':<{statusWidth}}{'Created At':<{createdWidth}}{'Updated At':{updatedWidth}}")
    print("----------------------------------------------------------------------------------------------------------")

    dynamicDone = ''
    dynamicNotDone = ''
    dynamicInProgress = ''
    if listdone == True:
        dynamicDone = 'Done'
    if listnotdone == True:
        dynamicNotDone = 'Not Done'
    if listinprogress == True:
        dynamicInProgress = 'In Progress'
    for i in todolist:
        if todolist[i]['taskstatus'] == dynamicDone or todolist[i]['taskstatus'] == dynamicNotDone or todolist[i]['taskstatus'] == dynamicInProgress:
            print(f"{i:<{idWidth}}{todolist[i]['taskname']:<{taskWidth}}{todolist[i]['taskstatus']:<{statusWidth}}{todolist[i]['createdat']:<{createdWidth}}{todolist[i]['updatedat']:<{updatedWidth}}")
    
    optionsTrue = 0
    for i in [listdone, listnotdone, listinprogress]:
        if i == True:
            optionsTrue += 1
    if optionsTrue == 0:
        for i in todolist:
            print(f"{i:<{idWidth}}{todolist[i]['taskname']:<{taskWidth}}{todolist[i]['taskstatus']:<{statusWidth}}{todolist[i]['createdat']:<{createdWidth}}{todolist[i]['updatedat']:<{updatedWidth}}")

# Creating the add function
def add(task):
    lastTaskId = len(todolist.keys())
    todolist[lastTaskId + 1] = {"taskname":task, "taskstatus":"Not Done", "createdat":now, "updatedat":""}
    
    addDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(addDump)

# Creating the update function
def update(id, task=None, done=False, notdone=False, inprogress=False):
    if int(id) > len(todolist):
        print('Please use a valid / existing task id when running update, the id you provided was not valid or does not exist.')
        return
    
    optionsTrue = 0
    for i in [done, notdone, inprogress]:
        if i == True:
            optionsTrue += 1
    
    if optionsTrue > 1:
        print("You have selected at least 2 of the following options: -dn, -nd or -ip which are conflicting instructions, please choose either one.")
        return
    
    if task == None and done == False and notdone == False and inprogress == False:
        print("Please provide either a task name or a task status to update. You have provided a task id, but nothing to update under that id.")
        return

    if task is not None:
        todolist[id].update({"taskname":task, "updatedat":now})
        print(f"Task {id} updated to: '{task}'.")

    if done == True and notdone == False and inprogress == False:
        todolist[id].update({"taskstatus":"Done", "updatedat":now})
        print(f"Task {id} updated to status: 'Done'.")

    if notdone == True and done == False and inprogress == False:
        todolist[id].update({"taskstatus":"Not Done", "updatedat":now})
        print(f"Task {id} updated to status: 'Not Done'.")

    if inprogress == True and done == False and notdone == False:
        todolist[id].update({"taskstatus":"In Progress", "updatedat":now})
        print(f"Task {id} updated to status: 'In Progress'")

    updateDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(updateDump)

# Creating the delete function
def delete(id):
    global todolist
    if int(id) > len(todolist):
        print('Please use a valid / existing task id when running delete, the id you provided was not valid or does not exist.')
        return

    del todolist[id]
    todolist = {str(index + 1): value for index, value in enumerate(todolist.values())}
    
    deleteDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(deleteDump)

# Creating the mark-done function
def markdone(id):
    if int(id) > len(todolist):
        print('Please use a valid / existing task id when running mark-done, the id you provided was not valid or does not exist.')
        return
    
    todolist[id].update({"taskstatus":"Done", "updatedat":now})
    print(f"Task {id} updated to status: 'Done'.")
    
    doneDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(doneDump)

# Creating the mark-notdone function
def marknotdone(id):
    if int(id) > len(todolist):
        print('Please use a valid / existing task id when running mark-notdone, the id you provided was not valid or does not exist.')
        return
    
    todolist[id].update({"taskstatus":"Not Done", "updatedat":now})
    print(f"Task {id} updated to status: 'Not Done'.")
    
    notDoneDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(notDoneDump)

# Creating the mark-inprogress function
def markinprogress(id):
    if int(id) > len(todolist):
        print('Please use a valid / existing task id when running mark-inprogress, the id you provided was not valid or does not exist.')
        return
    
    todolist[id].update({"taskstatus":"In Progress", "updatedat":now})
    print(f"Task {id} updated to status: 'In Progress'.")
    
    inprogressDump = json.dumps(todolist)
    with open('todolist.json', 'w') as outfile:
        outfile.write(inprogressDump)        
    
# Calling the necessary function
if args.command == 'add':
    tasktoadd = args.tasktoadd
    add(tasktoadd)
elif args.command == 'list':
    listdone = args.dn
    listnotdone = args.nd
    listinprogress = args.ip
    list(listdone, listnotdone, listinprogress)
elif args.command == 'delete':
    taskidtodelete = args.taskidtodelete
    delete(taskidtodelete)
elif args.command == 'update':
    idtoupdate = args.idtoupdate
    optionaltask = args.t
    optionaldone = args.dn
    optionalnotdone = args.nd
    optionalinprogress = args.ip
    update(idtoupdate, optionaltask, optionaldone, optionalnotdone, optionalinprogress)
elif args.command == 'mark-done':
    idtodone = args.idtodone
    markdone(idtodone)
elif args.command == 'mark-notdone':
    idtonotdone = args.idtonotdone
    marknotdone(idtonotdone)
elif args.command == 'mark-inprogress':
    idtoinprogress = args.idtoinprogress
    markinprogress(idtoinprogress)
