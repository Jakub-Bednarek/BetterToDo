from ToDo import ToDoList, ToDoItem, InvalidItemException, InvalidPriorityException

FIRST_ITEM_LIST_INDEX = 0
FIRST_ITEM_ID = 1
SECOND_ITEM_ID = 2
THIRD_ITEM_ID = 3
OTHER_ITEM_ID = 55
INVALID_PRIORITY = 139


def create_item_id_1():
    item1 = ToDoItem(FIRST_ITEM_ID)
    item1.name = "First"
    item1.description = "ZLast description"
    item1.priority = 3

    return item1


def create_item_id_2():
    item2 = ToDoItem(SECOND_ITEM_ID)
    item2.name = "Middle"
    item2.description = "First description"
    item2.priority = 8

    return item2


def create_item_id_3():
    item3 = ToDoItem(THIRD_ITEM_ID)
    item3.name = "Last"
    item3.description = "Middle description"
    item3.priority = 1

    return item3


def prepare_sample_items_list_for_sort():
    list = ToDoList()
    list.add_new_item(create_item_id_3())
    list.add_new_item(create_item_id_1())
    list.add_new_item(create_item_id_2())

    return list


def test_item_should_throw_when_provided_invalid_priority():
    item = ToDoItem(FIRST_ITEM_ID)

    try:
        item.priority = INVALID_PRIORITY
        assert False
    except InvalidPriorityException:
        assert True


def test_new_list_should_be_empty():
    list = ToDoList()
    assert list.empty()


def test_list_with_item_should_not_return_empty():
    list = ToDoList()
    list.add_new_item(ToDoItem(0))
    assert list.empty()


def test_list_should_be_empty_after_add_remove_item():
    list = ToDoList()
    list.add_new_item(ToDoItem(OTHER_ITEM_ID))
    list.remove_item(OTHER_ITEM_ID)

    assert list.empty()


def test_list_should_throw_when_item_not_removed():
    list = ToDoList()

    try:
        list.remove_item(FIRST_ITEM_ID)
        assert False
    except InvalidItemException:
        assert True


def test_list_should_return_item_by_id_when_single_item_in_list():
    list = ToDoList()
    item = ToDoItem(FIRST_ITEM_ID)
    list.add_new_item(item)

    assert list.get_item(FIRST_ITEM_ID) == item


def test_list_should_return_item_by_id_when_multiple_items_in_list():
    list = prepare_sample_items_list_for_sort()
    item = ToDoItem(OTHER_ITEM_ID)
    list.add_new_item(item)

    assert list.get_item(OTHER_ITEM_ID) == item


def test_list_should_throw_when_item_not_found_by_id_with_empty_list():
    list = ToDoList()

    try:
        list.get_item(FIRST_ITEM_ID)
        assert False
    except InvalidItemException:
        assert True


def test_list_should_throw_when_item_not_found_by_id_with_multiple_items():
    list = prepare_sample_items_list_for_sort()

    try:
        list.get_item(OTHER_ITEM_ID)
        assert False
    except InvalidItemException:
        assert True


def test_list_should_return_item_by_index_when_single_item_in_list():
    list = ToDoList()
    item = ToDoItem(FIRST_ITEM_ID)

    list.add_new_item(item)
    assert list.at(FIRST_ITEM_LIST_INDEX).id == item.id


def test_list_should_return_item_by_index_when_multiple_items_in_list():
    list = prepare_sample_items_list_for_sort()
    item = ToDoItem(OTHER_ITEM_ID)

    list.add_new_item(item)
    assert list.at(3) == item


def test_list_should_throw_when_index_out_of_range_in_empty_list():
    list = ToDoList()

    try:
        list.at(0)
        assert False
    except InvalidItemException:
        assert True


def test_list_should_throw_when_index_out_of_range_in_filled_list():
    list = prepare_sample_items_list_for_sort()

    try:
        list.at(5)
        assert False
    except InvalidItemException:
        assert True


def test_list_should_be_sorted_by_id_ascending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_id()

    assert sample_list.at(0).id == FIRST_ITEM_ID
    assert sample_list.at(1).id == SECOND_ITEM_ID
    assert sample_list.at(2).id == THIRD_ITEM_ID


def test_list_should_be_sorted_by_id_descending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_id(reverse=True)

    assert sample_list.at(0).id == THIRD_ITEM_ID
    assert sample_list.at(1).id == SECOND_ITEM_ID
    assert sample_list.at(2).id == FIRST_ITEM_ID


def test_list_should_be_sorted_by_name_ascending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_name()

    assert sample_list.at(0).id == FIRST_ITEM_ID
    assert sample_list.at(1).id == THIRD_ITEM_ID
    assert sample_list.at(2).id == SECOND_ITEM_ID


def test_list_should_be_sorted_by_name_descending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_name(reverse=True)

    assert sample_list.at(0).id == SECOND_ITEM_ID
    assert sample_list.at(1).id == THIRD_ITEM_ID
    assert sample_list.at(2).id == FIRST_ITEM_ID


def test_list_should_be_sorted_by_description_ascending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_description()

    assert sample_list.at(0).id == SECOND_ITEM_ID
    assert sample_list.at(1).id == THIRD_ITEM_ID
    assert sample_list.at(2).id == FIRST_ITEM_ID


def test_list_should_be_sorted_by_description_descending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_description(reverse=True)

    assert sample_list.at(0).id == FIRST_ITEM_ID
    assert sample_list.at(1).id == THIRD_ITEM_ID
    assert sample_list.at(2).id == SECOND_ITEM_ID


def test_list_should_be_sorted_by_priority_ascending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_priority()

    assert sample_list.at(0).id == THIRD_ITEM_ID
    assert sample_list.at(1).id == FIRST_ITEM_ID
    assert sample_list.at(2).id == SECOND_ITEM_ID


def test_list_should_be_sorted_by_priority_descending():
    sample_list = prepare_sample_items_list_for_sort()
    sample_list.sort_by_priority(reverse=True)

    assert sample_list.at(0).id == SECOND_ITEM_ID
    assert sample_list.at(1).id == FIRST_ITEM_ID
    assert sample_list.at(2).id == THIRD_ITEM_ID
