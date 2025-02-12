import sys
import argparse
from datetime import datetime, UTC
from src import task_manager
from src.utils import getcurrenttime, formatstatus, printerror, printsuccess, CURRENTUSER


def createparser():
    parser = argparse.ArgumentParser(
        description=f'TaskTracker CLI - User: {CURRENTUSER}',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    addparser = subparsers.add_parser("add", help="Add a new task")
    addparser.add_argument("description", type=str, nargs="+", help="Task description")

    updateparser = subparsers.add_parser("update", help="Update a task")
    updateparser.add_argument("taskid", type=int, help="Task ID")
    updateparser.add_argument("description", type=str, nargs="+", help="New task description")

    deleteparser = subparsers.add_parser("delete", help="Delete a task")
    deleteparser.add_argument("taskid", type=int, help="Task ID")

    markinprogress = subparsers.add_parser("inprogress", help="Mark a task as in progress")
    markinprogress.add_argument("taskid", type=int, help="Task ID")

    markdone = subparsers.add_parser("done", help="Mark a task as done")
    markdone.add_argument("taskid", type=int, help="Task ID")

    listparser = subparsers.add_parser("list", help="List tasks")
    listparser.add_argument("--status", type=str, choices=["todo", "inprogress", "done"],
                            help="Filter tasks by status")

    return parser


def formattask(task):
    status = formatstatus(task["status"])
    return (f"ID: {task['id']} | Status: {status} | "
            f"Description: {task['description']} | "
            f"Created: {task['created']} | Updated: {task['updated']}")


def printtaskcount(tasks, status=None):
    total = len(tasks)
    if total == 0:
        print("No tasks found")
        return

    statuscounts = {
        "todo": len([t for t in tasks if t["status"] == "todo"]),
        "inprogress": len([t for t in tasks if t["status"] == "inprogress"]),
        "done": len([t for t in tasks if t["status"] == "done"])
    }

    print(f"\nTotal tasks: {total}")
    if not status:
        print(f"Tasks todo: {statuscounts['todo']}")
        print(f"Tasks in progress: {statuscounts['inprogress']}")
        print(f"Tasks done: {statuscounts['done']}")


def handleerror(message):
    printerror(message)
    sys.exit(1)


def main():
    parser = createparser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    task_manager.initializetasks()

    try:
        if args.command == "add":
            description = " ".join(args.description)
            taskid = task_manager.addtask(description)
            if taskid:
                printsuccess(f"Task added successfully (ID: {taskid})")
            else:
                handleerror("Failed to add task")

        elif args.command == "update":
            description = " ".join(args.description)
            task = task_manager.gettask(args.taskid)
            if not task:
                handleerror(f"Task with ID {args.taskid} not found")

            if task_manager.updatetask(args.taskid, description):
                printsuccess(f"Task {args.taskid} updated successfully")
            else:
                handleerror(f"Failed to update task {args.taskid}")

        elif args.command == "delete":
            task = task_manager.gettask(args.taskid)
            if not task:
                handleerror(f"Task with ID {args.taskid} not found")

            if task_manager.deletetask(args.taskid):
                printsuccess(f"Task {args.taskid} deleted successfully")
            else:
                handleerror(f"Failed to delete task {args.taskid}")

        elif args.command == "inprogress":
            if task_manager.changetaskstatus(args.taskid, "inprogress"):
                printsuccess(f"Task {args.taskid} marked as in progress")
            else:
                handleerror(f"Failed to mark task {args.taskid} as in progress")

        elif args.command == "done":
            if task_manager.changetaskstatus(args.taskid, "done"):
                printsuccess(f"Task {args.taskid} marked as done")
            else:
                handleerror(f"Failed to mark task {args.taskid} as done")

        elif args.command == "list":
            tasks = task_manager.listtask(args.status)
            if tasks:
                print("\nTask List:")
                print("=" * 100)
                for task in tasks:
                    print(formattask(task))
                print("=" * 100)
                printtaskcount(tasks, args.status)
            else:
                print("\nNo tasks found.")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        handleerror(str(e))


if __name__ == "__main__":
    print("\nTask Tracker CLI")
    print(f"Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): {getcurrenttime()}")
    print(f"Current User's Login: {CURRENTUSER}")
    print("-" * 50)
    try:
        main()
    except Exception as e:
        printerror(str(e))
        sys.exit(1)