from setuptools import setup, find_packages

setup(
    name='treejsonapp',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tk==0.1.0",
    ],
    entry_points={
        'console_scripts': [
            'treejsonapp=treejsonapp.gui:construire_gui_json',
        ],
    },
    author="Nathan Pizzetta",
    author_email="nathan.pizzetta@gmail.com",
    description="Application Tkinter pour afficher l'arborescence d'un fichier JSON",
    url="https://github.com/n-pizzetta/treejsonapp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
