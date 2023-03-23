from typing import List
from ToDo import (
    ToDoItem,
    ToDoList,
    MIN_PRIORITY,
    MAX_PRIORITY,
    InvalidItemException,
    InvalidPriorityException,
    ActionType,
)

END_OF_LOOP = 0


def print_user_menu():
    print("0. Exit\n1. Show all items\n2. Add new item\n3. Remove item")


NEXT_ITEM_ID_GENERATOR = (x for x in range(0, 100))


def create_new_item():
    new_item = ToDoItem(next(NEXT_ITEM_ID_GENERATOR))
    new_item.name = input("Item name: ")
    new_item.description = input("Item description: ")

    proper_priority_provided = False
    while not proper_priority_provided:
        try:
            new_item.priority = int(
                input(f"Item priority({MIN_PRIORITY}, {MAX_PRIORITY}): ")
            )
            proper_priority_provided = True
        except InvalidPriorityException as e:
            print(e)
        except ValueError:
            print("Provided priority is not an integer!")
    return new_item


def perform_item_removal(items_list: ToDoList):
    try:
        selected_item = int(input("Select item to delete with number: "))
    except ValueError:
        print("Provided value is not an integer")
    try:
        items_list.remove_item(selected_item)
    except InvalidItemException as e:
        print(e)


def perform_sort(items_list: ToDoList):
    print("1. Sort by id\n2. Sort by name\n3. Exit")
    try:
        action = int(input("Provide option: "))
        if action < 1 or action > 3:
            print("Provided option is invalid, try again")
            perform_sort(items_list)
        if action == 1:
            items_list.sort_by_id()
        elif action == 2:
            items_list.sort_by_name()

    except ValueError:
        print("Provided value is not an integer")
        perform_sort(items_list)


def perform_action(action: ActionType, items_list: ToDoList):
    if action == ActionType.SHOW_ALL:
        print("Showing all items")
        print(items_list)
    elif action == ActionType.ADD_ITEM:
        items_list.add_new_item(create_new_item())
    elif action == ActionType.REMOVE_ITEM:
        perform_item_removal(items_list)
    elif action == ActionType.SORT_ITEMS:
        perform_sort(items_list)


def main():
    action = -1
    todoList = ToDoList()
    while action != END_OF_LOOP:
        print_user_menu()
        userInput = input("\nProvide option: ")
        try:
            action = int(userInput)
            perform_action(ActionType(action), todoList)
        except ValueError:
            print("Invalid option provided, try again.\n")


if __name__ == "__main__":
    main()
