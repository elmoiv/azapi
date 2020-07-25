import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="azapi",
    version="3.0.2",
    author="elmoiv",
    author_email="elmoiv@yahoo.com",
    description="Get Lyrics from AZLyrics.com like a Boss ~(0_0)~",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/elmoiv/azapi",
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
