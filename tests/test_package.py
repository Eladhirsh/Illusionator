import illusionator


def test_package_exposes_version():
    assert isinstance(illusionator.__version__, str)
    assert illusionator.__version__
