from urllib.parse import urlparse
from bs4 import BeautifulSoup
import config 

class HTMLParser:
    '''Parses a URL to find the direct URL to PDF download.'''
    def parse_for_download_links(self, url, html) -> list[str]:
        if html == "":
            raise ValueError("HTML is empty.")

        full_download_urls = []

        download_links = self.get_download_links_from_html(html)

        # building final url
        url_bits = urlparse(url)
        website_part = url_bits.scheme + "://" + url_bits.netloc # https://www.nature.com or https://www.frontiersin.org

        # link is either absolute ("https://nature.com/article/supplementary-info/download") or relative ("/article/name/pdf")
        for link in download_links:
            full_download_url = link if self.is_url_absolute(link) else self.absolutify_url(website_part, link)
            full_download_urls.append(full_download_url)

        if not download_links:
            print(f"Couldn't find any download links on: {url}. Possibly, a captcha or login verification was required.")
            with open(config.UNABLE_TO_DOWNLOAD_HISTORY, 'a') as file:
                file.write(f"{url},")

        return full_download_urls
    
    def get_download_links_from_html(self, html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')

        informative_links = []

        all_links = set(soup.find_all('a', href=lambda href: href and href.lower().endswith('pdf')))
        for link in all_links:
            if "reporting" in str(link).lower():
                continue
            informative_links.append(link.get("href"))
        
        return informative_links
    
    def is_url_absolute(self, url: str) -> bool:
        return urlparse(url).netloc

    def absolutify_url(self, website_part, url: str) -> str:
        return website_part + url