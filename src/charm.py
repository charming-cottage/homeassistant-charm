#!/usr/bin/env python3

"""Charm the application."""

import logging
import subprocess
import sys

import ops

logger = logging.getLogger(__name__)


class HomeAssistantCharm(ops.CharmBase):
    """Charm the application."""

    def __init__(self, *args):
        super().__init__(*args)
        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.start, self._on_start)
        self.framework.observe(self.on.stop, self._on_stop)

    def _on_start(self, event: ops.StartEvent):
        """Handle start event."""
        subprocess.run(["snap", "start", "home-assistant-snap"])
        self.unit.status = ops.ActiveStatus("running")

    def _on_stop(self, event: ops.StopEvent):
        self.unit.status = ops.MaintenanceStatus("stopping")
        subprocess.run(["snap", "stop", "home-assistant-snap"])

    def _on_install(self, event: ops.InstallEvent) -> None:
        self.unit.status = ops.MaintenanceStatus("home assistant snap")
        subprocess.run(
            ["snap", "install", "home-assistant-snap"],
            text=True,
            stdout=sys.stdout,
            stderr=sys.stderr,
            check=True,
        )
        self.unit.open_port("tcp", 8123)
        self.unit.status = ops.ActiveStatus("Installed")


if __name__ == "__main__":  # pragma: nocover
    ops.main(HomeAssistantCharm)  # type: ignore
