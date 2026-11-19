# Precision Time Protocol — quick refresher

## Purpose
PTP (IEEE 1588) synchronises clocks across a network. It is different from a point-to-point topology. Accurate timestamps support event ordering and latency measurement in trading systems.

## Clock roles and timestamps
- The grandmaster is the reference clock for a PTP domain.
- Ordinary clocks participate at endpoints; boundary clocks synchronise between ports.
- Transparent clocks account for residence time through a device.
- Hardware timestamps near the NIC reduce software scheduling noise. Clock quality and path asymmetry still limit accuracy.
- An alternate timescale provides additional time interpretation; it is not a replacement for synchronisation.

## Linux tools
- `ptp4l` implements PTP; hardware mode typically disciplines the NIC's PTP hardware clock (PHC).
- `phc2sys` synchronises clocks, commonly the system clock to the PHC.
- `ethtool -T eth0` reports timestamping capabilities.
- `journalctl -u ptp4l` shows logs when the daemon is managed under that service name.

## Troubleshooting
Check domain/profile compatibility, timestamping mode, selected grandmaster, offset stability and path asymmetry. A stable offset of whole seconds can indicate a UTC/PTP timescale mismatch. Do not let unrelated time services compete to discipline the same clock.

References: [ptp4l](https://www.linuxptp.org/documentation/ptp4l/), [phc2sys](https://www.linuxptp.org/documentation/phc2sys/).
