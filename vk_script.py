#!/usr/bin/env python3

import os
import requests

from datetime import datetime

from src.parse_arguments import parse


def main():
    arguments = parse()

    year, month = arguments.year, arguments.month
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'owner_id': -159352562,
        'from_group': 1,
        'v': 5.131,
        'access_token': '',
        'message': None,
        'publish_date': None,
    }

    result = os.popen(f'./main.py {year} {month} -a {arguments.accuracy}').read()

    result = result.split('\n')[3:]
    for post in [day.split() for day in result]:
        if len(post) == 2:
            day, params['message'] = post
            time = '00:00'
        elif len(post) == 3:
            day, params['message'], time = post
        else:
            print(post)
            break

        params['publish_date'] = datetime.fromisoformat(f'{year}-{month:02d}-{day} {time}').timestamp()
        requests.get(url, params)


if __name__ == '__main__':
    main()
