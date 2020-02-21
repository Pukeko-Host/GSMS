import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GSMS-Pukeko",
    version="0.0.1",
    author="Pukeko-Host",
    description="https://github.com/Pukeko-Host/GSMS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pukeko-Host/GSMS",
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)