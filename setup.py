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

# from setuptools import setup, find_packages

# setup(
#     name='enhanced_google_search',
#     version='0.1',
#     description='An enhanced google search library',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     author='Rian',
#     author_email='rianmakt2008@gmail.com',
#     url='https://github.com/K-K-L-L/google_search_py',
#     packages=find_packages('src'),
#     package_dir={'': 'src'},
#     install_requires=[
#         'httpx'
#     ],
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#     ],
# )