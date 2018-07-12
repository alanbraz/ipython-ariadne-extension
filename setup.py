import setuptools
from typecheck import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipython-typecheck-extension",
    version=__version__,
    author="Alan Braz",
    author_email="alanbraz@gmail.com",
    description="IPython typecheck extension for notebook\' multiple cells.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alanbraz/ipython-typecheck-extension",
    packages=setuptools.find_packages(),
    #packages=['typecheck-extension'],
    install_requires=['mypy'],
    zip_safe=False
)
