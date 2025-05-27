def test_squares():
    expected_result = [0, 4, 16, 36, 64]
    result = list((x * x for x in range(10) if x % 2 == 0))
    assert result == expected_result
