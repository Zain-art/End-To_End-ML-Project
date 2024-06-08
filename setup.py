from typing import List
from setuptools import find_packages,setup

HYPEN_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements





setup(
    name='mlproject',
    version='0.0.1',
    author='Zain khan',
    author_email='za870411@gmail.com',
    package=find_packages(),
    # install_requires=['numpy','pandas','matplotlib','seaborn','scikit-learn']
    install_requires=get_requirements('requirements.txt')
)

