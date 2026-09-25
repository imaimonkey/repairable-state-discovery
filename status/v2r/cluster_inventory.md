# V2R cluster inventory

2026-09-25T13:08:16.940127+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319111421952 available bytes; 82.20% used; 112477566 free inodes.

server1 `/home`: 319111421952 available bytes; 82.20% used; 112477566 free inodes.

server1 `/tmp`: 319111421952 available bytes; 82.20% used; 112477566 free inodes.

server1 `/var/tmp`: 319111421952 available bytes; 82.20% used; 112477566 free inodes.

server1 `/mnt/raid5`: 368451764224 available bytes; 98.31% used; 337547980 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8293273600 available bytes; 99.54% used; 110408765 free inodes.

server2 `/home`: 8293273600 available bytes; 99.54% used; 110408765 free inodes.

server2 `/tmp`: 8293273600 available bytes; 99.54% used; 110408765 free inodes.

server2 `/var/tmp`: 8293273600 available bytes; 99.54% used; 110408765 free inodes.

server2 `/mnt/raid5`: 324077121536 available bytes; 97.76% used; 445077626 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84208201728 available bytes; 95.30% used; 114154960 free inodes.

server3 `/home`: 84208201728 available bytes; 95.30% used; 114154960 free inodes.

server3 `/data`: 142356844544 available bytes; 98.03% used; 225810071 free inodes.

server3 `/tmp`: 84208201728 available bytes; 95.30% used; 114154960 free inodes.

server3 `/var/tmp`: 84208201728 available bytes; 95.30% used; 114154960 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656545280 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656545280 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231423373312 available bytes; 96.80% used; 224954455 free inodes.

server4 `/tmp`: 105656545280 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656545280 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
