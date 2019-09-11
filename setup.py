import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="azapi",
    version="1.0.1",
    author="elmoiv",
    author_email="elmoiv@yahoo.com",
    description="Fast and Secure AZLyrics API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmoiv/AZLyricsAPI",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)