# Ray Tracer

| Language | Lines of Code |
| :------: | :-----------: |
|  Python  |      20       |

## Running

The script reads the secret key from stdin. Invoke it like this:

```sh
echo "<base32-secret-key>" | python totp.py
```

The script should produce a 6 digit code.

## Sources

- [Python code](https://github.com/susam/mintotp)
- [HOTP Spec](https://datatracker.ietf.org/doc/html/rfc4226)
- [TOTP Spec](https://datatracker.ietf.org/doc/html/rfc6238)

## License

Python code:

```
The MIT License (MIT)
=====================

Copyright (c) 2019 Susam Pal

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
