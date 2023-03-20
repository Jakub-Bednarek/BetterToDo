from os import system
from enum import Enum, auto
from typing import List


END_OF_LOOP = 0
MIN_PRIORITY = 0
MAX_PRIORITY = 10
DEFAULT_PRIORITY = 0


class InvalidPriorityException(ValueError):
    pass


class InvalidItemException(ValueError):
    pass


class ActionType(Enum):
    SHOW_ALL = auto()
    ADD_ITEM = auto()
    REMOVE_ITEM = auto()


class TodoItem:
    def __init__(self):
        self.__name = "Item"
        self.__description = "Description for ToDo item"
        self.__priority = DEFAULT_PRIORITY

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, new_description: str):
        self.__description = new_description

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, new_priority):
        if new_priority < MIN_PRIORITY or new_priority > MAX_PRIORITY:
            raise InvalidPriorityException(
                f"Priority must be in range <{MIN_PRIORITY}, {MAX_PRIORITY}>"
            )

        self.__priority = new_priority

    def __str__(self):
        return f"Name: {self.__name} | Description: {self.__description} | Priority: {self.__priority}"


def print_user_menu():
    print("0. Exit\n1. Show all items\n2. Add new item\n3. Remove item")


def create_new_item():
    new_item = TodoItem()
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


def perform_item_removal(items_list: List[TodoItem]):
    try:
        selected_item = int(input("Select item to delete with number: "))
    except ValueError:
        print("Provided value is not an integer")

    if selected_item > len(items_list):
        raise InvalidItemException("Selected item doesn't exist.")

    del items_list[selected_item - 1]


def perform_action(action: ActionType, items_list: List[TodoItem]):
    if action == ActionType.SHOW_ALL:
        print("Showing all items")
        index = 1
        for todo_item in items_list:
            print(f"Item {index}: {todo_item}")
            index += 1
    elif action == ActionType.ADD_ITEM:
        items_list.append(create_new_item())
    elif action == ActionType.REMOVE_ITEM:
        perform_item_removal(items_list)


def main():
    action = -1
    items: List[TodoItem] = []
    while action != END_OF_LOOP:
        print_user_menu()
        userInput = input("\nProvide option: ")
        try:
            action = int(userInput)
            perform_action(ActionType(action), items)
        except ValueError:
            print("Invalid option provided, try again.\n")


if __name__ == "__main__":
    main()
