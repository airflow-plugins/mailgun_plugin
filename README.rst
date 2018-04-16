Airflow Mailgun Plugin
======================

.. image:: https://api.codeclimate.com/v1/badges/6216131319f2a4e75718/maintainability
   :target: https://codeclimate.com/github/airflow-plugins/mailgun_plugin/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/6216131319f2a4e75718/test_coverage
   :target: https://codeclimate.com/github/airflow-plugins/mailgun_plugin/test_coverage
   :alt: Test Coverage

An Airflow hook and operator to validate a list of emails using the `Mailgun Email Validation API <https://www.mailgun.com/email-validation>`_.

An `example Mailgun validation DAG <https://github.com/airflow-plugins/Example-Airflow-DAGs/blob/master/poc/mailgun_validation_example.py>`_ is available as well.

Setup
-----

In the root of your Airflow project run:

.. code-block:: console

    $ pip install -U git+https://github.com/airflow-plugins/mailgun_plugin.git@v0.0.1

Quickstart
----------

1. Create an S3 bucket ``my_bucket`` on AWS or use an existing one.

2. Upload a list of contacts ``contacts.json`` to it which consists of newline-delimited JSON (ndjson):

.. code-block:: json

    {"id": 123, "email": "foo@example.com"}
    {"id": 456, "email": "bar@example.com"}
    {"id": 96, "email": "info@example.com"}
    {"id": 433, "email": "Real Person <rperson@example.com>"}

3. Create an S3 connection in Airflow:

.. code-block::

    - Conn Id: aws_s3
    - Conn type: S3
    - Login: <AWS Access Key ID>
    - Password: <AWS Secret Access Key>

4. Create a Mailgun connection in Airflow:

.. code-block::

    - Conn Id: mailgun_api
    - Conn type: (empty)
    - Login: <Mailgun Public Validation Key>

5. Add a task to your DAG like:

.. code-block:: python

    dag = DAG(...)

    email_validator = EmailValidationOperator(
        task_id='email_validator',
        mailgun_conn_id='mailgun_api',
        aws_conn_id='aws_s3',
        s3_bucket_name='my_bucket',
        s3_key_source='contacts.json',
        dag=dag,
    )

Notes
-----

Mailgun Email Validation Pricing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Your first 100 email validations per month are free; beyond that, see the `Mailgun Pricing page <https://www.mailgun.com/pricing>`_.

Test
----

Install:

.. code-block:: console

    $ git clone https://github.com/airflow-plugins/mailgun_plugin
    $ cd mailgun_plugin
    $ pip install -U -r requirements_test.txt

Run tests:

.. code-block:: console

    $ pytest

Run coverage:

.. code-block:: console

    $ pytest --cov=mailgun_plugin

To show uncovered lines:

.. code-block:: console

    $ coverage report --include=mailgun_plugin/* --show-missing

Development
-----------

Switch to the root of your Airflow project.

To install:

.. code-block:: console

    $ git clone https://github.com/airflow-plugins/mailgun_plugin plugins/mailgun_plugin
    $ pip install -U -r plugins/mailgun_plugin/requirements_dev.txt
