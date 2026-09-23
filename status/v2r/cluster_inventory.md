# V2R cluster inventory

2026-09-23T22:47:31.155866+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325745143808 available bytes; 81.83% used; 112501727 free inodes.

server1 `/home`: 325745143808 available bytes; 81.83% used; 112501727 free inodes.

server1 `/tmp`: 325745143808 available bytes; 81.83% used; 112501727 free inodes.

server1 `/var/tmp`: 325745143808 available bytes; 81.83% used; 112501727 free inodes.

server1 `/mnt/raid5`: 1388115320832 available bytes; 93.63% used; 337739964 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41072291840 available bytes; 97.71% used; 110432621 free inodes.

server2 `/home`: 41072291840 available bytes; 97.71% used; 110432621 free inodes.

server2 `/tmp`: 41072291840 available bytes; 97.71% used; 110432621 free inodes.

server2 `/var/tmp`: 41072291840 available bytes; 97.71% used; 110432621 free inodes.

server2 `/mnt/raid5`: 536148389888 available bytes; 96.30% used; 445206359 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292546285568 available bytes; 83.67% used; 114193393 free inodes.

server3 `/home`: 292546285568 available bytes; 83.67% used; 114193393 free inodes.

server3 `/data`: 82436796416 available bytes; 98.86% used; 225846879 free inodes.

server3 `/tmp`: 292546285568 available bytes; 83.67% used; 114193393 free inodes.

server3 `/var/tmp`: 292546285568 available bytes; 83.67% used; 114193393 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106325626880 available bytes; 94.07% used; 114353907 free inodes.

server4 `/home`: 106325626880 available bytes; 94.07% used; 114353907 free inodes.

server4 `/data`: 300110372864 available bytes; 95.85% used; 225434487 free inodes.

server4 `/tmp`: 106325626880 available bytes; 94.07% used; 114353907 free inodes.

server4 `/var/tmp`: 106325626880 available bytes; 94.07% used; 114353907 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
