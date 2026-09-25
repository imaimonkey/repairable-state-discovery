# V2R cluster inventory

2026-09-25T02:54:28.848525+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318952828928 available bytes; 82.21% used; 112480426 free inodes.

server1 `/home`: 318952828928 available bytes; 82.21% used; 112480426 free inodes.

server1 `/tmp`: 318952828928 available bytes; 82.21% used; 112480426 free inodes.

server1 `/var/tmp`: 318952828928 available bytes; 82.21% used; 112480426 free inodes.

server1 `/mnt/raid5`: 416163708928 available bytes; 98.09% used; 337603096 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22998667264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/home`: 22998667264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/tmp`: 22998667264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/var/tmp`: 22998667264 available bytes; 98.72% used; 110410441 free inodes.

server2 `/mnt/raid5`: 482379620352 available bytes; 96.67% used; 445113266 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84346368000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84346368000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 145117552640 available bytes; 97.99% used; 225810576 free inodes.

server3 `/tmp`: 84346368000 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84346368000 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105693544448 available bytes; 94.10% used; 114350921 free inodes.

server4 `/home`: 105693544448 available bytes; 94.10% used; 114350921 free inodes.

server4 `/data`: 54853574656 available bytes; 99.24% used; 224967544 free inodes.

server4 `/tmp`: 105693544448 available bytes; 94.10% used; 114350921 free inodes.

server4 `/var/tmp`: 105693544448 available bytes; 94.10% used; 114350921 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
