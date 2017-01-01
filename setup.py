from setuptools import setup, find_packages

setup(
    name='er',
    version='0.1',

    description='Generate data that matches a given regular expression.',
    author="Simon Engledew",
    author_email="simon@engledew.com",
    url="https://github.com/simon-engledew/python-er",

    install_requires = [
    ],
    extras_require = {
      'tests': [
        'nose'
      ],
      ':python_version < "3.4"': ["enum34"]
    },
    entry_points = {
        'console_scripts': [
            'er = er:main',
        ],
    },
    zip_safe=True,
    include_package_data=False,
    packages=find_packages(),
    license='MIT',
    keywords = [
        're',
        'test',
        'testing',
        'data',
        'fake',
        'regular expression'
    ],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
