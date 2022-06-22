# Contributing

Thank you for contributing to the project. This document will show you the ins-and-outs of the project, and explain the structure of the files and things like how to get set up.

## Requirements

This repository contains some newer Python syntax and dependencies that expect Python 3.7 or higher. One of the core philosophies of this project is that ["new is always better"](https://youtu.be/1SNRULEnTVQ?t=14). This project was built on macOS, so anything here should work on any *nix system. Windows users: it should not be very different.

## Setup

To get started, fork this repo and then clone it. This allows you to immediately submit PRs. Next, install requirements:

```
pip3 install -r requirements.txt
```

That's it! You are now set up to contribute code to the project.

## Installation

The project is configured to install as a script. This means you can install it like so:

```
pip3 install .
```

You might prefer to use the [`--editable` flag](https://stackoverflow.com/a/35064498/2713263):

```
pip3 install -e .
```

## What do these files do?

Most files in the project are standard in Python development; however, if you are unfamiliar, this section is for you.

* `.gitignore`: Tells Git what files to ignore.
* `.pre-commit-config.yaml`: This repo is held to a higher code standard than the templates. For that reason, we use `pylint` to check your code, and a pre-commit hook to prevent committing code that is not held to this standard.
* `.pypirc`: You will not have this when you clone the repo; see the Release section below for instructions on setting it up. It is, however, pretty likely that you will *never* need this anyway.
* `build.sh`: You again, will not likely interact with this file. This simply creates a build and uploads it to PyPI. It's two commands, but it's two commands I often forget.
* `CONTRIBUTING.md`: Tells people how to contribute to the project. You're likely reading it right now.
* `LICENSE`: The project license (MIT). I have thought about using GPL or AGPL, but most of our lab operates on the MIT license anyway; it felt appropriate to use it.
* `main.py`: The main code file (at the time of writing, the *only* code file). All the secret sauce is in here.
* `pyproject.toml`: A file that tells the build system how to package the project.
* `README.md`: The...README
* `requirements.txt`: Specifies the packages required to develop this project.
* `setup.cfg`: Contains metadata and instructions for `setuptools`, which is what builds the package.

If it isn't obvious, you will likely only interact with `main.py`. That may change in the future if/when this is modularized. I feel like this doc is over-elaborated.

## Code philosophy

Here lie the core philosophical ideas of this project:

* **New is always better.** We (I) like the new shinies. Newer Python versions, newer syntax, newer coffee brewers, you get the idea. For some backward compatibility, Python 3.7 is the oldest version you should have.
* **Consistency matters.** When in doubt, make things consistent. This means if you prefer one syntax over another in one place in your code, use the same in other places as well.
* **We do not blame devs.** Devs working on this project are volunteering their time. You might be tempted to `git blame` someone; resist the urge. If there's a bug, fix it, submit a PR, and move on. (yes, I'm covering my ass here, but I do agree with the principle).
* **Moderate standards enforcement.** Standards (like PEP8) matter, but we're not anal here. As long as your code is clean and follows PEP8, your PR should be accepted.
* **Code should speak for itself.** To quote PEP20 (The Zen of Python), "If the implementation is hard to explain, it's a bad idea."
* **When in doubt, comment.** *You* understand your code *now*. You or others may not later. Code should definitely speak for itself, but if you're writing a nontrivial piece of code, comment. Similarly, magic numbers/strings should be described in a comment. Functions and files should have docstrings.

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
