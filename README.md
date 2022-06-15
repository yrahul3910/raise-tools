# raise-tools

This repository contains the source for `raise`, which check repositories by the RAISE lab for compliance with a template.

## Usage

There are two primary use cases for this tool. The first is to check that a directory containing your code is compliant with a RAISE-provided template. To do so, use

```
raise .
```

The `.` can be replaced by the directory where your code lives. This will check that your code follows PEP8 standards, that it contains the required files, and that the README file contains the necessary sections.

A second use case is to initialize a new repo from a template, similar to `npm init`. The templates come with some working code already to give you a feel for how code is expected to be written. To initialize, use

```
raise init --template dl4se
```

`dl4se` can be replaced by any template name (currently, it is the only one). If the template argument is not provided, `dl4se` is assumed. You can provide configuration options in a file. To do so, name the file `.raise.conf` in the current directory. The configuration file has the syntax below.

**Note:** The options in the configuration file have precedence over command-line args. This means that if you specify the same thing in both places, your command-line args will be ignored. This is to encourage the use of configuration files.

```
[init]
template = dl4se  # or any other template
token = GITHUB_ACCESS_TOKEN
fork = yes  # or "no"

[check]
max_line_length = 120
```

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
