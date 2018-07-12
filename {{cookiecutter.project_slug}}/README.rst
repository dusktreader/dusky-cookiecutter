.. image::  https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
   :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
   :alt:    Latest Published Version

.. image::  https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master
   :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
   :alt:    Build Status

.. image::  https://readthedocs.org/projects/{{ cookiecutter.project_slug }}/badge/?version=latest
   :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
   :alt:    Documentation Build Status

{% for _ in cookiecutter.project_name + 'xx' %}*{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name + 'xx' %}*{% endfor %}

{% for _ in cookiecutter.project_description %}-{% endfor %}
{{ cookiecutter.project_description }}
{% for _ in cookiecutter.project_description %}-{% endfor %}

*TODO: Fill in this summary of the project*

Super-quick Start
-----------------
 - requirements: `python` versions {{ cookiecutter.python_versions | join(', ') }}
 - install through pip: `$ pip install {{ cookiecutter.project_slug }}`

Documentation
------------------

The complete documentation can be found at the
`{{ cookiecutter.project_name }} home page <http://{{ cookiecutter.project_slug }}.readthedocs.io>`_
