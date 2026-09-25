# V2R cluster inventory

2026-09-25T05:46:00.654667+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318879662080 available bytes; 82.21% used; 112480347 free inodes.

server1 `/home`: 318879662080 available bytes; 82.21% used; 112480347 free inodes.

server1 `/tmp`: 318879662080 available bytes; 82.21% used; 112480347 free inodes.

server1 `/var/tmp`: 318879662080 available bytes; 82.21% used; 112480347 free inodes.

server1 `/mnt/raid5`: 408453074944 available bytes; 98.13% used; 337566378 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22913884160 available bytes; 98.72% used; 110410470 free inodes.

server2 `/home`: 22913884160 available bytes; 98.72% used; 110410470 free inodes.

server2 `/tmp`: 22913884160 available bytes; 98.72% used; 110410470 free inodes.

server2 `/var/tmp`: 22913884160 available bytes; 98.72% used; 110410470 free inodes.

server2 `/mnt/raid5`: 420340621312 available bytes; 97.10% used; 445102185 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84313038848 available bytes; 95.30% used; 114156041 free inodes.

server3 `/home`: 84313038848 available bytes; 95.30% used; 114156041 free inodes.

server3 `/data`: 142777917440 available bytes; 98.03% used; 225814558 free inodes.

server3 `/tmp`: 84313038848 available bytes; 95.30% used; 114156041 free inodes.

server3 `/var/tmp`: 84313038848 available bytes; 95.30% used; 114156041 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649524736 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649524736 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 24755044352 available bytes; 99.66% used; 224965521 free inodes.

server4 `/tmp`: 105649524736 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649524736 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
