#!/usr/bin/env python3
from pathlib import Path

import setuptools
from skbuild import setup
from setuptools import find_packages

this_dir = Path(__file__).parent

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

module_name = "wyoming_whisper_cpp"
module_dir = this_dir / module_name
data_files = []

version_path = module_dir / "VERSION"
data_files.append(version_path)
version = version_path.read_text(encoding="utf-8").strip()

# Add scikit-build as a build requirement
setup_requires = ["scikit-build", "cmake>=3.16"]

# -----------------------------------------------------------------------------

setup(
    name=module_name,
    version=version,
    description="Wyoming Server for whisper.cpp",
    url="http://github.com/rhasspy/wyoming-whisper-cpp",
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    license="MIT",
    packages=find_packages(),
    package_data={module_name: [str(p.relative_to(module_dir)) for p in data_files]},
    install_requires=requirements,
    setup_requires=setup_requires,
    cmake_install_dir=module_name,
    cmake_source_dir="whisper.cpp",
    cmake_args=[
        "-DBUILD_SHARED_LIBS=OFF",
        "-DWHISPER_BUILD_STATIC=ON",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="rhasspy wyoming whisper stt",
    entry_points={
        "console_scripts": ["wyoming-whisper-cpp = wyoming_whisper_cpp.__main__:run"]
    },
)
