# V2R cluster inventory

2026-09-24T10:56:13.537224+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324380794880 available bytes; 81.90% used; 112489067 free inodes.

server1 `/home`: 324380794880 available bytes; 81.90% used; 112489067 free inodes.

server1 `/tmp`: 324380794880 available bytes; 81.90% used; 112489067 free inodes.

server1 `/var/tmp`: 324380794880 available bytes; 81.90% used; 112489067 free inodes.

server1 `/mnt/raid5`: 496687112192 available bytes; 97.72% used; 337693991 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57698828288 available bytes; 96.78% used; 110430333 free inodes.

server2 `/home`: 57698828288 available bytes; 96.78% used; 110430333 free inodes.

server2 `/tmp`: 57698828288 available bytes; 96.78% used; 110430333 free inodes.

server2 `/var/tmp`: 57698828288 available bytes; 96.78% used; 110430333 free inodes.

server2 `/mnt/raid5`: 511998181376 available bytes; 96.46% used; 445174675 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85783842816 available bytes; 95.21% used; 114197376 free inodes.

server3 `/home`: 85783842816 available bytes; 95.21% used; 114197376 free inodes.

server3 `/data`: 164060065792 available bytes; 97.73% used; 225817712 free inodes.

server3 `/tmp`: 85783842816 available bytes; 95.21% used; 114197376 free inodes.

server3 `/var/tmp`: 85783842816 available bytes; 95.21% used; 114197376 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/home`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/data`: 132779675648 available bytes; 98.16% used; 225258266 free inodes.

server4 `/tmp`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server4 `/var/tmp`: 105734922240 available bytes; 94.10% used; 114348935 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
