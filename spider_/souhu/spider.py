#
# https://search.sohu.com/outer/search/meta?keyword=%E4%B8%AD%E6%97%A5&from=20&terminalType=wap&ip=14.16.197.7&city=%E5%B9%BF%E4%B8%9C%E7%9C%81&source=wap-sohu&SUV=1708311245246654&size=10&searchType=news&queryType=edit
#https://search.sohu.com/outer/search/meta?keyword=%E4%B8%AD%E6%97%A5&from=40&terminalType=wap&ip=14.16.197.7&city=%E5%B9%BF%E4%B8%9C%E7%9C%81&source=wap-sohu&SUV=1708311245246654&size=10&searchType=news&queryType=edit
#https://search.sohu.com/outer/search/meta?keyword=%E4%B8%AD%E6%97%A5&from=50&terminalType=wap&ip=14.16.197.7&city=%E5%B9%BF%E4%B8%9C%E7%9C%81&source=wap-sohu&SUV=1708311245246654&size=10&searchType=news&queryType=edit
#
import re

from spider_.common import get_code, get_link, get_content

link_list=get_link(url="https://search.sohu.com/outer/search/meta?keyword=中日&terminalType=wap&source=wap-sohu&SUV=1708311245246654",
               regex='url":"(http://www\.sohu\.com/a/.*?)"')

for link in link_list:
    print(link)
    content=get_content(link,regex_dict={'title':'<meta property="og:title" content="(.*?)"/>',
                                       'time':'<meta property="og:release_date" content="(\d{4}-\d{2}-\d{2} \d{2}:\d{2})"/>',
                                       'content':'<p>(.*?)</p>'})
    content["content"]="".join(re.split(pattern="<.*?>",string=content["content"]))
    print(content)

# for i in range(1,12):
#     print(i)