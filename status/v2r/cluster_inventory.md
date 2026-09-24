# V2R cluster inventory

2026-09-24T10:39:00.834339+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324406124544 available bytes; 81.90% used; 112489192 free inodes.

server1 `/home`: 324406124544 available bytes; 81.90% used; 112489192 free inodes.

server1 `/tmp`: 324406124544 available bytes; 81.90% used; 112489192 free inodes.

server1 `/var/tmp`: 324406124544 available bytes; 81.90% used; 112489192 free inodes.

server1 `/mnt/raid5`: 499960160256 available bytes; 97.71% used; 337696751 free inodes.
| server2 | True | ['5'] | [] | reference_compatible=False |

server2 `/`: 57720430592 available bytes; 96.78% used; 110430517 free inodes.

server2 `/home`: 57720430592 available bytes; 96.78% used; 110430517 free inodes.

server2 `/tmp`: 57720430592 available bytes; 96.78% used; 110430517 free inodes.

server2 `/var/tmp`: 57720430592 available bytes; 96.78% used; 110430517 free inodes.

server2 `/mnt/raid5`: 512521068544 available bytes; 96.46% used; 445175187 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85817147392 available bytes; 95.21% used; 114199486 free inodes.

server3 `/home`: 85817147392 available bytes; 95.21% used; 114199486 free inodes.

server3 `/data`: 164171079680 available bytes; 97.73% used; 225818076 free inodes.

server3 `/tmp`: 85817147392 available bytes; 95.21% used; 114199486 free inodes.

server3 `/var/tmp`: 85817147392 available bytes; 95.21% used; 114199486 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105744162816 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105744162816 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 153471352832 available bytes; 97.88% used; 225258360 free inodes.

server4 `/tmp`: 105744162816 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105744162816 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
