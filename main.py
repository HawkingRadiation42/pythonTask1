list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    list_3 = []
    # Merge information from list_1 and list_2
    for student_1 in list_1:
        student_id = student_1['id']
        student_2 = next((s for s in list_2 if s['id'] == student_id), {})
        merged_dict = {**student_1, **student_2}
        list_3.append(merged_dict)

    # Add students from list_2 that are not in list_1
    for student_2 in list_2:
        if student_2['id'] not in (s['id'] for s in list_3):
            list_3.append(student_2)

    return list_3

list_3 = merge_lists(list_1, list_2)
print(list_3)

