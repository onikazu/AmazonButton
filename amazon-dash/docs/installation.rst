.. highlight:: console

============
Installation
============


Stable release
--------------

To install amazon-dash, run these commands in your terminal:

.. code-block:: console

    $ pip install amazon_dash
    $ sudo python -m amazon_dash.install

This is the preferred method to install amazon-dash, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


Other releases
--------------
You can install other versions from Pypi using::

    $ pip install amazon-dash==<version>
    $ sudo python -m amazon_dash.install

For versions that are not in Pypi (it is a development version)::

    $ pip install git+https://github.com/Nekmo/amazon-dash.git@<branch>#egg=amazon-dash
    $ sudo python -m amazon_dash.install


Distro packages
---------------

Arch Linux
``````````
If you use Arch Linux or an Arch Linux derivative, you can install Amazon Dash from
`AUR <https://aur.archlinux.org/packages/amazon-dash-git/>`_. For example if you use yaourt::

    $ yaourt -S amazon-dash-git


From sources
------------

The sources for amazon-dash can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/Nekmo/amazon-dash

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/Nekmo/amazon-dash/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install
    $ sudo python -m amazon_dash.install


.. _Github repo: https://github.com/Nekmo/amazon-dash
.. _tarball: https://github.com/Nekmo/amazon-dash/tarball/master
