# Working on the storefront

A static storefront. No build step, no package manager, no network needed.

## Run it

```bash
./serve.sh                      # http://127.0.0.1:4173, PORT overrides
```

Serve it in the background before you open a browser on it:

```bash
./serve.sh >/tmp/store.log 2>&1 &
```

## Test it

```bash
python3 -m unittest discover -s tests -v
```

These checks need no browser. They start the server, fetch the page, and assert
the markup and the cart logic are in place.

## Look at it

This machine has a desktop and Google Chrome, and `DISPLAY` is already set in
your environment. Use it exactly as it is: do not set `DISPLAY` yourself and
do not pick a display by listing `/tmp/.X11-unix`. Screenshots are taken of
the display `DISPLAY` names, so a browser opened on any other one is
invisible to you.

```bash
google-chrome --window-size=1280,760 http://127.0.0.1:4173/ &
```

Give it a few seconds to paint before you look.

## House rules

- Keep it dependency-free: HTML, CSS, and plain JavaScript.
- Change the least CSS that fixes the problem, and delete any workaround the
  real fix makes unnecessary.
- Say what you saw in the browser, not only what you changed.
