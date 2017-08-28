import requests

default_ip = '127.0.0.1'
default_port = 5000
base_url = 'http://{ip}:{port}/'.format(ip=default_ip, port=5000)


def test_httpbin_post():
    mydata = [{'name': 'Dmitry'}, 'hello']
    r = requests.post(url=base_url+'post', json=mydata)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data['json'] == mydata


def test_httpbin_ip():
    r = requests.get(url=base_url+'ip')
    assert r.status_code == 200, r.text
    data = r.json()
    assert data == {u'origin': default_ip}
    assert r.elapsed.total_seconds() < 0.200
