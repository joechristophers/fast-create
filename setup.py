from setuptools import setup

setup(
    name="fast-create",
    version="0.1",
    py_modules=["fast_create"],
    install_requires=['fastapi[all]', 'psycopg2', 'sqlmodel', 'fastapi_mail', 'pydantic', "python-jose[cryptography]",'oauth2', 'passlib', 'sqlalchemy'],
    entry_points={
        "console_scripts": [
            "fast-create=fast_create:main",
        ],
    },
)
