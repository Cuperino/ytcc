#!/usr/bin/env python3

from glob import glob
from pathlib import Path
from subprocess import run
from setuptools import setup
import ytcc


def compile_translations():
    po_files = glob("po/*.po")
    package_data = []
    for file in po_files:
        lang = file[3:][:-3]
        package_data_file = "resources/locale/" + lang + "/LC_MESSAGES/ytcc.mo"
        out_file = Path("ytcc").joinpath(package_data_file)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        if run(["msgfmt", "-o", str(out_file), file]).returncode == 0:
            package_data.append(package_data_file)

    return package_data


setup(
    name="ytcc",
    description="A subscription wrapper for youtube-dl playlists",
    long_description=ytcc.__doc__,
    version=ytcc.__version__,
    url="https://github.com/woefe/ytcc",
    author=ytcc.__author__,
    author_email=ytcc.__email__,
    license=ytcc.__license__,
    packages=["ytcc"],
    install_requires=["youtube_dl", "click"],
    entry_points="""
        [console_scripts]
        ytcc=ytcc.cli:main
        """,
    package_data={
        "ytcc": compile_translations()
    },
)
