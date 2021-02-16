from distutils.core import setup
import setuptools

with open("README.md", "r") as f:
    long_description = fh.read()
    
setup(
  name = 'caffeination',
  packages = ['caffeination'],
  version = '0.1', 
  license='MIT',
  description = 'Caffeination makes sure your computes does not go to sleep. It is a sleep preventer.',
  long_description = long_description
  author = 'Antonio Raffaele Iannaccone',                   # Type in your name
  author_email = 'antonio@ariseo.sk',      # Type in your E-Mail
  url = 'https://github.com/neisor/caffeination',   # Provide either the link to your github or to your website
  keywords = ['caffeination', 'caffe', 'caffeine', 'sleep preventer'],   # Keywords that define your package best
  install_requires=[
          'pyautogui'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  py_modules=["caffeination.py"],
  package_dir={'': ''}
)
