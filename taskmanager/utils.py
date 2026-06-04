# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def filter_tasks(tasks, completed=None, priority=None):

    filtered = tasks


def format_task(task):
    priority = task.get("priority", "NORMAL")
    return f"[{priority}] {task['title']}"


