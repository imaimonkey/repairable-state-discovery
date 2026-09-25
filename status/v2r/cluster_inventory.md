# V2R cluster inventory

2026-09-25T06:15:16.075387+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318881427456 available bytes; 82.21% used; 112480346 free inodes.

server1 `/home`: 318881427456 available bytes; 82.21% used; 112480346 free inodes.

server1 `/tmp`: 318881427456 available bytes; 82.21% used; 112480346 free inodes.

server1 `/var/tmp`: 318881427456 available bytes; 82.21% used; 112480346 free inodes.

server1 `/mnt/raid5`: 401474936832 available bytes; 98.16% used; 337562822 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22893187072 available bytes; 98.72% used; 110410534 free inodes.

server2 `/home`: 22893187072 available bytes; 98.72% used; 110410534 free inodes.

server2 `/tmp`: 22893187072 available bytes; 98.72% used; 110410534 free inodes.

server2 `/var/tmp`: 22893187072 available bytes; 98.72% used; 110410534 free inodes.

server2 `/mnt/raid5`: 375119130624 available bytes; 97.41% used; 445100333 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84316790784 available bytes; 95.29% used; 114156037 free inodes.

server3 `/home`: 84316790784 available bytes; 95.29% used; 114156037 free inodes.

server3 `/data`: 142533320704 available bytes; 98.03% used; 225814057 free inodes.

server3 `/tmp`: 84316790784 available bytes; 95.29% used; 114156037 free inodes.

server3 `/var/tmp`: 84316790784 available bytes; 95.29% used; 114156037 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105648660480 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105648660480 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 254642257920 available bytes; 96.48% used; 225023551 free inodes.

server4 `/tmp`: 105648660480 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105648660480 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
