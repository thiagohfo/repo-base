# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks


def format_task(task):
    if not task.get("active", True):
        return None
    return f"{task['title']} ({task['priority']})"



def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
