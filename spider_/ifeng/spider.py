import re

from spider_.common import get_link, get_content, get_code



link_list=get_link(url="https://search.ifeng.com/sofeng/search.action?q=中日&c=1&p=3",regex="http.*?ifeng\.com.*?shtml")
regex_dict={'title':'<title>(.*?)</title>',
            "content":"<p>(.*?)</p>"}

for link in link_list:
    print(link)
    content_dict=get_content(link,regex_dict=regex_dict)
    content_dict["content"]="".join(re.split(pattern="<.*?>",string=content_dict["content"]))
    print(content_dict)