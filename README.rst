edx-enterprise-subsidy-client
#############################

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

Client for interacting with the enterprise-subsidy service.

Getting Started
***************

Developing
==========

One Time Setup
--------------
.. code-block::

  # Clone the repository into your ``[DEVSTACK]/src/`` folder
  git clone git@github.com:openedx/edx-enterprise-subsidy-client.git
  # Use a service container that would reasonably install this client, e.g.
  cd [DEVSTACK]/enterprise-subsidy && make app-shell
  cd /edx/src/edx-enterprise-subsidy-client

  # Set up a virtualenv in a ``venv/`` directory
  # You might need to install virtualenv first:
  # apt-get update
  # apt-get install -y virtualenv
  virtualenv venv/
  make requirements

  # Ensure things are looking ok by running tests
  make test

Every time you develop something in this repo
---------------------------------------------
.. code-block::

  # Grab the latest code
  git checkout main
  git pull

  # Use a service container that would reasonably install this client, e.g.
  cd [DEVSTACK]/enterprise-subsidy && make app-shell
  cd /edx/src/edx-enterprise-subsidy-client

  # Activate the virtualenv
  source venv/bin/activate

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit ...
  git push

  # Open a PR and ask for review.

Deploying
=========

TODO: How can a new user go about deploying this component? Is it just a few
commands? Is there a larger how-to that should be linked here?

PLACEHOLDER: For details on how to deploy this component, see the `deployment how-to`_

.. _deployment how-to: https://docs.openedx.org/projects/edx-enterprise-subsidy-client/how-tos/how-to-deploy-this-component.html

Getting Help
************

Documentation
=============

PLACEHOLDER: Start by going through `the documentation`_.  If you need more help see below.

.. _the documentation: https://docs.openedx.org/projects/edx-enterprise-subsidy-client

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

More Help
=========

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the
community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide.

https://github.com/openedx/edx-enterprise-subsidy-client/issues

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help

License
*******

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to have a discussion about your new feature idea with the maintainers prior to
beginning development to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://open-edx-backstage.herokuapp.com/catalog/default/component/edx-enterprise-subsidy-client

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@openedx.org.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/edx-enterprise-subsidy-client.svg
    :target: https://pypi.python.org/pypi/edx-enterprise-subsidy-client/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/openedx/edx-enterprise-subsidy-client/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/openedx/edx-enterprise-subsidy-client/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/openedx/edx-enterprise-subsidy-client/coverage.svg?branch=main
    :target: https://codecov.io/github/openedx/edx-enterprise-subsidy-client?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/edx-enterprise-subsidy-client/badge/?version=latest
    :target: https://edx-enterprise-subsidy-client.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/edx-enterprise-subsidy-client.svg
    :target: https://pypi.python.org/pypi/edx-enterprise-subsidy-client/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/openedx/edx-enterprise-subsidy-client.svg
    :target: https://github.com/openedx/edx-enterprise-subsidy-client/blob/main/LICENSE.txt
    :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
