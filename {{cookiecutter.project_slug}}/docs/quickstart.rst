Quickstart
==========

Requirements
------------

* Python versions {{ cookiecutter.python_versions | join(', ') }}

Installation
------------

Install from pypi
.................
This will install the latest release of {{ cookiecutter.project_slug }} from pypi via pip::

$ pip install {{ cookiecutter.project_slug }}

Install latest version from github
..................................
If you would like a version other than the latest published on pypi, you may
do so by cloning the git repostiory::

$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

Next, checkout the branch or tag that you wish to use::

$ cd {{ cookiecutter.project_slug }}
$ git checkout integration

Finally, use pip to install from the local directory::

$ pip install .

Using
-----

*TODO: Fill in this usage description*
