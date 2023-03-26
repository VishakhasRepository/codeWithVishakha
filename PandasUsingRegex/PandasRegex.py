import pandas

import pandas
import re

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
d = pandas.read_html(url)[1]
data = d.to_string()
#print(data)

res = re.findall(r"\n\d{1,}\s+(.+?)\s+mutable\s+.+", data)   #['bytearray', 'dict', 'list', 'set']
#print(res)

#match all types which has curly braces in sequence order of open and close in syntax examples column
res1 = re.findall(r"\d{1,}\s+(\w{1,})\s{1,}.+\{.*\}.+", data)
#print(res1)

#match all description whose type is not more than 4 characters
res1 = re.findall(r"\d{1,}\s+\w{1,4}\s{1,}\w{1,}\s{1,}(.+?)\s{2,}", data)
#print(res1)


#match first ten characters of the description of the odd number ids
res1 = re.findall(r"\d*[13579]\s{1,}\w+?\s{1,}\w+?\s{1,}(.{10})", data)


#match all types for which syntax contains atleast one floating point number
res1 = re.findall(r"\n\d{1,}\s+(\w{1,})\s{1,}.+\d{1,}\.\d{1,}", data)
print(res1)
