from setuptools import setup, find_packages

setup(
    name = "dundie",
    version = "0.1.0",
    description="Reward point system for Dunder Mifflin",
    author="Tiago Turquette",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)
