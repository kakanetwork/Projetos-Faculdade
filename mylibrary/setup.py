from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Coloque aqui as dependências necessárias para o seu pacote
    ],
    entry_points={
        'console_scripts': [
            'mylibrary = mylibrary.__main__:main'
        ]
    },
    # Outras configurações do seu pacote
)
