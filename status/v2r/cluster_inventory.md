# V2R cluster inventory

2026-09-24T03:51:32.050050+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324738781184 available bytes; 81.88% used; 112493674 free inodes.

server1 `/home`: 324738781184 available bytes; 81.88% used; 112493674 free inodes.

server1 `/tmp`: 324738781184 available bytes; 81.88% used; 112493674 free inodes.

server1 `/var/tmp`: 324738781184 available bytes; 81.88% used; 112493674 free inodes.

server1 `/mnt/raid5`: 406961668096 available bytes; 98.13% used; 337724797 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40816521216 available bytes; 97.72% used; 110430938 free inodes.

server2 `/home`: 40816521216 available bytes; 97.72% used; 110430938 free inodes.

server2 `/tmp`: 40816521216 available bytes; 97.72% used; 110430938 free inodes.

server2 `/var/tmp`: 40816521216 available bytes; 97.72% used; 110430938 free inodes.

server2 `/mnt/raid5`: 526559653888 available bytes; 96.36% used; 445197136 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292369285120 available bytes; 83.68% used; 114198570 free inodes.

server3 `/home`: 292369285120 available bytes; 83.68% used; 114198570 free inodes.

server3 `/data`: 33873260544 available bytes; 99.53% used; 225842553 free inodes.

server3 `/tmp`: 292369285120 available bytes; 83.68% used; 114198570 free inodes.

server3 `/var/tmp`: 292369285120 available bytes; 83.68% used; 114198570 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105792552960 available bytes; 94.10% used; 114349566 free inodes.

server4 `/home`: 105792552960 available bytes; 94.10% used; 114349566 free inodes.

server4 `/data`: 274965712896 available bytes; 96.20% used; 225384079 free inodes.

server4 `/tmp`: 105792552960 available bytes; 94.10% used; 114349566 free inodes.

server4 `/var/tmp`: 105792552960 available bytes; 94.10% used; 114349566 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
