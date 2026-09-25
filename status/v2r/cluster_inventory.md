# V2R cluster inventory

2026-09-25T02:38:06.321812+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318959263744 available bytes; 82.21% used; 112480422 free inodes.

server1 `/home`: 318959263744 available bytes; 82.21% used; 112480422 free inodes.

server1 `/tmp`: 318959263744 available bytes; 82.21% used; 112480422 free inodes.

server1 `/var/tmp`: 318959263744 available bytes; 82.21% used; 112480422 free inodes.

server1 `/mnt/raid5`: 416193622016 available bytes; 98.09% used; 337605000 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23008104448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23008104448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23008104448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23008104448 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 482871451648 available bytes; 96.66% used; 445113502 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84350996480 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350996480 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145464995840 available bytes; 97.99% used; 225811102 free inodes.

server3 `/tmp`: 84350996480 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350996480 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895567360 available bytes; 94.09% used; 114350966 free inodes.

server4 `/home`: 105895567360 available bytes; 94.09% used; 114350966 free inodes.

server4 `/data`: 314810368 available bytes; 100.00% used; 224968882 free inodes.

server4 `/tmp`: 105895567360 available bytes; 94.09% used; 114350966 free inodes.

server4 `/var/tmp`: 105895567360 available bytes; 94.09% used; 114350966 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
