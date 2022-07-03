import pytest
from dundie.core import load
from .constants import PEOPLE_FILE

@pytest.fixture(scope="function")
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("This is test code")
    yield
    file_.remove()

@pytest.mark.unit
@pytest.mark.high
def test_load(create_new_file):
    """ Test load function."""

    assert len(load(PEOPLE_FILE)) == 2
