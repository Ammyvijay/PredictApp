from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    '''
    The Get Requirement function will return the list of requirements.
    '''
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n", "") for r in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="predictapp",
    version="0.0.1",
    author="Ammy Vijay",
    author_email="ammyvijay.b@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
