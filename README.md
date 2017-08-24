[![python](http://forthebadge.com/images/badges/made-with-python.svg)](http://github.com/mortea15/kim)
# Kim :snake:

Kim is an open source, Raspberry Pi-powered virtual assistant. Written in :snake:Python. We'd love help of any kind, whether you'd like to contribute by submitting a bug, or have a request for a feature. You can also contribute with development, but please read the guidelines on [Contribution](#contribution) before you begin.


## Table of contents
- [Getting Started](#getting-started)
- [Documentation](#documentation)
- [Features](#features)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Contribution](#contribution)
- [License](#license)
- [Contributors](#contributors)

## Getting Started
- You will also need [Python](https://www.python.org/downloads/) for the Raspberry Pi in order to get the assistant up and running.
- After you've cloned the repository:

- To run the assistant, open a command line and type
```sh
sudo python kim.py
```

**The launcher.sh script is used to run the python script on reboot**

_In order to get this working, you'll need to do the following:_

```sh

sudo crontab -e

@reboot sh /home/pi/kim/launcher.sh >/home/pi/logs/cronlog 2>&1

```

## Documentation
https://github.com/mortea15/kim/wiki

## Features
Coming soon

## Contribution
We would love your help in the development of Kim. Please follow our guidelines on [Contribution](#contribution) on how to report bugs and request features you'd like to see, in addition to how you can contribute with development.
By following these guidelines, we make sure that communication is efficient and understandable, which hopefully will help us improve the project.

## Bugs and feature requests
If you want to submit a feature request or bug, please keep this in mind:
- Stay on topic, both regarding the request/bug itself and any discussion around it.
- Please avoid opening issues if it involves lines of code you do not understand.

### Bug reports
Definition of a bug:
A bug is an error, fault or failure in the application which is caused by the sourcecode found in this repository, which results in an incorrect or unexpected result.

We appreciate feedback of any sort, and it helps us in developing a great service. Thank you!
- Please browse the [issue tracker](https://github.com/mortea15/kim/issues) before you submit a bug or feature, to avoid duplicate entries.
- Before submitting, make sure to pull the latest version to check if the bug is fixed, or feature is implemented.
- Stick to ONE bug per issue.
* Please use the following format when submitting:

**Short description of what happened**

*Description*

**Expected behaviour**

*Description*

**Actual Behaviour**

*Description*

**Steps to reproduce**

*Description*

**Your enviroment**

*Operative System, Python Version, which Raspberry Pi, and any other information of relevance*

### Feature requests
We're open for adding new features, please keep in mind that it should be of relevance to this project.
- Including details when submitting feature requests is essential. It makes it easier for the developers to understand the request.

### Pull requests
- Please include documentation on all code submitted
- If a new feature is implemented, it should be explained with detail in the [Wiki](https://github.com/mortea15/kim/wiki)

## License
[GPL3.0](https://github.com/mortea15/kim/blob/master/LICENSE)

## Contributors
**Developed by:**
- [Morten Amundsen](https://github.com/mortea15/)
- [Svenn-Roger Sørensen](https://github.com/tjodalv2k/)
- [Benjamin Gutierrez Børresen](https://github.com/Bunnymann/)
- [Erik Haaland](https://github.com/erih14/)