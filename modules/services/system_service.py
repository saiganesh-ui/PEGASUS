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

    def disk(self):
        return psutil.disk_usage("/")