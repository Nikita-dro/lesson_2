import requests


def parse(query: str) -> dict:
    info = requests.get(query)
    return info.json()


if __name__ == '__main__':
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://127.0.0.1:5000/?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://127.0.0.1:5000/') == {}
    assert parse('http://127.0.0.1:5000/?') == {}
    assert parse('http://127.0.0.1:5000/?name=Dima') == {'name': 'Dima'}
    assert parse('http://127.0.0.1:5000/?empty=') == {'empty': ''}
    assert parse('http://127.0.0.1:5000/?name=Tom&work=store%20manager') == {'name': 'Tom', 'work': 'store manager'}
    assert parse('http://127.0.0.1:5000/?age=89&') == {'age': '89'}
    assert parse('http://127.0.0.1:5000/?password=678&password=9098') == {'password': '678'}
    assert parse('http://127.0.0.1:5000/?work=python%20developer&salary=') == {'work': 'python developer', 'salary': ''}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
