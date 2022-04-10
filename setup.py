from setuptools import setup, find_packages

def read_requirements(): 
    with open ('requirements.txt') as req:
        content = req.read() 
        requirements = content.split('\n')
    return requirements #return list of strings


setup(
    name='jpd',
    version='1.0',
    py_modules=["jpd"],
    packages = find_packages(),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'jpd=jpd.cli:cli'
        ],
    },
)
