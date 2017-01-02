from setuptools import setup, find_packages

setup(
    name='er',
    version='0.2',

    description='Generate data that matches a given regular expression.',
    author="Simon Engledew",
    author_email="simon@engledew.com",
    url="https://github.com/simon-engledew/python-er",

    install_requires=[
    ],
    extras_require={
        'tests': [
            'nose'
        ],
        ':python_version < "3.4"': [
            "enum34"
        ]
    },
    entry_points={
        'console_scripts': [
            'er = er:main',
        ],
    },
    zip_safe=True,
    include_package_data=False,
    packages=find_packages(),
    license='MIT',
    keywords=[
        're',
        'test',
        'testing',
        'data',
        'fake',
        'regular expression'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
)
