from enum import Enum, auto
from typing import List


class InvalidPriorityException(ValueError):
    pass


class InvalidItemException(ValueError):
    pass


class ActionType(Enum):
    SHOW_ALL = auto()
    ADD_ITEM = auto()
    REMOVE_ITEM = auto()


MIN_PRIORITY = 0
MAX_PRIORITY = 10
DEFAULT_PRIORITY = 0


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

    def __str__(self):
        return f"Id: {self.__id} | Name: {self.__name} | Description: {self.__description} | Priority: {self.__priority}"

    def __repr(self):
        return str(self)


class ToDoList:
    def __init__(self):
        self.__todoItems: List[ToDoItem] = []

    def add_new_item(self, todoItem: ToDoItem):
        self.__todoItems.append(todoItem)

    def remove_item(self, id: int):
        item = filter(lambda x: x.id == id, self.__todoItems)
        if not item:
            raise InvalidItemException(f"Item with id: {id} was not found in list")

    def __repr__(self):
        return "\n".join([str(item) for item in self.__todoItems])
