import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scan2gif",
    version="0.1",
    author="Léon Lenclos",
    author_email="leon.lenclos@gmail.com",
    description="Simple command line tool to quikly make gif from scans",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license = 'LICENSE',
    url="https://github.com/LeonLenclos/scan2gif",
    keywords = [
        'gif',
        'scan',
    ],
    packages=['scan2gif'],
    entry_points={
        'console_scripts': [
            'scan2gif=scan2gif.script:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)