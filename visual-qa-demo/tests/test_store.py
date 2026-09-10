"""Checks that run without a browser.

They start the real server, fetch the real page, and assert the markup and the
cart logic are in place. They pass. They also cannot see whether a click
reaches the button, which is the whole point of the demo: this suite is green
while the storefront is broken for every visitor.
"""

from __future__ import annotations

import subprocess
import time
import unittest
import urllib.error
import urllib.request
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
PORT = 4271
BASE = f"http://127.0.0.1:{PORT}"


def get(path: str) -> str:
    with urllib.request.urlopen(BASE + path, timeout=5) as response:
        return response.read().decode("utf-8")


class StoreTests(unittest.TestCase):
    server: subprocess.Popen

    @classmethod
    def setUpClass(cls) -> None:
        cls.server = subprocess.Popen(
            ["python3", "-m", "http.server", str(PORT), "--bind", "127.0.0.1"],
            cwd=APP_DIR,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        deadline = time.monotonic() + 10
        while time.monotonic() < deadline:
            try:
                get("/index.html")
                return
            except (urllib.error.URLError, ConnectionError):
                time.sleep(0.1)
        cls.server.terminate()
        raise AssertionError("the server did not come up")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.terminate()
        cls.server.wait(timeout=10)

    def test_page_is_served(self) -> None:
        self.assertIn("Tensorlake Supply Co.", get("/index.html"))

    def test_assets_are_served(self) -> None:
        self.assertIn(".card", get("/styles.css"))
        self.assertIn("addToCart", get("/app.js"))

    def test_page_has_an_add_to_cart_button(self) -> None:
        page = get("/index.html")
        self.assertIn('id="add"', page)
        self.assertIn("Add to cart", page)

    def test_page_has_a_cart_badge_starting_at_zero(self) -> None:
        page = get("/index.html")
        self.assertIn('id="cart-count"', page)
        self.assertIn('class="count">0<', page)

    def test_the_button_is_wired_to_the_cart(self) -> None:
        script = get("/app.js")
        self.assertIn('getElementById("add").addEventListener("click", addToCart)', script)

    def test_adding_to_cart_increments_the_badge(self) -> None:
        script = get("/app.js")
        body = script.split("function addToCart()", 1)[1].split("}", 1)[0]
        self.assertIn("state.count += 1", body)
        self.assertIn("badge.textContent", body)


if __name__ == "__main__":
    unittest.main()
