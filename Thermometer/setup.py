from setuptools import find_packages, setup

package_name = 'practice_py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gidong',
    maintainer_email='gd.baek1495@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'pub=practice_py_pubsub.temperature_publisher:main',
            'sub=practice_py_pubsub.temperature_subscriber:main'
        ],
    },
)
