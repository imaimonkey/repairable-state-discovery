# V2R cluster inventory

2026-09-25T05:16:46.087178+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318890409984 available bytes; 82.21% used; 112480261 free inodes.

server1 `/home`: 318890409984 available bytes; 82.21% used; 112480261 free inodes.

server1 `/tmp`: 318890409984 available bytes; 82.21% used; 112480261 free inodes.

server1 `/var/tmp`: 318890409984 available bytes; 82.21% used; 112480261 free inodes.

server1 `/mnt/raid5`: 408536096768 available bytes; 98.13% used; 337569917 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22930259968 available bytes; 98.72% used; 110410428 free inodes.

server2 `/home`: 22930259968 available bytes; 98.72% used; 110410428 free inodes.

server2 `/tmp`: 22930259968 available bytes; 98.72% used; 110410428 free inodes.

server2 `/var/tmp`: 22930259968 available bytes; 98.72% used; 110410428 free inodes.

server2 `/mnt/raid5`: 461589061632 available bytes; 96.81% used; 445108549 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84338528256 available bytes; 95.29% used; 114156049 free inodes.

server3 `/home`: 84338528256 available bytes; 95.29% used; 114156049 free inodes.

server3 `/data`: 142786248704 available bytes; 98.03% used; 225815127 free inodes.

server3 `/tmp`: 84338528256 available bytes; 95.29% used; 114156049 free inodes.

server3 `/var/tmp`: 84338528256 available bytes; 95.29% used; 114156049 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105658863616 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658863616 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26299072512 available bytes; 99.64% used; 224960103 free inodes.

server4 `/tmp`: 105658863616 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658863616 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
