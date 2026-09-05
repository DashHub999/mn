import asyncio
from bleak import BleakScanner
import time

async def scan():
    print("Scanning for Bluetooth devices...")
    devices = await BleakScanner.discover()

    for d in devices:
        print(f"{d.name} - {d.address}")

asyncio.run(scan())
time.sleep(5)
