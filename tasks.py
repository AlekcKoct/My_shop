
class Task:
    def __init__(self, descript_task, date_of_complet):
        self.descript_task = descript_task
        self.date_of_complet = date_of_complet
        self.complet = False

    def mark_complet(self):
        self.complet = True

    def __str__(self):
        status = "Выполнено" if self.complet else "Не выполнено"
        return f"Задача: {self.descript_task}, до {self.date_of_complet}, Статус: {status}"

class Task_manag :
    def __init__(self):
        self.tasks_ = []

    def add_task(self, descript_task, date_of_complet):
        task = Task(descript_task, date_of_complet)
        self.tasks_.append(task)

    def mark_task_complet(self, index):
        if 0 <= index < len(self.tasks_):
            self.tasks_[index].mark_complet()
        print("Выполнил влажную уборку квартиру!!!")

    def get_pending_tasks(self):
        return [task for task in self.tasks_ if not task.complet]

    def print_tasks(self):
        for task in self.tasks_ :
            print(task)

    def print_pending_tasks(self):
        for task in self.get_pending_tasks():
            print(task)

manag1 = Task_manag()
manag1.add_task("Сделать влажную уборку в квартире", "17.00")
manag1.add_task("Сделать домзадание с дочерью", "20.00")
manag1.add_task("Подготовить план работы", "20.11.2024г")

print("\nВот все мои дела:")
manag1.print_tasks()

print("\nДела которые я выполнил...")

manag1.mark_task_complet(0)

print("\nДела, которые я не выполнил:")
manag1.print_pending_tasks()
