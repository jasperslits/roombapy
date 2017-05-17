from setuptools import find_packages, setup


setup(
    name='Roomba980-Python',
    version='1.0',
    license='MIT',
    description='Python program and library to control iRobot Roomba 980 Vacuum Cleaner',
    author_email='nick.waterton@med.ge.com',
    url='https://github.com/NickWaterton/Roomba980-Python',
    packages=find_packages(),
    # package_data={'': ['resources/img/*.png', '']},
    install_requires=['numpy', 'opencv-python', 'paho-mqtt', 'pillow', 'six'],
    entry_points={
        'console_scripts': ['roomba=roomba.roomba:main', 'getpassword=roomba.getpassword:main']
    }
)
