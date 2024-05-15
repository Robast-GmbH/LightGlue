from setuptools import setup, find_packages

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()

setup(
    name='lightglue_robast',
    version='0.0',
    description='LightGlue: Local Feature Matching at Light Speed',
    #author='Philipp Lindenberger, Paul-Edouard Sarlin',
    packages=find_packages(),
    python_requires='>=3.6',
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
   # url='https://github.com/cvg/LightGlue/',
    # install_requires=requirements,
)