# V2R cluster inventory

2026-09-24T10:37:35.943371+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324407332864 available bytes; 81.90% used; 112489202 free inodes.

server1 `/home`: 324407332864 available bytes; 81.90% used; 112489202 free inodes.

server1 `/tmp`: 324407332864 available bytes; 81.90% used; 112489202 free inodes.

server1 `/var/tmp`: 324407332864 available bytes; 81.90% used; 112489202 free inodes.

server1 `/mnt/raid5`: 499983380480 available bytes; 97.71% used; 337696930 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57722707968 available bytes; 96.78% used; 110430533 free inodes.

server2 `/home`: 57722707968 available bytes; 96.78% used; 110430533 free inodes.

server2 `/tmp`: 57722707968 available bytes; 96.78% used; 110430533 free inodes.

server2 `/var/tmp`: 57722707968 available bytes; 96.78% used; 110430533 free inodes.

server2 `/mnt/raid5`: 512565755904 available bytes; 96.46% used; 445175332 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85818331136 available bytes; 95.21% used; 114199504 free inodes.

server3 `/home`: 85818331136 available bytes; 95.21% used; 114199504 free inodes.

server3 `/data`: 164176371712 available bytes; 97.73% used; 225818102 free inodes.

server3 `/tmp`: 85818331136 available bytes; 95.21% used; 114199504 free inodes.

server3 `/var/tmp`: 85818331136 available bytes; 95.21% used; 114199504 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744203776 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105744203776 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 153467854848 available bytes; 97.88% used; 225258361 free inodes.

server4 `/tmp`: 105744203776 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105744203776 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
