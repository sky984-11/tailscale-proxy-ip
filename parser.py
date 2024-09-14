'''
Description: 
Author: sky
Date: 2024-09-14 09:56:53
LastEditTime: 2024-09-14 12:15:48
LastEditors: sky
'''
import requests
import json
import re
from datetime import datetime
import os


import subprocess

def executeCmd(cmd):
    """
        命令执行及回显传参
        cmd:系统命令
    """
    (status, output) = subprocess.getstatusoutput(cmd)
    return (status, output)

def check_masscan():
    '''
    检查masscan
    '''
    cmd = 'masscan --version'
    masscan_status = executeCmd(cmd)[0]

    if masscan_status == 1:
        return True
    else:
        if masscan_status != 0:
            print('masscan未安装或未添加至环境变量')
        return False

def scan_ip():
    """
        扫描互联网上33445开放的IP
    """
    masscan_status = check_masscan()
    if masscan_status:
        cmd = f'sudo masscan -c myscan.conf'
        # masscan是否执行完成
        masscan_List = executeCmd(cmd)
        masscan_active = masscan_List[0]
        if masscan_active == 0:
            return True
        else:
            print(masscan_List[1])
            return False
        
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
        with open('README.md', 'w') as f:
            f.write(new_content)
        
def gitAction():
    executeCmd('git config --local user.email "action@github.com"')
    executeCmd('git config --local user.name "GitHub Action"')
    executeCmd('git add README.md')
    executeCmd('git commit -m "Update README via GitHub Actions"')
    executeCmd('git push')


def main():
    status = scan_ip()
    if status:
        with open('scan.json', 'r') as f:
            data = json.load(f)
            ipStr = ''
            for item in data:
                ip = scan_website(item['ip'])
                ipStr += f"{ip}\n"
            re_readme(ipStr)
            gitAction()




if __name__ == '__main__':
    main()