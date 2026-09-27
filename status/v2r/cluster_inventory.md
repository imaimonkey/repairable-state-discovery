# V2R cluster inventory

2026-09-27T09:15:52.818360+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314461102080 available bytes; 82.46% used; 112440741 free inodes.

server1 `/home`: 314461102080 available bytes; 82.46% used; 112440741 free inodes.

server1 `/tmp`: 314461102080 available bytes; 82.46% used; 112440741 free inodes.

server1 `/var/tmp`: 314461102080 available bytes; 82.46% used; 112440741 free inodes.

server1 `/mnt/raid5`: 634580570112 available bytes; 97.09% used; 337400197 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16516730880 available bytes; 99.08% used; 110356969 free inodes.

server2 `/home`: 16516730880 available bytes; 99.08% used; 110356969 free inodes.

server2 `/tmp`: 16516730880 available bytes; 99.08% used; 110356969 free inodes.

server2 `/var/tmp`: 16516730880 available bytes; 99.08% used; 110356969 free inodes.

server2 `/mnt/raid5`: 574083563520 available bytes; 96.03% used; 444741991 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78555463680 available bytes; 95.62% used; 114062920 free inodes.

server3 `/home`: 78555463680 available bytes; 95.62% used; 114062920 free inodes.

server3 `/data`: 1332574388224 available bytes; 81.58% used; 225762716 free inodes.

server3 `/tmp`: 78555463680 available bytes; 95.62% used; 114062920 free inodes.

server3 `/var/tmp`: 78555463680 available bytes; 95.62% used; 114062920 free inodes.
| server4 | True | ['4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111050870784 available bytes; 93.80% used; 114372868 free inodes.

server4 `/home`: 111050870784 available bytes; 93.80% used; 114372868 free inodes.

server4 `/data`: 364206665728 available bytes; 94.97% used; 224767869 free inodes.

server4 `/tmp`: 111050870784 available bytes; 93.80% used; 114372868 free inodes.

server4 `/var/tmp`: 111050870784 available bytes; 93.80% used; 114372868 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
