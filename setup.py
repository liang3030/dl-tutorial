import setuptools

with open("README.md", "r", encoding="utf-8") as f:
	long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'dl-tutorial'
AUTHOR_USER_NAME = 'liang3030'
SRC_REPO="template_dl_tutorial"
AUTHOR_EMAIL = 'liangzhang3030@gmail.com'


setuptools.setup(
	name = SRC_REPO,
	version=__version__,
	author=AUTHOR_USER_NAME,
	author_email=AUTHOR_EMAIL,
	description="A template for end to end deep learning engineering project setup",
	long_description="text/markdown",
	url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
	project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)