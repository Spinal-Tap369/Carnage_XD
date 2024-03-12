from setuptools import setup, find_packages

setup(
    name="Carnage_in_Hell",
    version="1.0.0",
    description="A simple Space Shooter game",
    long_description="same",
    author=["Arnold Joseph","Samuel Verghese","Karan Zaveri","Harsheta Murthy"]
    author_email=["arnold.joseph@stud.srh-campus-berlin.de","samuel.malayilverghese@stud.srh-campus-berlin.de","karan.zaveri@stud.srh-campus-berlin.de","harshethamurthy.keshavmurthy@stud.srh-campus-berlin.de"]
    packages=find_packages(),  # Automatically find all packages
    install_requires=['pygame'],  # Use a list for install_requires
    url="https://github.com/Spinal-Tap369/Carnage_XD",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Arcade",
    ],
    entry_points={'console_scripts':['cih = Carnage_in_Hell.main:run'],},
    )
