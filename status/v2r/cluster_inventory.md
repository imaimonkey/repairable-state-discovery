# V2R cluster inventory

2026-09-24T10:39:09.125825+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324406140928 available bytes; 81.90% used; 112489193 free inodes.

server1 `/home`: 324406140928 available bytes; 81.90% used; 112489193 free inodes.

server1 `/tmp`: 324406140928 available bytes; 81.90% used; 112489193 free inodes.

server1 `/var/tmp`: 324406140928 available bytes; 81.90% used; 112489193 free inodes.

server1 `/mnt/raid5`: 499956531200 available bytes; 97.71% used; 337696735 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57720426496 available bytes; 96.78% used; 110430517 free inodes.

server2 `/home`: 57720426496 available bytes; 96.78% used; 110430517 free inodes.

server2 `/tmp`: 57720426496 available bytes; 96.78% used; 110430517 free inodes.

server2 `/var/tmp`: 57720426496 available bytes; 96.78% used; 110430517 free inodes.

server2 `/mnt/raid5`: 512515592192 available bytes; 96.46% used; 445175164 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85817143296 available bytes; 95.21% used; 114199486 free inodes.

server3 `/home`: 85817143296 available bytes; 95.21% used; 114199486 free inodes.

server3 `/data`: 164170485760 available bytes; 97.73% used; 225818056 free inodes.

server3 `/tmp`: 85817143296 available bytes; 95.21% used; 114199486 free inodes.

server3 `/var/tmp`: 85817143296 available bytes; 95.21% used; 114199486 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105744158720 available bytes; 94.10% used; 114348964 free inodes.

server4 `/home`: 105744158720 available bytes; 94.10% used; 114348964 free inodes.

server4 `/data`: 153471209472 available bytes; 97.88% used; 225258360 free inodes.

server4 `/tmp`: 105744158720 available bytes; 94.10% used; 114348964 free inodes.

server4 `/var/tmp`: 105744158720 available bytes; 94.10% used; 114348964 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
