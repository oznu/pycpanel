from distutils.core import setup

setup(
    name='pycpanel',
    version='0.1.1',
    author='OZNU',
    author_email='dev@oz.nu',
    packages=['pycpanel',],
    url='https://github.com/oznu/pycpanel',
    license='LICENSE.txt',
    description='Python module for the cPanel API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests >= 2.0.0",
    ],
)
