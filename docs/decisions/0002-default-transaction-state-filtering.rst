0002 Transaction state filter defaults
######################################

Status
******

**Accepted** (May 2023)

Context
*******

The enterprise-subsidy service transaction ``list`` view allows for filtering by transaction state,
e.g. one may filter for only ``committed`` transactions.  Clients of the service require this functionality
to determine which transactions actually count toward caluclations that determine if the
already-consumed quantity from a subsidy's transactions are below some consumption limit.  For example,
the ``SubsidyAccessPolicy`` API often wants to know the total amount already spent via subsidy transactions
that are related to some particular policy instance, or perhaps the total amount spent by some learner
within a policy.

**We generally don't want "failed" transactions considered in these calculations.**

The transactions API does not do any "sane defaults" filtering - it allows clients to filter for
multiple states via query params, but if none are provided, the resulting payload may contain
transactions in **any** state.
See https://github.com/openedx/enterprise-subsidy/blob/main/docs/decisions/0006-transaction-api-state-filtering.rst
for further details.

Decision
********

Because *this* client is the primary mechanism through which the subsidy access policy API
makes requests of the transactions API, we'll modify this client to request a transactions
in a certain set of states by default.  Those states are ``committed``, ``pending``, and ``created``, i.e.
every state except ``failed``.

This is the same set of states considered when calculating the balance for a subsidy's ledger.
See https://github.com/openedx/openedx-ledger/blob/main/docs/decisions/0006-ledger-balance-transaction-states.rst
for an explanation of why we consider these states.

Consequences
************

We're making the client "do the right thing" out of the box by requesting only non-failed states
by default.  The client function to request filtered transactions still allows the caller
to filter for specific states by doing e.g. ``list_subsidy_transactions(transaction_states='failed')``.
But if the caller specifies *no* states, they'll get a filter for the non-failed transactions states.


Rejected Alternatives
*********************

Having the transactions API control what the sane defaults are.  This is suggested as an anti-pattern
in ``django-filters``, https://django-filter.readthedocs.io/en/stable/guide/tips.html#using-initial-values-as-defaults.
