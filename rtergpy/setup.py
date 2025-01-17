from setuptools import setup

setup(
    name='rtergpy',
    version='0.2.2a',
    description='A package for real-time processing of Earthquake Energy and duration',
    url='https://github.com/lmjaffe/',
    author='Leah Jaffe',
    author_email='lmjaffe@uvm.edu',
    license='MIT',
    packages=['rtergpy'],
    install_requirements=['pygmt>=0.3.1', 
                        'numpy>=1.0',
                        'matplotlib>=3.3.0',
                        'tqdm',
                        'obspy>=1.2.0',
                        'pandas>=1.2.0',
			'compress_pickle'
                        ],
    classifiers=[ 
        'Development Status :: 2 - Beta',
        'Intended Audience :: Science',
        'Operating System :: OS Independent',
        'Programming Language :: Python :3.9',
        ],
)
