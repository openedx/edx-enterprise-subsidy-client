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

[0.4.4]
*******
* feat: add support for deposit creation (ENT-9133)

[0.4.3]
*******
* feat: adding new subsidy client method to fetch subsidy aggregate data

[0.4.2]
*******
* Switch from ``edx-sphinx-theme`` to ``sphinx-book-theme`` since the former is
  deprecated
* Add python 3.12 support

[0.4.1]
*******
* chore: add a unit test for ``create_subsidy_transaction()``.

[0.4.0]
*******
* feat: allow requested prices for v2 transaction creation.

[0.3.7]
*******
* feat: upgrade many python dependencies, notably Django 3.2.19

[0.3.6]
*******
* feat: pass idempotency key during transaction creation (pt. 2)

[0.3.5]
*******
* feat: pass idempotency key during transaction creation

[0.3.3]
*******
* allow additional query params, like ``page_size``, to be passed through to listing endpoints.

[0.3.3]
*******
* admin-list transactions will also be filtered by ``created`` state by default.
* Adds an ADR explaining the default states for which this client filters transactions.

[0.3.2]
*******
* admin-list transactions will ask to be filtered for only `committed` and `pending` states by default.
  Caller may specify other valid states (e.g. `failed` or `created`).

[0.3.1]
*******
* fix: correctly pass ``subsidy_uuid`` to subsidy API V2 endpoint string format.

[0.3.0]
*******
* feat: add new client for v2 transaction endpoint.

[0.2.6]
*******
* feat: transaction endpoint accepts `lms_user_id` instead of `learner_id`

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
