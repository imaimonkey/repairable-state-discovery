# V2R cluster inventory

2026-09-25T05:47:32.561667+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318879531008 available bytes; 82.21% used; 112480338 free inodes.

server1 `/home`: 318879531008 available bytes; 82.21% used; 112480338 free inodes.

server1 `/tmp`: 318879531008 available bytes; 82.21% used; 112480338 free inodes.

server1 `/var/tmp`: 318879531008 available bytes; 82.21% used; 112480338 free inodes.

server1 `/mnt/raid5`: 408446599168 available bytes; 98.13% used; 337566191 free inodes.
| server2 | True | ['0'] | [] |

server2 `/`: 22910697472 available bytes; 98.72% used; 110410432 free inodes.

server2 `/home`: 22910697472 available bytes; 98.72% used; 110410432 free inodes.

server2 `/tmp`: 22910697472 available bytes; 98.72% used; 110410432 free inodes.

server2 `/var/tmp`: 22910697472 available bytes; 98.72% used; 110410432 free inodes.

server2 `/mnt/raid5`: 420287758336 available bytes; 97.10% used; 445101999 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312793088 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84312793088 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142778937344 available bytes; 98.03% used; 225814540 free inodes.

server3 `/tmp`: 84312793088 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84312793088 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105649475584 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649475584 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 24748085248 available bytes; 99.66% used; 224965257 free inodes.

server4 `/tmp`: 105649475584 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649475584 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
