from setuptools import setup, find_packages

__version__ = "0.0.0"

REPOSITORY_NAME = "loan_approval_prediction"
AUTHOR_NAME = "RohitPawar001"
SRC_REPO = "loan_approval_prediction"
AUTHOR_EMAIL = "rppawar491@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="python package for loan approval prediction",
    url=f"https://github.com/{AUTHOR_NAME}/{REPOSITORY_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPOSITORY_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
