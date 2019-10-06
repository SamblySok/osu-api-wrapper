# Simple osu! API wrapper for python

## Requires

- python 2 or 3

## How to use?

```python
import osuapi
import requests
import aiohttp

r = requests.get(osuapi.url('user', 'your-secret-key', u='nathan on osu'))
print(r.status)
print(r.json())

# or

async with aiohttp.ClientSession() as session: # this will be in async function
  async with session.get(osuapi.url('user', 'your-secret-key', u='nathan on osu')) as res:
    print(await res.json())
```

Working **all** parts and parts arguments, but without `get_`
