# V2R cluster inventory

2026-09-24T18:21:35.776015+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324009013248 available bytes; 81.92% used; 112481441 free inodes.

server1 `/home`: 324009013248 available bytes; 81.92% used; 112481441 free inodes.

server1 `/tmp`: 324009013248 available bytes; 81.92% used; 112481441 free inodes.

server1 `/var/tmp`: 324009013248 available bytes; 81.92% used; 112481441 free inodes.

server1 `/mnt/raid5`: 416336408576 available bytes; 98.09% used; 337640383 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54494359552 available bytes; 96.96% used; 110412024 free inodes.

server2 `/home`: 54494359552 available bytes; 96.96% used; 110412024 free inodes.

server2 `/tmp`: 54494359552 available bytes; 96.96% used; 110412024 free inodes.

server2 `/var/tmp`: 54494359552 available bytes; 96.96% used; 110412024 free inodes.

server2 `/mnt/raid5`: 497005645824 available bytes; 96.57% used; 445161269 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408111104 available bytes; 95.29% used; 114156133 free inodes.

server3 `/home`: 84408111104 available bytes; 95.29% used; 114156133 free inodes.

server3 `/data`: 153009532928 available bytes; 97.89% used; 225800674 free inodes.

server3 `/tmp`: 84408111104 available bytes; 95.29% used; 114156133 free inodes.

server3 `/var/tmp`: 84408111104 available bytes; 95.29% used; 114156133 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105662660608 available bytes; 94.10% used; 114348516 free inodes.

server4 `/home`: 105662660608 available bytes; 94.10% used; 114348516 free inodes.

server4 `/data`: 90070728704 available bytes; 98.76% used; 225268132 free inodes.

server4 `/tmp`: 105662660608 available bytes; 94.10% used; 114348516 free inodes.

server4 `/var/tmp`: 105662660608 available bytes; 94.10% used; 114348516 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
