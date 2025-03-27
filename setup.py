from setuptools import setup

setup(
    name="fast-create",
    version="0.1",
    py_modules=["fast_create"],
    install_requires=['fastapi', 'sqlmodel', 'fastapi_mail', 'pydantic', 'jose','oauth2', 'passlib', 'sqlalchemy'],
    entry_points={
        "console_scripts": [
            "create-fastapi=fast_create:main",
        ],
    },
)
