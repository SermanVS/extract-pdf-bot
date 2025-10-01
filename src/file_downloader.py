from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import config

class FileDownloader():
    def download(self, url: str) -> bool:
        parsed_url = urlparse(url)
        filename =  Path(config.DOWNLOAD_DIRECTORY)/Path(parsed_url.path).name
        urllib.request.urlretrieve(url, filename)
        return self.check_file_exists(filename)
        
    def check_file_exists(self, filename: Path) -> bool:
        return filename.exists()