from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.3"
AUTHOR="Nawaz"
DESCRIPTION="This is my first machine learning project ( House Prediction )"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function will return a list of requiremnets
    mention in requirements.txt

    Return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages,#["housing"]
install_requires=get_requirements_list()
)
