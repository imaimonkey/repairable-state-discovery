# V2R cluster inventory

2026-09-25T15:51:57.262396+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318680735744 available bytes; 82.22% used; 112476523 free inodes.

server1 `/home`: 318680735744 available bytes; 82.22% used; 112476523 free inodes.

server1 `/tmp`: 318680735744 available bytes; 82.22% used; 112476523 free inodes.

server1 `/var/tmp`: 318680735744 available bytes; 82.22% used; 112476523 free inodes.

server1 `/mnt/raid5`: 363948756992 available bytes; 98.33% used; 337545503 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23109136384 available bytes; 98.71% used; 110407946 free inodes.

server2 `/home`: 23109136384 available bytes; 98.71% used; 110407946 free inodes.

server2 `/tmp`: 23109136384 available bytes; 98.71% used; 110407946 free inodes.

server2 `/var/tmp`: 23109136384 available bytes; 98.71% used; 110407946 free inodes.

server2 `/mnt/raid5`: 319417118720 available bytes; 97.79% used; 445071980 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84426809344 available bytes; 95.29% used; 114153471 free inodes.

server3 `/home`: 84426809344 available bytes; 95.29% used; 114153471 free inodes.

server3 `/data`: 142242078720 available bytes; 98.03% used; 225806872 free inodes.

server3 `/tmp`: 84426809344 available bytes; 95.29% used; 114153471 free inodes.

server3 `/var/tmp`: 84426809344 available bytes; 95.29% used; 114153471 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637302272 available bytes; 94.11% used; 114349677 free inodes.

server4 `/home`: 105637302272 available bytes; 94.11% used; 114349677 free inodes.

server4 `/data`: 231314722816 available bytes; 96.80% used; 224943688 free inodes.

server4 `/tmp`: 105637302272 available bytes; 94.11% used; 114349677 free inodes.

server4 `/var/tmp`: 105637302272 available bytes; 94.11% used; 114349677 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
