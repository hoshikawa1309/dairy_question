import requests
from bs4 import BeautifulSoup
import json
import random

class User(object):
    def __init__(self,id):
        self.id = id
        self.url = 'https://atcoder.jp/users/' + self.id

    ## テスト用
    def show_info(self):
        print()
        print("--show user info--")
        print(self.id)
        print(self.url)
        print(self.max_rate)
        print()

    def get_max_rate(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        elems = soup.findAll("span",{"class":"user-green"})
        if elems:
            self.max_rate = int(elems[2].get_text())
        else:
            print("no user info")
            exit()

    def get_question_candidates(self):
        res = requests.get(
            "https://kenkoooo.com/atcoder/resources/problem-models.json")
        data = json.loads(res.text)
        range_min = max(self.max_rate - 100, 0)
        range_max = self.max_rate + 100
        question_candidates = []
        for key, val in data.items():
            if 'difficulty' in val.keys() and range_min < val['difficulty'] < range_max:
                    question_candidates.append(key)
        # print(question_candidates)
        return question_candidates

    def get_question_name(self, code):
        res = requests.get("https://kenkoooo.com/atcoder/resources/merged-problems.json")
        data = json.loads(res.text)
        for datum in data:
            if datum['fastest_problem_id'] == code:
                return datum['title']

    def get_question(self):
        candidates = self.get_question_candidates()
        candidates_len = len(candidates)
        idx = random.randint(0, candidates_len - 1)
        question_code = candidates[idx]
        question_name = self.get_question_name(question_code)
        print(question_code, question_name)
