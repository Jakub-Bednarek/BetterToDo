from enum import Enum, auto
from typing import List
import platform
import os

MIN_PRIORITY = 0
MAX_PRIORITY = 10
DEFAULT_PRIORITY = 0


class InvalidPriorityException(ValueError):
    pass


class InvalidItemException(ValueError):
    pass


class ToDoItem:
    def __init__(self, id: int):
        self.__id = id
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
    def id(self):
        return self.__id

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

    def __repr__(self):
        return f"Id: {self.__id} | Name: {self.__name} | Description: {self.__description} | Priority: {self.__priority}"


class ToDoList:
    def __init__(self):
        self.__todoItems: List[ToDoItem] = []

    def add_new_item(self, todoItem: ToDoItem):
        self.__todoItems.append(todoItem)

    def remove_item(self, id: int):
        found_item = None
        for item in self.__todoItems:
            if item.id == id:
                found_item = item

        if not found_item:
            raise InvalidItemException(f"Item with id: {id} was not found in list")
        self.__todoItems.remove(found_item)

    def empty(self):
        return len(self.__todoItems) == 0

    def name_key(item: ToDoItem):
        return item.name

    def id_key(item: ToDoItem):
        return item.id

    def sort_by_id(self):
        self.__todoItems.sort(key=lambda item: item.id)

    def sort_by_name(self):
        self.__todoItems.sort(key=lambda item: item.name)

    def sort_by_description(self):
        self.__todoItems.sort(key=lambda item: item.description)

    def sort_by_priority(self):
        self.__todoItems.sort(key=lambda item: item.priority)

    def __repr__(self):
        return "\n".join([str(item) for item in self.__todoItems])


class UserInterface:
    NEXT_ITEM_ID_GENERATOR = (x for x in range(0, 100))

    class InterfaceState(Enum):
        MAIN_MENU = auto()
        SORT_MENU = auto()

    class MainMenuActionType(Enum):
        SHOW_ALL = auto()
        ADD_ITEM = auto()
        REMOVE_ITEM = auto()
        SORT_ITEMS = auto()

    class SortMenuActionType(Enum):
        BY_ID = auto()
        BY_NAME = auto()
        BY_DESCRIPTION = auto()
        BY_PRIORITY = auto()
        RETURN = auto()

    def __init__(self):
        self.__current_state = self.InterfaceState.MAIN_MENU
        self.__todo_list = ToDoList()

    def clear_console(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def print_menu(self):
        if self.__current_state == self.InterfaceState.MAIN_MENU:
            print(
                "0. Exit\n1. Show all items\n2. Add new item\n3. Remove item\n4. Sort items"
            )
        else:
            print("Sort by:\n1. Id\n2. Name\n3. Description\n4. Priority\n5. Return")

    def create_new_item(self):
        new_item = ToDoItem(next(self.NEXT_ITEM_ID_GENERATOR))
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
        self.__todo_list.add_new_item(new_item)

    def remove_item(self):
        try:
            selected_item = int(input("Select item to delete with number: "))
        except ValueError:
            print("Provided value is not an integer")
        try:
            self.__todo_list.remove_item(selected_item)
        except InvalidItemException as e:
            print(e)

    def read_user_input(self):
        try:
            user_input = int(input("Provide option: "))
            if user_input >= 0:
                if (
                    self.__current_state == self.InterfaceState.MAIN_MENU
                    and user_input <= len(self.MainMenuActionType)
                    or self.__current_state == self.InterfaceState.SORT_MENU
                    and user_input <= len(self.SortMenuActionType)
                ):
                    return user_input
        except ValueError:
            print("Provided option is not an int!")
            self.read_user_input()

        print("Invalid value provided!")

        return self.read_user_input()

    def dispatch_action(self, action: int):
        if action == 0:
            return

        if self.__current_state == self.InterfaceState.MAIN_MENU:
            match self.MainMenuActionType(action):
                case self.MainMenuActionType.SHOW_ALL:
                    if not self.__todo_list.empty():
                        print(self.__todo_list)
                    else:
                        print("Items list is empty!\n")
                case self.MainMenuActionType.ADD_ITEM:
                    self.create_new_item()
                case self.MainMenuActionType.REMOVE_ITEM:
                    self.remove_item()
                case self.MainMenuActionType.SORT_ITEMS:
                    self.__current_state = self.InterfaceState.SORT_MENU
                case _:
                    print("Action not handled yet")
        elif self.__current_state == self.InterfaceState.SORT_MENU:
            match self.SortMenuActionType(action):
                case self.SortMenuActionType.BY_ID:
                    self.__todo_list.sort_by_id()
                case self.SortMenuActionType.BY_NAME:
                    self.__todo_list.sort_by_name()
                case self.SortMenuActionType.BY_DESCRIPTION:
                    self.__todo_list.sort_by_description()
                case self.SortMenuActionType.BY_PRIORITY:
                    self.__todo_list.sort_by_priority()
                case self.SortMenuActionType.RETURN:
                    pass

            self.__current_state = self.InterfaceState.MAIN_MENU

    def run(self):
        action = -1
        while not (self.__should_exit(action)):
            self.print_menu()
            action = self.read_user_input()
            self.clear_console()
            self.dispatch_action(action)

    def __should_exit(self, action: int):
        return self.__current_state == self.InterfaceState.MAIN_MENU and action == 0
