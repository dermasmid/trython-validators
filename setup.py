import re

from setuptools import setup


with open("trython_validators.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]


with open("README.md", encoding="utf-8") as f:
    readme = f.read()


with open("requirements.txt", encoding="utf-8") as f:
    requirements = [r.strip() for r in f]


setup(
    name="trython-validators",
    version=version,
    py_modules=["trython_validators"],
    url="https://github.com/dermasmid/trython-validators",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Cheskel Twersky",
    author_email="twerskycheskel@gmail.com",
    description="Validators for trython",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires=">=3.6",
)
