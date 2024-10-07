import re
import json

def filter_emoji(desstr, restr=''):
    # 过滤表情
    co = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF' u'\u2600-\u2B55 \U00010000-\U0010ffff]+')
    return co.sub(restr, desstr)

if __name__ == "__main__":
    with open("output.json","r",encoding="utf8") as f:
        data = filter_emoji(f.read())
        data = json.loads(data)

    with open("output.json","w",encoding="utf8") as f:
        json.dump(data,f,indent=4,ensure_ascii=False)
