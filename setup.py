'''
The setup-py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages , setup
from typing import List

requirements_lst : List[str] = []
def get_requirements() -> List[str]:
    """
    This function will return list of requirements
    """

    try:
        with open("requirements.txt" , 'r') as file:
            ## Read the lines from file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirements = line.strip()
                ## Egnore the empty and  -e .
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

setup(
    name="NetworkSecurity" , 
    author="PandharinathMaske" , 
    version="0.0.1" , 
    author_email="pandhari2527@gmail.com" , 
    packages=find_packages() , 
    requires=get_requirements()
)


