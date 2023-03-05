import pytest
from mock_project import some_file


class TestA:
    def test_01(self):
        assert some_file.generate_random() == 1
