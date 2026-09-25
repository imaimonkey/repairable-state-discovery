# V2R cluster inventory

2026-09-25T13:08:03.759479+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['5'] | ['/tmp', '/var/tmp'] |

server1 `/`: 319111442432 available bytes; 82.20% used; 112477566 free inodes.

server1 `/home`: 319111442432 available bytes; 82.20% used; 112477566 free inodes.

server1 `/tmp`: 319111442432 available bytes; 82.20% used; 112477566 free inodes.

server1 `/var/tmp`: 319111442432 available bytes; 82.20% used; 112477566 free inodes.

server1 `/mnt/raid5`: 348412239872 available bytes; 98.40% used; 337547988 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 8293502976 available bytes; 99.54% used; 110408765 free inodes.

server2 `/home`: 8293502976 available bytes; 99.54% used; 110408765 free inodes.

server2 `/tmp`: 8293502976 available bytes; 99.54% used; 110408765 free inodes.

server2 `/var/tmp`: 8293502976 available bytes; 99.54% used; 110408765 free inodes.

server2 `/mnt/raid5`: 324078313472 available bytes; 97.76% used; 445077626 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84206817280 available bytes; 95.30% used; 114154960 free inodes.

server3 `/home`: 84206817280 available bytes; 95.30% used; 114154960 free inodes.

server3 `/data`: 142356951040 available bytes; 98.03% used; 225810071 free inodes.

server3 `/tmp`: 84206817280 available bytes; 95.30% used; 114154960 free inodes.

server3 `/var/tmp`: 84206817280 available bytes; 95.30% used; 114154960 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105656553472 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656553472 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231423631360 available bytes; 96.80% used; 224954486 free inodes.

server4 `/tmp`: 105656553472 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656553472 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
