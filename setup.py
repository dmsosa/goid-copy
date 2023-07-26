from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = "1.0.0"

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file

try:
    import pypadoc
    if path.isfile('README.rst'):
        print('README.rst already exist.')
        print('NOT REFRESHING README.rst')
    else:
        long_description = 
        pypandoc.convert_file('README.md', 'rst')
        with open('README.rst','w') as f:
            f.write(long_description)

    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    print("Error:{}:{}".format(type(e), e))
    print("NOT REFRESHING README.rst")
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

# get the dependencias and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='google_images_download',
    version=__version__,
    description="A goidcopy of the hardikvasa package 'google images download' that we used as model to learn to code! ",
    long_description=long_description,
    url='https://github.com/dmsosa/goid-copy',
    download_url='https://github.com/dmsosa/goid-copy/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='dmsosa',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='dmsosa@learning.com',
    entry_points={
        'console_scripts': [
            'goidcopy = goidcopy.__init__:main'
        ]},

)