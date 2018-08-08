# suppyress

A simple python library for running code and ignore any errors.

## Getting Started

### Installing

You can install this package with pip.

```shell
pip install suppyress
```

### Usage

All examples are intended for writing in a python shell (or python code file).

```python
from suppyress import suppress

@suppress
def test(a, b=1):
    result = "%s -> %s" % (a, int(b))
    return result


assert test("a", b="2") is not None
assert test("a", b="a") is None
```

or:

```python
from suppyress import safe_run

assert safe_run(int, "2") is not None
assert safe_run(int, "a") is None
```

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details
