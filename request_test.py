import requests
import re
import bs4

info = "姓名:bobby 生日:1987年10月1日 本科:2005年9月1日"

match_result =  re.search(".*生日.*?(\d{4}).*本科.*?(\d{4})", info)
print(match_result.group(1))
print(match_result.group(2))


# match 匹配截止于回车换行
# search 不会截止于回车换行符
print(info)
print(re.sub("\d{4}", "2019", info))

name = "my name is Bobby"
print(re.search("bobby", name, re.IGNORECASE).group())


