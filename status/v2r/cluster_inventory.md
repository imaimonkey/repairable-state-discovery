# V2R cluster inventory

2026-09-24T05:36:49.995053+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324533805056 available bytes; 81.90% used; 112492198 free inodes.

server1 `/home`: 324533805056 available bytes; 81.90% used; 112492198 free inodes.

server1 `/tmp`: 324533805056 available bytes; 81.90% used; 112492198 free inodes.

server1 `/var/tmp`: 324533805056 available bytes; 81.90% used; 112492198 free inodes.

server1 `/mnt/raid5`: 517635588096 available bytes; 97.63% used; 337723995 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57915396096 available bytes; 96.77% used; 110431350 free inodes.

server2 `/home`: 57915396096 available bytes; 96.77% used; 110431350 free inodes.

server2 `/tmp`: 57915396096 available bytes; 96.77% used; 110431350 free inodes.

server2 `/var/tmp`: 57915396096 available bytes; 96.77% used; 110431350 free inodes.

server2 `/mnt/raid5`: 522164375552 available bytes; 96.39% used; 445193832 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 127198162944 available bytes; 92.90% used; 114199547 free inodes.

server3 `/home`: 127198162944 available bytes; 92.90% used; 114199547 free inodes.

server3 `/data`: 185257725952 available bytes; 97.44% used; 225839274 free inodes.

server3 `/tmp`: 127198162944 available bytes; 92.90% used; 114199547 free inodes.

server3 `/var/tmp`: 127198162944 available bytes; 92.90% used; 114199547 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105816768512 available bytes; 94.10% used; 114349365 free inodes.

server4 `/home`: 105816768512 available bytes; 94.10% used; 114349365 free inodes.

server4 `/data`: 251505897472 available bytes; 96.52% used; 225358072 free inodes.

server4 `/tmp`: 105816768512 available bytes; 94.10% used; 114349365 free inodes.

server4 `/var/tmp`: 105816768512 available bytes; 94.10% used; 114349365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
