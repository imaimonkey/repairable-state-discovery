# V2R cluster inventory

2026-09-25T05:24:29.051650+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873341952 available bytes; 82.21% used; 112480261 free inodes.

server1 `/home`: 318873341952 available bytes; 82.21% used; 112480261 free inodes.

server1 `/tmp`: 318873341952 available bytes; 82.21% used; 112480261 free inodes.

server1 `/var/tmp`: 318873341952 available bytes; 82.21% used; 112480261 free inodes.

server1 `/mnt/raid5`: 408513400832 available bytes; 98.13% used; 337568964 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22924259328 available bytes; 98.72% used; 110410445 free inodes.

server2 `/home`: 22924259328 available bytes; 98.72% used; 110410445 free inodes.

server2 `/tmp`: 22924259328 available bytes; 98.72% used; 110410445 free inodes.

server2 `/var/tmp`: 22924259328 available bytes; 98.72% used; 110410445 free inodes.

server2 `/mnt/raid5`: 461358960640 available bytes; 96.81% used; 445108283 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84312420352 available bytes; 95.30% used; 114156042 free inodes.

server3 `/home`: 84312420352 available bytes; 95.30% used; 114156042 free inodes.

server3 `/data`: 142776655872 available bytes; 98.03% used; 225814900 free inodes.

server3 `/tmp`: 84312420352 available bytes; 95.30% used; 114156042 free inodes.

server3 `/var/tmp`: 84312420352 available bytes; 95.30% used; 114156042 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658617856 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658617856 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26281689088 available bytes; 99.64% used; 224959551 free inodes.

server4 `/tmp`: 105658617856 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658617856 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
