import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knock-recognizer",
    version="0.0.7",
    author="Team lyd og signal",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oyvinyg/knock-recognizer",
    packages=setuptools.find_packages(".", exclude=["test*"]),
    install_requires=["pyaudio", "SpeechRecognition"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
