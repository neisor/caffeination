import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
    
setuptools.setup(
  name = 'caffeination',
  version = '0.1', 
  license='MIT',
  description = 'Caffeination makes sure your computes does not go to sleep. It is a sleep preventer.',
  long_description = long_description,
  long_description_content_type="text/markdown",
  author = 'Antonio Raffaele Iannaccone',
  author_email = 'antonio@ariseo.sk',
  url = 'https://github.com/neisor/caffeination',
  keywords = ['caffeination', 'caffe', 'caffeine', 'sleep preventer'],
  install_requires=[
          'pyautogui'
      ],
  packages=setuptools.find_packages(),
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
  python_requires='>=3.6',
  entry_points={
      'console_scripts': [
          'caffeination=caffeination:main'
          ]
      }
)
