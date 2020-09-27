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
    python_requires='>=3.6',
)