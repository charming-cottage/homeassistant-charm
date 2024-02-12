Charmed HomeAssistant
#####################

|test-status-badge|_

Overview
========

A machine charm for `HomeAssistant`_ built with the `HomeAssistant Snap`_ and
ready to run on top of `juju`_.

Open source home automation that puts local control and privacy first.
Powered by a worldwide community of tinkerers and DIY enthusiasts.
Perfect to run on a Raspberry Pi or a local server.

Checklist
=========

☐ user-defined config files

☐ preserve config files (peer relation data bag)

☐ usb access for Z-Wave and Zigbee controllers

☐ license

☐ unit tests

☐ publish charm to charmhub

Requirements
============

The charm is meant to be deployed using ``juju>=3.1``.

Usage
=====

The HomeAssistant charm is not yet available on charmhub, so can be downloaded
from the `GitHub Releases page`_ or built with `charmcraft`_

.. code-block:: shell

    charmcraft pack

It can be deployed with

.. code-block:: shell

    juju deploy ./homeassistant_ubuntu-22.04-amd64.charm

To access the web interface on port 8123, expose the charm:

.. code-block:: shell

    juju expose homeassistant

HomeAssistant will be available at ``<server-ip>:8123``.

Contributing
============

Contributions are encouraged! Please see the `HACKING`_ doc and
`Juju SDK docs`_ for guidelines on enhancements to this charm
following best practice guidelines.

.. _`charmcraft`: https://github.com/canonical/charmcraft
.. _`GitHub Releases page`: https://github.com/charming-cottage/homeassistant-charm/releases
.. _`HACKING`: ./HACKING.rst
.. _`juju`: https://juju.is/
.. _`Juju SDK docs`: https://juju.is/docs/sdk
.. |test-status-badge| image:: https://github.com/charming-cottage/homeassistant-charm/actions/workflows/tests.yaml/badge.svg?branch=main
.. _test-status-badge: https://github.com/charming-cottage/homeassistant-charm/actions/workflows/tests.yaml
.. _`HomeAssistant`: https://www.home-assistant.io/
