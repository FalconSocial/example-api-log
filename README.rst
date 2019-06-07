Example API Log
===============

To set up:

.. code:: bash

  pip install -r requirements-dev.txt

To run using the development runtime:

.. code:: bash

  python run.py

or with Gunicorn:

.. code:: bash

  gunicorn --log-level=debug --workers=1 --bind=0.0.0.0:8080 run:app --access-logfile=-

Then go here: http://localhost:8080/api/v1/basic/ping
