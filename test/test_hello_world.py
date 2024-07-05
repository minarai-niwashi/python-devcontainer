from src.hello_world import get_hello_world


def test_get_hello_world():
    expected_output = "hello world!"
    assert (
        get_hello_world() == expected_output
    ), f"Expected '{expected_output}' but got '{get_hello_world()}'"
