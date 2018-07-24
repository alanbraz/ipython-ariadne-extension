import setuptools
from ariadne import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ipython-ariadne-extension",
    version=__version__,
    author="Alan Braz",
    author_email="alanbraz@gmail.com",
    description="IPython WALA/ML (Ariadne) extension for notebook\'s multiple cells.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alanbraz/ipython-ariadne-extension",
    packages=setuptools.find_packages(),
    #packages=['typecheck-extension'],
    # install_requires=['mypy'],
    zip_safe=False
)
