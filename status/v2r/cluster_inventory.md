# V2R cluster inventory

2026-09-25T00:09:59.305935+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319089094656 available bytes; 82.20% used; 112480789 free inodes.

server1 `/home`: 319089094656 available bytes; 82.20% used; 112480789 free inodes.

server1 `/tmp`: 319089094656 available bytes; 82.20% used; 112480789 free inodes.

server1 `/var/tmp`: 319089094656 available bytes; 82.20% used; 112480789 free inodes.

server1 `/mnt/raid5`: 416892022784 available bytes; 98.09% used; 337622220 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23094468608 available bytes; 98.71% used; 110410785 free inodes.

server2 `/home`: 23094468608 available bytes; 98.71% used; 110410785 free inodes.

server2 `/tmp`: 23094468608 available bytes; 98.71% used; 110410785 free inodes.

server2 `/var/tmp`: 23094468608 available bytes; 98.71% used; 110410785 free inodes.

server2 `/mnt/raid5`: 487111397376 available bytes; 96.63% used; 445163595 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84354174976 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84354174976 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 149238870016 available bytes; 97.94% used; 225813826 free inodes.

server3 `/tmp`: 84354174976 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84354174976 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['0', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105797890048 available bytes; 94.10% used; 114348297 free inodes.

server4 `/home`: 105797890048 available bytes; 94.10% used; 114348297 free inodes.

server4 `/data`: 57826951168 available bytes; 99.20% used; 225087383 free inodes.

server4 `/tmp`: 105797890048 available bytes; 94.10% used; 114348297 free inodes.

server4 `/var/tmp`: 105797890048 available bytes; 94.10% used; 114348297 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
