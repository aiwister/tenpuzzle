from setuptools import setup

setup(
        install_requires=["numpy"],
        entry_points={
            "console_scripts":[
                "tenpuzzle = tenpuzzle:task"
            ]
        }
)