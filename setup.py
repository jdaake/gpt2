from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='gpt',
    version='2.0.0',
    description='OpenAI Chat Completion API CLI Utility',
    long_description=readme,
    author='Jordan Daake',
    author_email='daakejl@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['openai'],
    entry_points={
        'console_scripts': 'gpt=gpt.cli:main',
    }
)
