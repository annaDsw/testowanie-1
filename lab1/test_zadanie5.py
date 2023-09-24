import zadanie5
import pytest

def test_groupByFileType_when_given_one_file():
    assert zadanie5.groupByFileType(["file.png"]) == [["file.png"]]

def test_groupByFileType_when_given_multiple_files():
    assert ["file.gif"] in zadanie5.groupByFileType(["file.png", "file.gif", "file2.png", "file3.mid"])
    assert ["file3.mid"] in zadanie5.groupByFileType(["file.png", "file.gif", "file2.png", "file3.mid"])
    assert ["file.png", "file2.png"] in zadanie5.groupByFileType(["file.png", "file.gif", "file2.png", "file3.mid"])
    assert isinstance(zadanie5.groupByFileType(["file.png", "file.gif", "file2.png", "file3.mid"]), list)
    assert len(zadanie5.groupByFileType(["file.png", "file.gif", "file2.png", "file3.mid"])) == 3


def test_groupByFileType_when_not_given_array():
    with pytest.raises(Exception):
        zadanie5.groupByFileType("file.png")

def test_groupByFileType_when_not_given_strings():
    with pytest.raises(Exception):
        zadanie5.groupByFileType([1, 2])
        
def test_groupByFileType_when_not_given_strings_with_types_after_dot():
    with pytest.raises(Exception):
        zadanie5.groupByFileType("file", "file.png")