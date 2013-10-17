from distutils.core import setup

setup(
  name='cabinet',
  version='0.1.1',
  description="cabinet",
  url='http://github.com/adeel/cabinet',
  author='Adeel Khan Yusufzai',
  author_email='kadeel@gmail.com',
  packages=['cabinet'],
  scripts=['bin/cabinet'],
  install_requires=['termcolor', 'pymongo'],
  license='MIT',
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Operating System :: POSIX',
    'Topic :: Utilities',
  ]
)