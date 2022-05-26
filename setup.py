from setuptools import find_packages, setup
setup(
    name='metalabblender',
    packages=find_packages(include=['metalabblender']),
    version='0.1.0',
    description='Metalab blender renderer',
    author='Treinetic',
    license='MIT',
    install_requires=['pyjwt'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)