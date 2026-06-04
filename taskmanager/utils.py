# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks


def filter_priority(tasks, priority):
    return [task for task in tasks if task.get("priority") == priority]

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]

