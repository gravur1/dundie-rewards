import pytest

MARKER = """\
unit: Mark integration tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
win: Runs on windows
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmp_dir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield
