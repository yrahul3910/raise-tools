# raise-tools

This repository contains the source for `raise-tools`, which check repositories by the RAISE lab for compliance with a template.

## Release

To release a new version, ensure you have a `.pypirc` file setup as follows:

```
[distutils]
  index-servers =
    pypi
    raise-tools

[pypi]
  username = __token__
  password = YOUR_TOKEN_HERE

[raise-tools]
  repository = https://upload.pypi.org/legacy/
  username = __token__
  password = YOUR_TOKEN_HERE
```
