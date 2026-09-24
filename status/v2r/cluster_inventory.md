# V2R cluster inventory

2026-09-24T23:30:08.883108+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319013195776 available bytes; 82.20% used; 112480782 free inodes.

server1 `/home`: 319013195776 available bytes; 82.20% used; 112480782 free inodes.

server1 `/tmp`: 319013195776 available bytes; 82.20% used; 112480782 free inodes.

server1 `/var/tmp`: 319013195776 available bytes; 82.20% used; 112480782 free inodes.

server1 `/mnt/raid5`: 415228317696 available bytes; 98.10% used; 337613211 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23111790592 available bytes; 98.71% used; 110410806 free inodes.

server2 `/home`: 23111790592 available bytes; 98.71% used; 110410806 free inodes.

server2 `/tmp`: 23111790592 available bytes; 98.71% used; 110410806 free inodes.

server2 `/var/tmp`: 23111790592 available bytes; 98.71% used; 110410806 free inodes.

server2 `/mnt/raid5`: 486397063168 available bytes; 96.64% used; 445151191 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 84369240064 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84369240064 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 148207038464 available bytes; 97.95% used; 225800917 free inodes.

server3 `/tmp`: 84369240064 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84369240064 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799565312 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799565312 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61334470656 available bytes; 99.15% used; 225147381 free inodes.

server4 `/tmp`: 105799565312 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799565312 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
