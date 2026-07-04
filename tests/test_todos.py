from learning_lab.todos import add_todo, complete_todo, open_todos


def test_add_todo_appends_open_item():
    assert add_todo([], "Practice") == [{"title": "Practice", "done": False}]


def test_complete_todo_marks_matching_item():
    todos = [{"title": "Practice", "done": False}]

    assert complete_todo(todos, "Practice") == [{"title": "Practice", "done": True}]


def test_open_todos_filters_done_items():
    todos = [{"title": "Practice", "done": False}, {"title": "Rest", "done": True}]

    assert open_todos(todos) == [{"title": "Practice", "done": False}]
