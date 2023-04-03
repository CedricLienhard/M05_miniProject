from setuptools import setup, find_packages


def load_requirements(f):
    retval = [str(k.strip()) for k in open(f, "rt")]
    return [k for k in retval if k and k[0] not in ("#", "-")]


setup(
    name="src_bostonHousingWineQuality",
    version="0.6.2",
    description="M05_miniProject",
    url="https://github.com/CedricLienhard/M05_miniProject",
    license="MIT",
    author="Cedric Lienhard, Mustapha Al-Dabboussi",
    author_email="lienhard.cedric@gmail.com",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
    
    #creates a command line script 'src-main' that can be executed from the terminal. The script is linked to the main function in the src.main module. 
    #When you run the command src-main from the terminal, it will execute the main function in the src.main module.
    entry_points={"console_scripts": ["src-main = src.main:main"]}, 
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
