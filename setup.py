from setuptools import find_packages, setup

setup(
    name='airflow_mailgun_plugin',
    version='0.0.0',
    description='A hook and operator for the Mailgun Email Validation API',
    long_description=open('README.rst').read(),
    url='https://github.com/airflow-plugins/mailgun_plugin',
    author='Astronomer',
    author_email='taylor@astronomer.io',
    maintainer='Astronomer',
    maintainer_email='taylor@astronomer.io',
    license='MIT License',
    packages=find_packages(exclude=['tests']),
    install_requires=open('requirements.txt').read().split('\n'),
)
