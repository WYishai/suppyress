from suppyress import safe_run, suppress

@suppress
def test(a, b=1):
    result = "%s -> %s" % (a, int(b))
    return result


assert test(1, b="2") is not None
assert test(1, b="a") is None
assert safe_run(int, "2") is not None
assert safe_run(int, "a") is None
