from setuptools import setup

setup(name='runat',
      version='0.1',
      description='A tool for running things at a specific time',
      url='http://github.com/nchodosh/runat',
      author='Nate Chodosh',
      author_email='nchodosh@gmail.com',
      packages=['runat'],
      entry_points = {
        'console_scripts': ['runat=runat:main'],
      },
      install_requires=[
          'python-dateutil', 'python-crontab',
      ],
      zip_safe=False)
