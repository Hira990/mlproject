from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    return requirements  
        
setup(
    name='mlproject',
    version='0.0.1',
    packages=find_packages(),
    author = 'Hira',
    author_email= 'hkhalid99@gmail.com',
    install_requires=get_requirements('requirements.txt')
)
