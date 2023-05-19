# google_search_py
An enhanced google search library

Fixed the language issue in the original repo: https://github.com/cj-praveen/googlesearch.py so you can search with any language google.com support


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

**Discord: KKLL#9777**
