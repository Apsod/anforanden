import re
import sys
import collections
import json
from html.parser import HTMLParser


stylefix = re.compile(r'\s*STYLEREF Kantrubrik \\[*] MERGEFORMAT\s*')
parafix = re.compile(r'\n{3,}')

class DataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tagstack = []
        self.data = []

    def handle_starttag(self, tag, attrs):
        self.tagstack.append(tag)

    def handle_endtag(self, tag):
        assert self.tagstack.pop() == tag
        if tag == 'p':
            self.data.append('')

    def handle_data(self, data):
        if (m := stylefix.search(data)):
            pass
            #print(data)
        else:
            self.data.append(data)

    def get_data(self):
        assert len(self.tagstack) == 0
        return parafix.sub('\n\n', '\n'.join(self.data)).strip()

if __name__ == '__main__':
    data = collections.defaultdict(dict)
    KEYS = ['dok_id', 'avsnittsrubrik', 'underrubrik']
    for line in sys.stdin:
        doc = json.loads(line)['anforande']
        key = tuple(doc.get(k, '') for k in KEYS)
        subkey = int(doc['anforande_nummer'])
        text = doc['anforandetext']
        if text is None:
            text = ''
        parser = DataParser()
        parser.feed(text)
        parser.close()
        text = parser.get_data()
        data[key][subkey] = {'role': doc['talare'], 'message': text}
    for key, parts in data.items():
        doc_id, title, subtitle = key
        nums = sorted(parts)
        print(json.dumps({'title': title, 'subtitle': subtitle, 'turns': [parts[n] for n in nums]}))
