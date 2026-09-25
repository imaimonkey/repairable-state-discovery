# V2R cluster inventory

2026-09-25T10:08:47.539387+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318834307072 available bytes; 82.21% used; 112480382 free inodes.

server1 `/home`: 318834307072 available bytes; 82.21% used; 112480382 free inodes.

server1 `/tmp`: 318834307072 available bytes; 82.21% used; 112480382 free inodes.

server1 `/var/tmp`: 318834307072 available bytes; 82.21% used; 112480382 free inodes.

server1 `/mnt/raid5`: 364789604352 available bytes; 98.33% used; 337556898 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22828048384 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22828048384 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22828048384 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22828048384 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 316259102720 available bytes; 97.81% used; 445091196 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418019328 available bytes; 95.29% used; 114156045 free inodes.

server3 `/home`: 84418019328 available bytes; 95.29% used; 114156045 free inodes.

server3 `/data`: 142029303808 available bytes; 98.04% used; 225816332 free inodes.

server3 `/tmp`: 84418019328 available bytes; 95.29% used; 114156045 free inodes.

server3 `/var/tmp`: 84418019328 available bytes; 95.29% used; 114156045 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614147584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614147584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240002121728 available bytes; 96.68% used; 224990613 free inodes.

server4 `/tmp`: 105614147584 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614147584 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
