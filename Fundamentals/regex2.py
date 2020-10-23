title_pattern = r"<title>([\s\n]*[\w ]+)<\/title>"
body = r"<body>(.*?)<\/body>"

import re

text = input()
title = "".join(re.findall(title_pattern, text))
body_match = "".join(re.findall(body, text))

a = re.sub(r"<[^>]*>", '', body_match)
a = re.sub(r"\s{2,}", '', a)
a = re.sub(r"\\n+", '', a, flags= re.MULTILINE)

print(f"Title: {title}\nContent: {a}")