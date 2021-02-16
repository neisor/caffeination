from distutils.core import setup
setup(
  name = 'caffeination',         # How you named your package folder (MyLib)
  packages = ['caffeination'],   # Chose the same as "name"
  version = '0.1', 
  license='MIT',
  description = 'Caffeination makes sure your computes does not go to sleep. It is a sleep preventer.',   # Give a short description about your library
  author = 'Antonio Raffaele Iannaccone',                   # Type in your name
  author_email = 'antonio@ariseo.sk',      # Type in your E-Mail
  url = 'https://github.com/neisor/caffeination',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['caffeination', 'caffe', 'caffeine'],   # Keywords that define your package best
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
)
