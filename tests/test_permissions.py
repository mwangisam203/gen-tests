from learning_lab.permissions import allowed_actions, can_delete, can_edit


def test_can_edit_allows_admins_and_editors():
    assert can_edit("admin")
    assert can_edit("editor")
    assert not can_edit("viewer")


def test_can_delete_allows_admin_or_owner():
    assert can_delete("admin", owns_item=False)
    assert can_delete("viewer", owns_item=True)
    assert not can_delete("viewer", owns_item=False)


def test_allowed_actions_combines_permissions():
    assert allowed_actions("editor", owns_item=True) == ["view", "edit", "delete"]
