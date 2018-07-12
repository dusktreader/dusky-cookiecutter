{% for _ in cookiecutter.project_name + 'xx' %}*{% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name + 'xx' %}*{% endfor %}

{% for _ in cookiecutter.project_description %}-{% endfor %}
{{ cookiecutter.project_description }}
{% for _ in cookiecutter.project_description %}-{% endfor %}

.. include:: overview.rst

Table of Contents
=================

.. toctree::
   :glob:
   :maxdepth: 2
   :caption: Contents:

   Quickstart <quickstart>
   API <sview>
dusky-cookiecutter/{{cookiecutter.project_slug}}/docs/index.rst
