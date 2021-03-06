from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Kittyscript',
  version='2.9.3',
  description='Assist mode for python',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Anahad Khosa',
  author_email='hahacoolguystaco@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Assist mode', 
  packages=find_packages(),
  install_requires=[''],
  long_description_content_type='text/markdown',
  License_content_type='text/markdown'
)