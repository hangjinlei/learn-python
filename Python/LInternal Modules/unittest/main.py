# https://www.youtube.com/playlist?list=PLe4mIUXfbIqaXv8kRvUqgrMREq-p5GgdV
# pip install nose
# nosetest --verbosity 2

import requests
import requests.exceptions


def len_todo():
    todo = get_todo()
    return len(todo)


def get_todo():
    url = "https://jsonplaceholder.typicode.com/todos"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return "No todos"
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as e:
        status_code = e.response.status_code
        if status_code in [503, 504]:
            pass
        else:
            pass
        return "HTTPError was raise"

    else:
        if response.status_code == 200:
            todo = response.json()["title"]
        else:
            todo = "No todos"

        return todo


if __name__ == "__main__":
    print(get_todo())
