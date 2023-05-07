import setuptools

with open('ReadMe.md', 'r', encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "bender"
AUTHOR_USER_NAME = "Sarthak"
SRC_REPO = "bender"
AUTHOR_EMAIL = 'sarthaktiwari.ind@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/sarthaktiwari/bender",
    project_url = {
        "Bug Tracker": "https://github.com/sarthaktiwari/bender/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    )