# V2R cluster inventory

2026-09-25T05:13:40.057634+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318893768704 available bytes; 82.21% used; 112480301 free inodes.

server1 `/home`: 318893768704 available bytes; 82.21% used; 112480301 free inodes.

server1 `/tmp`: 318893768704 available bytes; 82.21% used; 112480301 free inodes.

server1 `/var/tmp`: 318893768704 available bytes; 82.21% used; 112480301 free inodes.

server1 `/mnt/raid5`: 408585039872 available bytes; 98.13% used; 337570353 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22929440768 available bytes; 98.72% used; 110410436 free inodes.

server2 `/home`: 22929440768 available bytes; 98.72% used; 110410436 free inodes.

server2 `/tmp`: 22929440768 available bytes; 98.72% used; 110410436 free inodes.

server2 `/var/tmp`: 22929440768 available bytes; 98.72% used; 110410436 free inodes.

server2 `/mnt/raid5`: 461692174336 available bytes; 96.81% used; 445108861 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84338941952 available bytes; 95.29% used; 114156065 free inodes.

server3 `/home`: 84338941952 available bytes; 95.29% used; 114156065 free inodes.

server3 `/data`: 142790221824 available bytes; 98.03% used; 225815230 free inodes.

server3 `/tmp`: 84338941952 available bytes; 95.29% used; 114156065 free inodes.

server3 `/var/tmp`: 84338941952 available bytes; 95.29% used; 114156065 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658970112 available bytes; 94.10% used; 114350409 free inodes.

server4 `/home`: 105658970112 available bytes; 94.10% used; 114350409 free inodes.

server4 `/data`: 26322067456 available bytes; 99.64% used; 224960425 free inodes.

server4 `/tmp`: 105658970112 available bytes; 94.10% used; 114350409 free inodes.

server4 `/var/tmp`: 105658970112 available bytes; 94.10% used; 114350409 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
