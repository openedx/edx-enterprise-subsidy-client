Change Log
##########

..
   All enhancements and patches to edx_enterprise_subsidy_client will be documented
   in this file.  It adheres to the structure of https://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (https://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
**********

* Switch from ``edx-sphinx-theme`` to ``sphinx-book-theme`` since the former is
  deprecated

[0.2.5]
*******
* feat: redemption metadata.

[0.2.4]
*******
* fix: don't directly access a status code on a failed response for logging.

[0.2.3]
*******
* DON'T be flexible about settings variable names for client initialization.

[0.2.2]
*******
* str() incoming UUID arguments


[0.2.1]
*******
* Be flexible about settings variable names for client initialization.

[0.2.0]
*******
* Add implementation for many of the client methods; currently defering on unit tests.
* Add a ``scripts/e2e.py`` script for end-to-end testing between enterprise-subsidy and edx-enterprise.

[0.1.0] - 2023-02-01
********************

Added
=====

* First release on PyPI.
