# V2R cluster inventory

2026-09-25T18:44:39.158098+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318743810048 available bytes; 82.22% used; 112476344 free inodes.

server1 `/home`: 318743810048 available bytes; 82.22% used; 112476344 free inodes.

server1 `/tmp`: 318743810048 available bytes; 82.22% used; 112476344 free inodes.

server1 `/var/tmp`: 318743810048 available bytes; 82.22% used; 112476344 free inodes.

server1 `/mnt/raid5`: 371166502912 available bytes; 98.30% used; 337541447 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23095808000 available bytes; 98.71% used; 110407938 free inodes.

server2 `/home`: 23095808000 available bytes; 98.71% used; 110407938 free inodes.

server2 `/tmp`: 23095808000 available bytes; 98.71% used; 110407938 free inodes.

server2 `/var/tmp`: 23095808000 available bytes; 98.71% used; 110407938 free inodes.

server2 `/mnt/raid5`: 313529729024 available bytes; 97.83% used; 445065838 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84380913664 available bytes; 95.29% used; 114152621 free inodes.

server3 `/home`: 84380913664 available bytes; 95.29% used; 114152621 free inodes.

server3 `/data`: 131383349248 available bytes; 98.18% used; 225809465 free inodes.

server3 `/tmp`: 84380913664 available bytes; 95.29% used; 114152621 free inodes.

server3 `/var/tmp`: 84380913664 available bytes; 95.29% used; 114152621 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105607081984 available bytes; 94.11% used; 114349599 free inodes.

server4 `/home`: 105607081984 available bytes; 94.11% used; 114349599 free inodes.

server4 `/data`: 229694455808 available bytes; 96.83% used; 224931550 free inodes.

server4 `/tmp`: 105607081984 available bytes; 94.11% used; 114349599 free inodes.

server4 `/var/tmp`: 105607081984 available bytes; 94.11% used; 114349599 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
