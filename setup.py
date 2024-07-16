from setuptools import setup

setup(
    name='image_converter',
    version='1.0',
    scripts=['image_converter.py'],
    install_requires=[
        'Pillow',
        'loguru',
    ],
    entry_points={
        'console_scripts': [
            'image_converter=image_converter:main',
        ],
    },
    description='A simple image converter script',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
