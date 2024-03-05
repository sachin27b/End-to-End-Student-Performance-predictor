from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This Function will return the list of packages required
    '''
    requirements = []
    HYPHEN_E_DOT = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
setup(
    name='project',
    version='1.0.0',
    author='Sachin Bahuleyan',
    author_email='t22060@students.iitmandi.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)