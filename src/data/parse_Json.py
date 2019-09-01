#coding:UTF-8
import json

def load_json(path):
    with open(path, "r", encoding='UTF-8') as load_js:
        return json.load(load_js)


