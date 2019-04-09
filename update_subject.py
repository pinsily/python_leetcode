import re

text = open("leetcode.html").read()

pattern = re.compile('.+?<tr>\n.+<td>(.*?)</td>\n.+<td>\n.+<div><a.+href="(.*?)">(.*?)</a></div>\n.+</td>\n.+<td><span>(.*?)</span></td>\n.+</tr>\n', flags=re.MULTILINE)
items = re.findall(pattern, text)

with open("README.md", 'a') as f:
    for item in items:
        order = item[0]
        link = item[1]
        title = item[2]
        difficulty = item[3]

        md = "- [ ] [{0}. {1}]({2})\n".format(order, title, link)
        f.write(md)
