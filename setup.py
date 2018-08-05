import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Genclass",
    version="0.0.7",
    author="Mohan Chand Peddapuli",
    author_email="mohanroger63@gmail.com",
    description="Generate classes there itself. Just pass class name and fields",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohan78/Genclass",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
