from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='gtr',
      version='0.1.1',
      description='A Python interface to the Gateway To Research GTR-2 API.',
      long_description=readme(),
      url='http://github.com/nestauk/gtr',
      author='James Gardiner',
      author_email='james.gardiner@nesta.org.uk',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'requests==2.9.1',
      ],
      classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
      ])