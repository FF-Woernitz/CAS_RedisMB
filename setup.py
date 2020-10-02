import setuptools

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
    install_reqs=
    [
        'redis~=3.5',
        'Logbook~=1.5'
    ],
    python_requires='>=3.6',
)