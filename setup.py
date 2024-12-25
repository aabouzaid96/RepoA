from setuptools import setup, find_packages

setup(
    name="repoa",  # Name of the package
    version="0.1",
    packages=find_packages(),  # Automatically find packages
    include_package_data=True,  # Include static and template files
    install_requires=[
        "django>=3.2"  # Specify Django version compatibility
    ],
    author="abouzaid",
    author_email="aabouzaid96@gmail.com",
    description="A reusable Django app",
    url="http://example.com/django-app-a",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
