# Storefront: a bug the tests cannot see

A one-product storefront used to demonstrate visual QA by a cloud agent.

The page renders correctly. The test suite passes. **Clicking "Add to cart"
does nothing**, and the cart badge never leaves `0`.

Nothing in a log or a test run says so:

- the server returns 200 and the markup is correct;
- `app.js` defines the handler and binds it to the button;
- no JavaScript error is thrown, because the handler is simply never reached;
- `python3 -m unittest discover -s tests -v` is green.

Finding it takes a browser, a click, and something that looks at the result.

## Layout

| Path | What it is |
|---|---|
| `index.html` | The page |
| `styles.css` | The styling |
| `app.js` | Cart counter, toast, details dialog |
| `serve.sh` | `python3 -m http.server 4173` |
| `tests/test_store.py` | Browserless checks that pass |
| `AGENTS.md` | How to run, test, and view it |

## Reset it

To restore the bug after a fix, revert the change to `styles.css`.
