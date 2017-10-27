from setuptools import setup

setup(
    name='pandaspread',
    version='0.1.0',
    description='Write Pandas DataFrame to Google Sheets.',
    author='Takuya Arita',
    author_email='takuya.arita@gmail.com',
    url='https://github.com/ariarijp/pandaspread',
    packages=[
        'pandaspread',
    ],
    license='MIT',
    install_requires=[
        'pandas',
        'google-api-python-client',
    ],
)
