import os
import pytest


def delete_file(file_path):
    try:
        if not os.path.exists(file_path):
            return "ファイルが存在しません"

        os.remove(file_path)
        return "ファイルを削除しました"
    except:
        return "エラーが発生しました"


def test_file_not_exist(mocker):
    mocker.patch('os.path.exists', return_value=False)

    message = delete_file('test_file_path')

    assert message == 'ファイルが存在しません'


def test_file_exist(mocker):
    mocker.patch('os.path.exists', return_value=True)

    message = delete_file('test_file_path')

    assert message == 'エラーが発生しました'


def test_file_exists_exception(mocker):
    mocker.patch('os.path.exists', side_effect=Exception)

    message = delete_file('test_file_path')

    assert message == 'エラーが発生しました'


def test_remove(mocker):
    isfile_mock = mocker.patch("os.path.exists", return_value=True)
    remove_mock = mocker.patch("os.remove")

    message = delete_file("test_file_path")

    assert message == "ファイルを削除しました"

    isfile_mock.assert_called_once_with("test_file_path")
    remove_mock.assert_called_once_with("test_file_path")
