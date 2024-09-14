'''
Description: 
Author: sky
Date: 2024-09-14 09:56:53
LastEditTime: 2024-09-14 10:41:49
LastEditors: sky
'''
import requests
import json
import re
from datetime import datetime

def scan_website(address):
    '''
      Tailscale服务器扫描
      address:IP地址
    '''
    url = f'http://{address}:33445/'
    try:
        # 使用Session保持会话状态
        with requests.Session() as session:
            # 设置超时时间为3秒
            res = session.get(url, timeout=3)
            if ('Client sent an HTTP request to an HTTPS server' or 'Tailscale') in res.text:
                return address
    except requests.RequestException as e:
        pass


def re_readme(ipStr):
    '''
      处理README.md文件
    '''
    with open('README.md', 'r') as f:
        content = f.read()

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        pattern = r'<!-- BLOG_START -->(.*)<!-- BLOG_END -->'
        replacement = f'<!-- BLOG_START -->\n### 更新日期: {current_time}\n```\n{ipStr}\n```\n<!-- BLOG_END -->'

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        print(new_content)
        with open('README.md', 'w') as f:
            f.write(new_content)
        

def main():
    with open('scan.json', 'r') as f:
        data = json.load(f)
        ipStr = ''
        for item in data:
            ip = scan_website(item['ip'])
            ipStr += f"{ip}\n"
        re_readme(ipStr)




if __name__ == '__main__':
    main()