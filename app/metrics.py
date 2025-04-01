import psutil
from prometheus_client import Gauge

# Create Prometheus gauges for metrics
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Current CPU usage percent')
MEMORY_USAGE = Gauge('system_memory_usage_percent', 'Current memory usage percent')
DISK_USAGE = Gauge('system_disk_usage_percent', 'Current disk usage percent')

def collect_metrics():
    """Collect system metrics and update Prometheus gauges"""
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    CPU_USAGE.set(cpu_percent)
    
    # Memory usage
    memory = psutil.virtual_memory()
    MEMORY_USAGE.set(memory.percent)
    
    # Disk usage (root partition)
    disk = psutil.disk_usage('/')
    DISK_USAGE.set(disk.percent)