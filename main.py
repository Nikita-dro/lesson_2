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


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
