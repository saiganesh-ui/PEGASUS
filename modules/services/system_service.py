"""
System Service
Project PEGASUS
Author: Sai Ganesh
"""

import platform
import psutil


class SystemService:

    def os_name(self):
        return platform.system()

    def os_version(self):
        return platform.release()

    def processor(self):
        return platform.processor()

    def machine(self):
        return platform.machine()

    def python_version(self):
        return platform.python_version()

    def cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def ram(self):
        return psutil.virtual_memory()

    def disk_usage(self):
        return psutil.disk_usage("/")

    # ----------------------------
    # New wrapper methods
    # ----------------------------

    def cpu(self):
        return f"CPU Usage: {self.cpu_usage()}%"

    def memory(self):
        ram = self.ram()
        return (
            f"RAM Usage: {ram.percent}% "
            f"({ram.used // (1024**3)} GB / {ram.total // (1024**3)} GB)"
        )

    def disk(self):
        disk = self.disk_usage()
        return (
            f"Disk Usage: {disk.percent}% "
            f"({disk.used // (1024**3)} GB / {disk.total // (1024**3)} GB)"
        )

    def system_info(self):
        return (
            f"OS: {self.os_name()} {self.os_version()}\n"
            f"Processor: {self.processor()}\n"
            f"Machine: {self.machine()}\n"
            f"Python: {self.python_version()}"
        )