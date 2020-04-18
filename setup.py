import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="ieugwaspy",
    version="0.1.1",
    author="Tom Gaunt",
    author_email="tom@biocompute.org.uk",
    description="Python interface to IEU GWAS database API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MRCIEU/ieugwaspy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["requests"],
)
