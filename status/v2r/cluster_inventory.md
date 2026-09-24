# V2R cluster inventory

2026-09-24T05:15:20.895801+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324591251456 available bytes; 81.89% used; 112492536 free inodes.

server1 `/home`: 324591251456 available bytes; 81.89% used; 112492536 free inodes.

server1 `/tmp`: 324591251456 available bytes; 81.89% used; 112492536 free inodes.

server1 `/var/tmp`: 324591251456 available bytes; 81.89% used; 112492536 free inodes.

server1 `/mnt/raid5`: 501088235520 available bytes; 97.70% used; 337724535 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40746844160 available bytes; 97.73% used; 110430366 free inodes.

server2 `/home`: 40746844160 available bytes; 97.73% used; 110430366 free inodes.

server2 `/tmp`: 40746844160 available bytes; 97.73% used; 110430366 free inodes.

server2 `/var/tmp`: 40746844160 available bytes; 97.73% used; 110430366 free inodes.

server2 `/mnt/raid5`: 522827571200 available bytes; 96.39% used; 445194213 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 291993841664 available bytes; 83.71% used; 114175941 free inodes.

server3 `/home`: 291993841664 available bytes; 83.71% used; 114175941 free inodes.

server3 `/data`: 21163118592 available bytes; 99.71% used; 225840071 free inodes.

server3 `/tmp`: 291993841664 available bytes; 83.71% used; 114175941 free inodes.

server3 `/var/tmp`: 291993841664 available bytes; 83.71% used; 114175941 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105817890816 available bytes; 94.09% used; 114349379 free inodes.

server4 `/home`: 105817890816 available bytes; 94.09% used; 114349379 free inodes.

server4 `/data`: 252596166656 available bytes; 96.51% used; 225366786 free inodes.

server4 `/tmp`: 105817890816 available bytes; 94.09% used; 114349379 free inodes.

server4 `/var/tmp`: 105817890816 available bytes; 94.09% used; 114349379 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
