from setuptools import setup
from pathlib import Path

subpackage_path = (Path(__file__).parent / "deps" / "subpackage").resolve()

setup(
    name="mainpackage",
    version="0.1",
    packages="mainpackage",
    install_requires=[
        f"subpackage @ git+file://{subpackage_path}#subpackage-0.1",
    ],
)
