from setuptools import setup

setup(
    packages=["intake_project"],
    entry_points={
        "intake.imports": [
            "data = intake_project:ExampleData",
            "reader = intake_project:ExampleReader",
        ],
    },
    include_package_data=True,
    install_requires=["intake"],
)
