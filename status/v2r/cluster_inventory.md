# V2R cluster inventory

2026-09-26T06:05:36.722713+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318778220544 available bytes; 82.22% used; 112476286 free inodes.

server1 `/home`: 318778220544 available bytes; 82.22% used; 112476286 free inodes.

server1 `/tmp`: 318778220544 available bytes; 82.22% used; 112476286 free inodes.

server1 `/var/tmp`: 318778220544 available bytes; 82.22% used; 112476286 free inodes.

server1 `/mnt/raid5`: 225914417152 available bytes; 98.96% used; 337539946 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22737715200 available bytes; 98.73% used; 110405657 free inodes.

server2 `/home`: 22737715200 available bytes; 98.73% used; 110405657 free inodes.

server2 `/tmp`: 22737715200 available bytes; 98.73% used; 110405657 free inodes.

server2 `/var/tmp`: 22737715200 available bytes; 98.73% used; 110405657 free inodes.

server2 `/mnt/raid5`: 274421125120 available bytes; 98.10% used; 445033676 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82431201280 available bytes; 95.40% used; 114110913 free inodes.

server3 `/home`: 82431201280 available bytes; 95.40% used; 114110913 free inodes.

server3 `/data`: 123990372352 available bytes; 98.29% used; 225822683 free inodes.

server3 `/tmp`: 82431201280 available bytes; 95.40% used; 114110913 free inodes.

server3 `/var/tmp`: 82431201280 available bytes; 95.40% used; 114110913 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106093936640 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106093936640 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106988056576 available bytes; 98.52% used; 224929127 free inodes.

server4 `/tmp`: 106093936640 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106093936640 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
