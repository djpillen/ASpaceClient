import setuptools

setuptools.setup(
    name="ASpaceClient",
    version="0.0.1",
    author="Dallas Pillen",
    description="ArchivesSpace API Wrapper",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "lxml"
    ]
)
