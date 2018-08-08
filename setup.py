from setuptools import setup, find_packages

with open("README.md", "rb") as readme_file:
    long_description = readme_file.read()
    long_description = long_description \
        .replace("](LICENSE)", "](https://github.com/WYishai/suppyress/blob/master/LICENSE)")

setup(
    name="suppyress",
    version="0.1",
    packages=find_packages(),

    author="Yishai Wiesner",
    author_email="wyishai@gmail.com",
    description="A tiny python library for running code and ignore any errors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    url="https://github.com/WYishai/suppyress",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
