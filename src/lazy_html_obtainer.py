import requests

class LazyHTMLObtainer:
    '''Returns the HTML content of the URL.'''    
    async def get_html(self, url: str) -> str:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        if response.content:
            return response.content