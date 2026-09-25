# V2R cluster inventory

2026-09-25T13:09:49.555077+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319111180288 available bytes; 82.20% used; 112477566 free inodes.

server1 `/home`: 319111180288 available bytes; 82.20% used; 112477566 free inodes.

server1 `/tmp`: 319111180288 available bytes; 82.20% used; 112477566 free inodes.

server1 `/var/tmp`: 319111180288 available bytes; 82.20% used; 112477566 free inodes.

server1 `/mnt/raid5`: 364386992128 available bytes; 98.33% used; 337547915 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8292876288 available bytes; 99.54% used; 110408764 free inodes.

server2 `/home`: 8292876288 available bytes; 99.54% used; 110408764 free inodes.

server2 `/tmp`: 8292876288 available bytes; 99.54% used; 110408764 free inodes.

server2 `/var/tmp`: 8292876288 available bytes; 99.54% used; 110408764 free inodes.

server2 `/mnt/raid5`: 323513548800 available bytes; 97.76% used; 445077791 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84208181248 available bytes; 95.30% used; 114154960 free inodes.

server3 `/home`: 84208181248 available bytes; 95.30% used; 114154960 free inodes.

server3 `/data`: 142354993152 available bytes; 98.03% used; 225810041 free inodes.

server3 `/tmp`: 84208181248 available bytes; 95.30% used; 114154960 free inodes.

server3 `/var/tmp`: 84208181248 available bytes; 95.30% used; 114154960 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656520704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656520704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231421288448 available bytes; 96.80% used; 224954263 free inodes.

server4 `/tmp`: 105656520704 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656520704 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
