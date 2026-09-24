# V2R cluster inventory

2026-09-24T03:52:29.017325+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324737486848 available bytes; 81.88% used; 112493658 free inodes.

server1 `/home`: 324737486848 available bytes; 81.88% used; 112493658 free inodes.

server1 `/tmp`: 324737486848 available bytes; 81.88% used; 112493658 free inodes.

server1 `/var/tmp`: 324737486848 available bytes; 81.88% used; 112493658 free inodes.

server1 `/mnt/raid5`: 406960427008 available bytes; 98.13% used; 337724797 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40817426432 available bytes; 97.72% used; 110430936 free inodes.

server2 `/home`: 40817426432 available bytes; 97.72% used; 110430936 free inodes.

server2 `/tmp`: 40817426432 available bytes; 97.72% used; 110430936 free inodes.

server2 `/var/tmp`: 40817426432 available bytes; 97.72% used; 110430936 free inodes.

server2 `/mnt/raid5`: 526525575168 available bytes; 96.36% used; 445197012 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292368932864 available bytes; 83.68% used; 114198570 free inodes.

server3 `/home`: 292368932864 available bytes; 83.68% used; 114198570 free inodes.

server3 `/data`: 33872093184 available bytes; 99.53% used; 225842522 free inodes.

server3 `/tmp`: 292368932864 available bytes; 83.68% used; 114198570 free inodes.

server3 `/var/tmp`: 292368932864 available bytes; 83.68% used; 114198570 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105791942656 available bytes; 94.10% used; 114349539 free inodes.

server4 `/home`: 105791942656 available bytes; 94.10% used; 114349539 free inodes.

server4 `/data`: 274459545600 available bytes; 96.21% used; 225384001 free inodes.

server4 `/tmp`: 105791942656 available bytes; 94.10% used; 114349539 free inodes.

server4 `/var/tmp`: 105791942656 available bytes; 94.10% used; 114349539 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
