# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def filter_tasks(tasks, completed=None, priority=None):

    filtered = tasks

    if completed is not None:
        filtered = [
            task for task in filtered
            if task["completed"] == completed
        ]

    if priority is not None:
        filtered = [
            task for task in filtered
            if task.get("priority") == priority
        ]

    return filtered

def format_task(task):
    priority = task.get("priority", "NORMAL")
    return f"[{priority}] - {task['title']}"


