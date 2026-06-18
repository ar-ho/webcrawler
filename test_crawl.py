import unittest
from crawl import normalize_url

class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        test_cases = [
            ("https://www.boot.dev/blog/path", "www.boot.dev/blog/path"),
            ("http://www.boot.dev/blog/path", "www.boot.dev/blog/path"),
            ("https://boot.dev/blog/path", "boot.dev/blog/path"),
            ("http://boot.dev/blog/path", "boot.dev/blog/path"),
            ("https://www.boot.dev", "www.boot.dev"),
            ("https://www.boot.dev/", "www.boot.dev"),
        ]

        for input_url, expected in test_cases:
            with self.subTest(url=input_url):
                actual = normalize_url(input_url)
                self.assertEqual(actual, expected)
