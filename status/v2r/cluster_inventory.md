# V2R cluster inventory

2026-09-24T13:52:56.968073+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324067504128 available bytes; 81.92% used; 112481661 free inodes.

server1 `/home`: 324067504128 available bytes; 81.92% used; 112481661 free inodes.

server1 `/tmp`: 324067504128 available bytes; 81.92% used; 112481661 free inodes.

server1 `/var/tmp`: 324067504128 available bytes; 81.92% used; 112481661 free inodes.

server1 `/mnt/raid5`: 416979427328 available bytes; 98.09% used; 337672547 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57503539200 available bytes; 96.79% used; 110428485 free inodes.

server2 `/home`: 57503539200 available bytes; 96.79% used; 110428485 free inodes.

server2 `/tmp`: 57503539200 available bytes; 96.79% used; 110428485 free inodes.

server2 `/var/tmp`: 57503539200 available bytes; 96.79% used; 110428485 free inodes.

server2 `/mnt/raid5`: 505913823232 available bytes; 96.50% used; 445168987 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85076058112 available bytes; 95.25% used; 114188085 free inodes.

server3 `/home`: 85076058112 available bytes; 95.25% used; 114188085 free inodes.

server3 `/data`: 161094254592 available bytes; 97.77% used; 225802721 free inodes.

server3 `/tmp`: 85076058112 available bytes; 95.25% used; 114188085 free inodes.

server3 `/var/tmp`: 85076058112 available bytes; 95.25% used; 114188085 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105760370688 available bytes; 94.10% used; 114348716 free inodes.

server4 `/home`: 105760370688 available bytes; 94.10% used; 114348716 free inodes.

server4 `/data`: 90037477376 available bytes; 98.76% used; 225257162 free inodes.

server4 `/tmp`: 105760370688 available bytes; 94.10% used; 114348716 free inodes.

server4 `/var/tmp`: 105760370688 available bytes; 94.10% used; 114348716 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
