# coding: utf-8

import logging
import requests
import random


logger = logging.getLogger('wechat-pocket')


class Tuling:

    api_url = 'http://www.tuling123.com/openapi/api'

    def __init__(self, api_key):
        self.session = requests.Session()
        self.api_key = api_key

    def random_words(self):
        return random.choice([
            '哦',
            '🤣',
        ])

    def reply_text(self, text, user_name, location):
        if location:
            location = location[:30]

        payload = {
            'key': self.api_key,
            'info': str(text),
            'user_id': user_name,
            'loc': location
        }

        try:
            r = self.session.post(self.api_url, json=payload).json()
            answer = r.get('text')
        except Exception as e:
            logger.exception(e)
            answer = None

        if not answer:
            answer = self.random_words()

        return answer
