# V2R cluster inventory

2026-09-25T09:45:49.137618+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318837116928 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318837116928 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318837116928 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318837116928 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 350355079168 available bytes; 98.39% used; 337556817 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22836559872 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22836559872 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22836559872 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22836559872 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 331268567040 available bytes; 97.71% used; 445092014 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84417757184 available bytes; 95.29% used; 114156041 free inodes.

server3 `/home`: 84417757184 available bytes; 95.29% used; 114156041 free inodes.

server3 `/data`: 142295830528 available bytes; 98.03% used; 225810391 free inodes.

server3 `/tmp`: 84417757184 available bytes; 95.29% used; 114156041 free inodes.

server3 `/var/tmp`: 84417757184 available bytes; 95.29% used; 114156041 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105623216128 available bytes; 94.11% used; 114350278 free inodes.

server4 `/home`: 105623216128 available bytes; 94.11% used; 114350278 free inodes.

server4 `/data`: 240047718400 available bytes; 96.68% used; 224993566 free inodes.

server4 `/tmp`: 105623216128 available bytes; 94.11% used; 114350278 free inodes.

server4 `/var/tmp`: 105623216128 available bytes; 94.11% used; 114350278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
