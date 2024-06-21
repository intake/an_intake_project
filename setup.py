from setuptools import setup

setup(
    packages=["intake_project"],
    entry_points={
        "intake.imports": [
            "myclass = intake_project:MyClass",
        ],
    },
    include_package_data=True,
    install_requires=["intake"],
)
