# V2R cluster inventory

2026-09-24T10:45:21.606409+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324407697408 available bytes; 81.90% used; 112489167 free inodes.

server1 `/home`: 324407697408 available bytes; 81.90% used; 112489167 free inodes.

server1 `/tmp`: 324407697408 available bytes; 81.90% used; 112489167 free inodes.

server1 `/var/tmp`: 324407697408 available bytes; 81.90% used; 112489167 free inodes.

server1 `/mnt/raid5`: 499778678784 available bytes; 97.71% used; 337696001 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57714819072 available bytes; 96.78% used; 110430453 free inodes.

server2 `/home`: 57714819072 available bytes; 96.78% used; 110430453 free inodes.

server2 `/tmp`: 57714819072 available bytes; 96.78% used; 110430453 free inodes.

server2 `/var/tmp`: 57714819072 available bytes; 96.78% used; 110430453 free inodes.

server2 `/mnt/raid5`: 511791091712 available bytes; 96.46% used; 445174968 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85815005184 available bytes; 95.21% used; 114199422 free inodes.

server3 `/home`: 85815005184 available bytes; 95.21% used; 114199422 free inodes.

server3 `/data`: 143476867072 available bytes; 98.02% used; 225817922 free inodes.

server3 `/tmp`: 85815005184 available bytes; 95.21% used; 114199422 free inodes.

server3 `/var/tmp`: 85815005184 available bytes; 95.21% used; 114199422 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735577600 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105735577600 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 132810096640 available bytes; 98.16% used; 225258339 free inodes.

server4 `/tmp`: 105735577600 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105735577600 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
