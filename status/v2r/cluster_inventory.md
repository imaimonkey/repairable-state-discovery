# V2R cluster inventory

2026-09-24T03:56:14.823476+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324733431808 available bytes; 81.88% used; 112493634 free inodes.

server1 `/home`: 324733431808 available bytes; 81.88% used; 112493634 free inodes.

server1 `/tmp`: 324733431808 available bytes; 81.88% used; 112493634 free inodes.

server1 `/var/tmp`: 324733431808 available bytes; 81.88% used; 112493634 free inodes.

server1 `/mnt/raid5`: 411798900736 available bytes; 98.11% used; 337724784 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40814727168 available bytes; 97.72% used; 110430904 free inodes.

server2 `/home`: 40814727168 available bytes; 97.72% used; 110430904 free inodes.

server2 `/tmp`: 40814727168 available bytes; 97.72% used; 110430904 free inodes.

server2 `/var/tmp`: 40814727168 available bytes; 97.72% used; 110430904 free inodes.

server2 `/mnt/raid5`: 526415302656 available bytes; 96.36% used; 445196829 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292383797248 available bytes; 83.68% used; 114201274 free inodes.

server3 `/home`: 292383797248 available bytes; 83.68% used; 114201274 free inodes.

server3 `/data`: 33865932800 available bytes; 99.53% used; 225842470 free inodes.

server3 `/tmp`: 292383797248 available bytes; 83.68% used; 114201274 free inodes.

server3 `/var/tmp`: 292383797248 available bytes; 83.68% used; 114201274 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105791643648 available bytes; 94.10% used; 114349524 free inodes.

server4 `/home`: 105791643648 available bytes; 94.10% used; 114349524 free inodes.

server4 `/data`: 258352615424 available bytes; 96.43% used; 225382442 free inodes.

server4 `/tmp`: 105791643648 available bytes; 94.10% used; 114349524 free inodes.

server4 `/var/tmp`: 105791643648 available bytes; 94.10% used; 114349524 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
