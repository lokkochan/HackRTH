import os, json


def save_data(d):
    datafile.write(json.dumps(d))
    datafile.flush()


if os.path.exists('data.json'):
    datafile = open('data.json', 'w+')
    try:
        data = json.load(datafile)
    except json.decoder.JSONDecodeError:
        data = {'codes': {}}
else:
    data = {'codes': {}}
    datafile = open('data.json', 'w+')
    save_data(data)