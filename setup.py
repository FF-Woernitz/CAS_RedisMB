import setuptools

setuptools.setup(
    name="RedisMBlib", # Replace with your own username
    version="0.0.1",
    author="FF Woernitz",
    author_email="technik@www.ff-woernitz.de",
    description="The redis message borker lib used in the CAS system",
    url="https://github.com/FF-Woernitz/CAS_RedisMB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)