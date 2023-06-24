# enhanced_google_search
An enhanced google search library

**The New PyPi Project: https://pypi.org/project/enhanced-google-search/**

Fixed the language issue in the original repo: https://github.com/cj-praveen/googlesearch.py so you can search with any language google.com support

```py
pip install enhanced-google-search
```

Examples:
```py
from enhanced_google_search import search

results = search("بايثون", lang = "ar")
print(results)
```

```py
from enhanced_google_search import search

results = search(query = "Python")
print(results)
```

```py
from enhanced_google_search import search

results = search("Python")
print(results)
```

```py
from enhanced_google_search import search

results = search("Python", num = 2) # Number of results
print(results)
```

**Discord: imacoolhuman**
