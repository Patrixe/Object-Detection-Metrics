import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="odm-liedtke",
    version="0.0.1",
    author="Patrick Liedtke",
    author_email="",
    description="A small fork of rafaelpadillas object-detection-metric project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Patrixe/Object-Detection-Metrics",
    install_requires=['opencv-python>4.2.0.31'],
    packages=setuptools.find_packages(include=['object_detection_metrics']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)