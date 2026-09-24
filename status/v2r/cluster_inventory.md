# V2R cluster inventory

2026-09-24T23:19:22.341881+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319008382976 available bytes; 82.20% used; 112480799 free inodes.

server1 `/home`: 319008382976 available bytes; 82.20% used; 112480799 free inodes.

server1 `/tmp`: 319008382976 available bytes; 82.20% used; 112480799 free inodes.

server1 `/var/tmp`: 319008382976 available bytes; 82.20% used; 112480799 free inodes.

server1 `/mnt/raid5`: 415258341376 available bytes; 98.10% used; 337614469 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23119351808 available bytes; 98.71% used; 110410812 free inodes.

server2 `/home`: 23119351808 available bytes; 98.71% used; 110410812 free inodes.

server2 `/tmp`: 23119351808 available bytes; 98.71% used; 110410812 free inodes.

server2 `/var/tmp`: 23119351808 available bytes; 98.71% used; 110410812 free inodes.

server2 `/mnt/raid5`: 487015735296 available bytes; 96.63% used; 445151643 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84373970944 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84373970944 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148463570944 available bytes; 97.95% used; 225801111 free inodes.

server3 `/tmp`: 84373970944 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84373970944 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799880704 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799880704 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61519245312 available bytes; 99.15% used; 225162711 free inodes.

server4 `/tmp`: 105799880704 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799880704 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
