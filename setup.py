from distutils.core import setup

setup(
    name='pycpanel',
    version='0.1.5',
    author='oznu',
    author_email='dev@oz.nu',
    packages=['pycpanel',],
    url='https://github.com/oznu/pycpanel',
    license='Apache License',
    description='Python Client for the cPanel API and CSF.',
    long_description=open('README.rst').read(),
    install_requires=[
        "requests >= 2.0.0",
    ],
)
