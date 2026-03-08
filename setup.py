from setuptools import setup, find_packages

setup(
    name="ai-talent-matching-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic",
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "matching-agent=src.matching_agent:main",
        ],
    },
    python_requires=">=3.8",
)