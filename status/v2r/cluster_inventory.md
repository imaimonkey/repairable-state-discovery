# V2R cluster inventory

2026-09-24T04:42:15.993129+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324623183872 available bytes; 81.89% used; 112492874 free inodes.

server1 `/home`: 324623183872 available bytes; 81.89% used; 112492874 free inodes.

server1 `/tmp`: 324623183872 available bytes; 81.89% used; 112492874 free inodes.

server1 `/var/tmp`: 324623183872 available bytes; 81.89% used; 112492874 free inodes.

server1 `/mnt/raid5`: 460148527104 available bytes; 97.89% used; 337724632 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40770027520 available bytes; 97.73% used; 110430480 free inodes.

server2 `/home`: 40770027520 available bytes; 97.73% used; 110430480 free inodes.

server2 `/tmp`: 40770027520 available bytes; 97.73% used; 110430480 free inodes.

server2 `/var/tmp`: 40770027520 available bytes; 97.73% used; 110430480 free inodes.

server2 `/mnt/raid5`: 524424966144 available bytes; 96.38% used; 445195421 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292407201792 available bytes; 83.68% used; 114200439 free inodes.

server3 `/home`: 292407201792 available bytes; 83.68% used; 114200439 free inodes.

server3 `/data`: 24363962368 available bytes; 99.66% used; 225840720 free inodes.

server3 `/tmp`: 292407201792 available bytes; 83.68% used; 114200439 free inodes.

server3 `/var/tmp`: 292407201792 available bytes; 83.68% used; 114200439 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105836318720 available bytes; 94.09% used; 114349396 free inodes.

server4 `/home`: 105836318720 available bytes; 94.09% used; 114349396 free inodes.

server4 `/data`: 253382512640 available bytes; 96.50% used; 225366862 free inodes.

server4 `/tmp`: 105836318720 available bytes; 94.09% used; 114349396 free inodes.

server4 `/var/tmp`: 105836318720 available bytes; 94.09% used; 114349396 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
