x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0

print(x)
print(y)

print(chr(129312))

from CQs.cq06_sum import f_range_sum


def test_1() -> None:
    vals: list[float] = [3.3, 4.9, 6.5, 6.3]
    assert f_range_sum(vals) == 21.0
