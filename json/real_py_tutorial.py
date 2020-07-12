import requests
import json


def main():

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)

    count_complete = {}

    for i in todos:
        if i["userId"] not in count_complete:
           count_complete[i["userId"]] = 0
        if i["completed"] == True:
           count_complete[i["userId"]] += 1

    top_complete = sorted(count_complete.items(), key=lambda x: x[1], reverse=True)
    print(top_complete)


if __name__ == '__main__':

    print("hello world")
    main()
