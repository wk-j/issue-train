import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="wk-issue-train",
    version="0.0.2",
    scripts=["wk-train-model", "wk-load-issue"],
    author="panu00x",
    author_email="lewpanu@gmail.com",
    description="train github issue to model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panu00x/LoadIssue",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
