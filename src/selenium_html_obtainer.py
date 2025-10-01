from selenium import webdriver
from selenium_stealth import stealth

class SeleniumHTMLObtainer:
    '''Returns the HTML content of the URL.'''    
    async def get_html(self, url: str) -> str:
        options = webdriver.FirefoxOptions()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/96.0.4664.110 Safari/537.36')

        browser = webdriver.Firefox(options=options)
        browser.implicitly_wait(30)
        browser.get(url)
        
        html_source = browser.page_source
        browser.quit()
        return html_source
