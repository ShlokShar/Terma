from setuptools import setup, find_packages

setup(
    name="terma",
    version="0.1.0",
    description="A natural language terminal assistant that translates plain English into real terminal commands for Linux, macOS, and Windows.",
    author="Shlok Sharma",
    author_email="shlokrma@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer[all]",
        "python-dotenv",
        "requests",
        "openai",
    ],
    entry_points={
        "console_scripts": [
            "terma=terma.main:app",
        ],
    },
    python_requires=">=3.7",
)