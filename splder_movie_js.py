import requests
import json
import random
import sqlite3


# 建立一个find() func
def find():
    # 确定访问地址
    url2 = 'https://www.1905.com/api/content/index.php'
    # 加一个请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
    }
    # 确定请求参数
    params = {
        'callback': 'reloadList',
        'm': 'converged',
        'a': 'info',
        'type': 'jryp',
        'year': 2021,
        'month': 10
    }
    # 请求地址
    response = requests.get(url2, headers=header, params=params)

    result = response.text
    print(result)


if __name__ == '__main__':
    find()