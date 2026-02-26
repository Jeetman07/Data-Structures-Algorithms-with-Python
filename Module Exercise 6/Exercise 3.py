import hashlib


class URLShortener:
    """
    Mini URL shortener.

    Stores:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int

    Collision rule:
    - If generated code already exists for another URL,
      generate a new one using an extra counter value.
    """

    def __init__(self):
        # Initialize dictionaries
        self.code_to_url = {}
        self.url_to_code = {}
        self.click_counts = {}

    def _make_code(self, url, extra=""):
        """
        Create a short code using MD5 hashing.
        Returns first 6 characters of the hash.
        """
        digest = hashlib.md5((url + extra).encode()).hexdigest()
        return digest[:6]

    def shorten(self, url):
        """
        Return a short code for the URL.

        Rules:
        - If URL already shortened → return existing code
        - Otherwise generate new code
        - Resolve collisions if necessary
        """

        # If URL already exists, return stored code
        if url in self.url_to_code:
            return self.url_to_code[url]

        counter = 0
        code = self._make_code(url)

        # Collision handling
        while code in self.code_to_url and self.code_to_url[code] != url:
            counter += 1
            code = self._make_code(url, str(counter))

        # Store mappings
        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0

        return code

    def open_url(self, code):
        """
        Return original URL and increase click count.
        Return None if code not found.
        """
        if code not in self.code_to_url:
            return None

        self.click_counts[code] += 1
        return self.code_to_url[code]

    def get_stats(self, code):
        """
        Return statistics dictionary:
        {
            "code": short_code,
            "url": original_url,
            "clicks": click_count
        }

        Return None if code not found.
        """
        if code not in self.code_to_url:
            return None

        return {
            "code": code,
            "url": self.code_to_url[code],
            "clicks": self.click_counts[code]
        }


# =========================
# TESTING SECTION
# =========================

if __name__ == "__main__":

    shortener = URLShortener()

    url1 = "https://example.com/products/usb-cable"
    url2 = "https://example.com/about"
    url3 = "https://example.com/products/usb-cable"  # same as url1

    code1 = shortener.shorten(url1)
    code2 = shortener.shorten(url2)
    code3 = shortener.shorten(url3)

    print("Codes:", code1, code2, code3)
    print("Open code1:", shortener.open_url(code1))
    print("Open code1 again:", shortener.open_url(code1))
    print("Stats code1:", shortener.get_stats(code1))