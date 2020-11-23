import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='parsearg',
    version='0.1.3',
    author='Thomas P. Harte',
    author_email='tharte@cantab.net',
    description='parsearg turns argparse on its head the declarative way',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tharte/parsearg',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
