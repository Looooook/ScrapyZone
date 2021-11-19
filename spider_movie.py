import requests
import re
from time import sleep  # 防止爬的过猛
import sys
import importlib

# python2.x
# import sys
# reload(sys)
# sys.setdefaultencoding(‘utf-8’)


# python3.x


importlib.reload(sys)
# 确认访问地址
url = 'https://www.1905.com/mtalk/'
# 确认查找规则
pattern = '<figcaption class="list-title"><a href="(.*?)" target="_blank">(.*?)</a></figcaption>'
# 加一个请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36'
}
# 请求地址
response = requests.get(url=url, headers=header)

# 注意编码按照页面编码制定
response.encoding = 'utf-8'
# 匹配我想要的东西 re.S换行也找
result = re.findall(string=response.text, pattern=pattern, flags=re.S)

# 打印输出
# print(response, response.text)

for i in result:
    print(i[0], i[1])
    with open('film.txt', 'a+') as w:
        w.write(i[0] + i[1] + '\n')
        # print(len(result),result)
