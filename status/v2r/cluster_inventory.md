# V2R cluster inventory

2026-09-26T07:20:25.739626+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318767935488 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318767935488 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318767935488 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318767935488 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219261931520 available bytes; 98.99% used; 337539295 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320218112 available bytes; 98.75% used; 110403882 free inodes.

server2 `/home`: 22320218112 available bytes; 98.75% used; 110403882 free inodes.

server2 `/tmp`: 22320218112 available bytes; 98.75% used; 110403882 free inodes.

server2 `/var/tmp`: 22320218112 available bytes; 98.75% used; 110403882 free inodes.

server2 `/mnt/raid5`: 271533641728 available bytes; 98.12% used; 445027209 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82679713792 available bytes; 95.39% used; 114110895 free inodes.

server3 `/home`: 82679713792 available bytes; 95.39% used; 114110895 free inodes.

server3 `/data`: 123980599296 available bytes; 98.29% used; 225821233 free inodes.

server3 `/tmp`: 82679713792 available bytes; 95.39% used; 114110895 free inodes.

server3 `/var/tmp`: 82679713792 available bytes; 95.39% used; 114110895 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074738688 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106074738688 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105869819904 available bytes; 98.54% used; 224922733 free inodes.

server4 `/tmp`: 106074738688 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106074738688 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
