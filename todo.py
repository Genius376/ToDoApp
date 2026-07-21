import random, datetime, json
from typing import Any

class Task:
    def __init__(self, text):
        self.id = random.randint(1,100)
        self.text = text
        self.completed = False

    def toggle_complete(self):
        self.completed = not self.completed

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "comleted": self.completed
        }
    
class DeadlineTask(Task):
    def __init__(self, text, due_date):
        super().__init__(text=text)
        self.due_date = due_date

    def to_dict(self) -> dict[str, Any]:
        task = super().to_dict()
        task["due_date"] = self.due_date
        return task


class ReccuringTask(Task):
    def __init__(self, text, frequency):
        super().__init__(text=text)
        self.frequency = frequency

    def to_dict(self):
        task = super().to_dict()
        task["frequency"] = self.frequency
        return task

class Kontroler:
    def __init__(self):
        self.task_list: list[Task | DeadlineTask | ReccuringTask] = self.load()

    def save(self):
        '''Saves task list to JSON format'''
        tasks = self.view_tasks()
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)

    def load(self):
        '''Loads task list from JSON format'''
        with open("tasks.json", "r") as f:
            deserialized = json.load(f)
            return deserialized
    
    # CREATE
    def add_task(self, task: Task | ReccuringTask | DeadlineTask):
        self.task_list.append(task)
    
    # READ
    def view_tasks(self):
        return [ task.to_dict() for task in self.task_list ]

    # UPDATE
    def update_items(self):
        if len(self.task_list) <= 0:
            print("Your list is empty!")
            Kontroler.add_item(self)
        else:
            print(self.task_list)
            choice = input("If you want to add an item type 'ADD'\nIf you want to remove an item type 'YES'\nif you want to exit type 'NO':\n")
            if choice == "ADD".lower():
                Kontroler.add_item(self)
            elif choice == "YES".lower():
                Kontroler.remove_item(self)
        self.save()

        # DELETE
    def remove_item(self):
        print(self.task_list)
        removed_item = input("Enter an item you want to remove from your list: ")
        if removed_item in self.task_list:
            self.task_list.remove(removed_item)
            print(f"You removed {removed_item} from the list.\nYou have {self.task_list} in your list.")
        else:
            print(f"{removed_item} is not on your list!")
        self.save()

main_menu_items = [
    "New list",
    "Update list",
    "View list",
    "Delete list",
    "Exit"
]

task_menu_items = [
    "Task",
    "Deadline Task",
    "Reccuring Task"
]


def main():
    print("Welcome to my ToDo application.")
    print("-" * 60)

    kontroler = Kontroler()

    while True:
        print()
        # Print the main menu to user
        for index, item in enumerate(main_menu_items):
            print(f"{index + 1}) {item}")

        main_menu_selection = int(input("Please select an option: "))
        print()

        if main_menu_selection == 1:
            # Print the task menu to user
            for index, item in enumerate(task_menu_items):
                print(f"{index + 1}) {item}")

            task_menu_selection = int(input("Please select an option: "))
            print()

            if task_menu_selection == 1:
                task_text = input("Enter task text:\n")
                task = Task(text=task_text)
                kontroler.add_task(task)
            
            if task_menu_selection == 2:
                due_date_text = input("Enter due date: ")
                task_text = input("Enter task text:\n")
                task = DeadlineTask(text=task_text, due_date=int(due_date_text))
                kontroler.add_task(task)
            
            if task_menu_selection == 3:
                frequency_text = input("Enter frequency: ")
                task_text = input("Enter task text:\n")
                task = ReccuringTask(text=task_text, frequency=int(frequency_text))
                kontroler.add_task(task)
            
            kontroler.save()
        
        if main_menu_selection == 3:
            tasks = kontroler.view_tasks()
            for task in tasks:
                print(task)
                print("*" * 60)

        if main_menu_selection == 5:
            break
    

if __name__ == "__main__":
    main()




# # Your list
# task = Task(text="nešto")
# task_dict = task.to_dict()
# task_json = json.dumps(task_dict)

# print(type(task_dict))
# print(type(task_json))
# """
# kontroler = Kontroler()
# kontroler.options() """
