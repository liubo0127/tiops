from setuptools import setup, find_packages  
  
setup(  
    name = "tiops", 
    version = "0.1.0",
    keywords = ("tidb", "tikv"),
    description = "eds sdk",
    license = "MIT Licence",
    url = "http://www.pingcap.com",
    packages = find_packages(),
    install_requires = [
        'yaml-config',
        'IPy',
    ],
    scripts = ['tiops'],
    entry_points = {  
        'console_scripts': [  
            'test = test.help:main'  
        ]  
    }  
)
