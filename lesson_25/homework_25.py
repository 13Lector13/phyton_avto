import requests
from lxml import html


url = "https://qauto2.forstudy.space/"
response = requests.get(url, auth=("guest", "welcome2qauto"))

tree = html.fromstring(response.content)

elements = tree.xpath("//*")[:25]

for i, el in enumerate(elements, 1):
    tag = el.tag

    xpath = f"(//{tag})[{i}]"
    css = f"{tag}:nth-of-type({i})"

    print("CSS:", css)
    print("XPath:", xpath)
    print("-" * 40)
