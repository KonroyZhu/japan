import re

import requests


def get_link(url,regex,encoding='utf-8'):
    """
    通过正则和导航页url获取页面上的连接
    :param url: 导航页url
    :param regex: 正则
    :return: 内容页列表
    """
    code=get_code(url,encoding=encoding)
    url_list=re.findall(regex,code)
    return url_list

def get_content(url,regex_dict,encoding='utf-8'):
    content_dict={}
    code=get_code(url,encoding=encoding)
    for key in regex_dict.keys():
        content_dict[key]={}
        content_dict[key]="\n".join(re.findall(pattern=regex_dict[key],string=code))
    return content_dict

def get_code(url,encoding='utf-8'):
    # return requests.get(url).text
    content=requests.get(url).content
    return str(content,encoding)