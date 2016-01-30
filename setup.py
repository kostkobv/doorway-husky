from distutils.core import setup

setup(
    name='doorway-husky',
    version='0.0.1',
    packages=[''],
    install_requires=['python-linkedin',
                      'openpyxl',
                      'enum34'],
    url='https://github.com/kostkobv/doorway-husky',
    license='Apache 2.0',
    author='bv',
    author_email='bohdan.kostko@gmail.com',
    description='Checks data on linkedin from provided .xlsx file and corrects if it is not so.'
)
