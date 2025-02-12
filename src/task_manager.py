import json
import os
from .utils import getcurrenttime, validatedescription, validatestatus, ensuredirectory, printerror

TASKSFILE = "data/tasks.json"

def initializetasks():
    ensuredirectory("data")
    if not os.path.exists(TASKSFILE):
        with open(TASKSFILE, "w") as f:
            json.dump({"tasks": []}, f, indent=2)

def readtasks():
    try:
        with open(TASKSFILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        initializetasks()
        return {"tasks": []}

def savetasks(data):
    with open(TASKSFILE, "w") as f:
        json.dump(data, f, indent=2)

def addtask(description):
    try:
        description = validatedescription(description)
        data = readtasks()
        currid = 1
        if data["tasks"]:
            currid = max(task["id"] for task in data["tasks"]) + 1

        newtask = {
            "id": currid,
            "description": description,
            "status": "todo",
            "created": getcurrenttime(),
            "updated": getcurrenttime(),
        }

        data["tasks"].append(newtask)
        savetasks(data)
        return currid
    except Exception as e:
        printerror(f"Error adding task: {str(e)}")
        return None

def updatetask(taskid, newdescription):
    try:
        newdescription = validatedescription(newdescription)
        data = readtasks()
        for task in data["tasks"]:
            if task["id"] == taskid:
                task["description"] = newdescription
                task["updated"] = getcurrenttime()
                savetasks(data)
                return True
        return False
    except Exception as e:
        printerror(f"Error updating task: {str(e)}")
        return False

def deletetask(taskid):
    try:
        data = readtasks()
        data["tasks"] = [task for task in data["tasks"] if task["id"] != taskid]
        savetasks(data)
        return True
    except Exception as e:
        printerror(f"Error deleting task: {str(e)}")
        return False

def changetaskstatus(taskid, newstatus):
    try:
        newstatus = validatestatus(newstatus)
        data = readtasks()
        for task in data["tasks"]:
            if task["id"] == taskid:
                task["status"] = newstatus
                task["updated"] = getcurrenttime()
                savetasks(data)
                return True
        return False
    except Exception as e:
        printerror(f"Error changing task status: {str(e)}")
        return False

def listtask(status=None):
    try:
        data = readtasks()
        if status:
            return [task for task in data["tasks"] if task["status"] == status]
        return data["tasks"]
    except Exception as e:
        printerror(f"Error listing tasks: {str(e)}")
        return None

def gettask(taskid):
    try:
        data = readtasks()
        for task in data["tasks"]:
            if task["id"] == taskid:
                return task
        return None
    except Exception as e:
        printerror(f"Error getting task: {str(e)}")
        return None