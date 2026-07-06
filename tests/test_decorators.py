from learning_lab.decorators import call_counter


def test_call_counter_tracks_calls():
    @call_counter
    def greet(name):
        return f"Hi {name}"

    assert greet("Ada") == "Hi Ada"
    assert greet("Grace") == "Hi Grace"
    assert greet.calls == 2
