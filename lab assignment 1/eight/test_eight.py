import eight as eight
str = "Hello WORLD "


def test_script():
    result = eight.make_lower(str)
    assert result == "hello world "
    result2 = eight.make_upper(str)
    assert result2 == "HELLO WORLD "
    result3 = eight.make_capital(str)
    assert result3 == "Hello World "
