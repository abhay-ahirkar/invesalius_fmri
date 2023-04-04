from setuptools import setup, find_packages

setup(
    name='invesalius-fmri',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'wxpython',
        'nibabel',
    ],
    author='abhay-ahirkar',
    author_email='abhayahirkar2@gmail.com',
    description='InVesalius fMRI support',
    long_description='A package that adds fMRI support to InVesalius, allowing for simultaneous visualization of functional and structural MRI data.',
    url='https://github.com/abhay-ahirkar/invesalius_fmri',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
