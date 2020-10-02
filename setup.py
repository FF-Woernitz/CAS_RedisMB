import setuptools
from pkg_resources import parse_requirements

setuptools.setup(
    name="CASlib",
    version="0.0.1",
    author="FF Woernitz",
    author_email="technik@ff-woernitz.de",
    description="The redis message borker lib used in the CAS system",
    url="https://github.com/FF-Woernitz/CAS_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_reqs=parse_requirements('requirements.txt'),
    python_requires='>=3.6',
)