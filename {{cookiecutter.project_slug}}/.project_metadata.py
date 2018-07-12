{
    "release": "{{ cookiecutter.release }}",
    "author_email": "{{ cookiecutter.email }}",
    "copyright": "{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}",
    "license": "MIT",
    "author": "{{ cookiecutter.full_name }}",
    "name": "{{ cookiecutter.project_slug }}",
    "url": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    "description": "{{ cookiecutter.project_description }}",
    "version": "{{ cookiecutter.version }}",
}
