import re

class MessageParser:
    '''Parses a message to find URLs.'''
    def parse(self, message: str) -> list[str]:
        url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\??[/\w\.-=&%]*'
        urls = re.findall(url_pattern, message)
        return urls