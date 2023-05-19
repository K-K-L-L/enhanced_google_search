import setuptools

setuptools.setup(
    name="enhanced_google_search",
    version="0.1",
    description="An enhanced google search library",
    author="KKLL",
    url="https://github.com/K-K-L-L/google_search_py",
    long_description=str(open("README.md", "r", encoding="utf-8").read()),
    long_description_content_type="text/markdown",
    keywords="googlesearch.py, enhanced_google_search, python google search, google search pypi, google api",
    package_dir={"": "src"},
    install_requires=["httpx"]
)
