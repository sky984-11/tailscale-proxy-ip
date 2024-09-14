'''
Description: 
Author: sky
Date: 2024-09-14 10:30:09
LastEditTime: 2024-09-14 10:36:01
LastEditors: sky
'''
import re
from datetime import datetime


markdown_file_path = './README.md'
with open(markdown_file_path, 'r') as f:
    content = f.read()
    print(content)
    # 获取当前时间并格式化
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ipStr = '192.168.1.1\n192.168.1.1\n'
    # 匹配并替换 <!-- BLOG_START --> 之间的内容
    pattern = r'<!-- BLOG_START -->(.*)<!-- BLOG_END -->'
    replacement = f'<!-- BLOG_START -->\n### 更新日期: {current_time}\n```\n{ipStr}\n```\n<!-- BLOG_END -->'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    print(new_content)