# V2R cluster inventory

2026-09-27T09:19:14.332998+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314460266496 available bytes; 82.46% used; 112440739 free inodes.

server1 `/home`: 314460266496 available bytes; 82.46% used; 112440739 free inodes.

server1 `/tmp`: 314460266496 available bytes; 82.46% used; 112440739 free inodes.

server1 `/var/tmp`: 314460266496 available bytes; 82.46% used; 112440739 free inodes.

server1 `/mnt/raid5`: 634557632512 available bytes; 97.09% used; 337400196 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16515985408 available bytes; 99.08% used; 110356967 free inodes.

server2 `/home`: 16515985408 available bytes; 99.08% used; 110356967 free inodes.

server2 `/tmp`: 16515985408 available bytes; 99.08% used; 110356967 free inodes.

server2 `/var/tmp`: 16515985408 available bytes; 99.08% used; 110356967 free inodes.

server2 `/mnt/raid5`: 573995393024 available bytes; 96.03% used; 444742289 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78555922432 available bytes; 95.62% used; 114062923 free inodes.

server3 `/home`: 78555922432 available bytes; 95.62% used; 114062923 free inodes.

server3 `/data`: 1332517113856 available bytes; 81.58% used; 225762637 free inodes.

server3 `/tmp`: 78555922432 available bytes; 95.62% used; 114062923 free inodes.

server3 `/var/tmp`: 78555922432 available bytes; 95.62% used; 114062923 free inodes.
| server4 | True | ['0', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111050752000 available bytes; 93.80% used; 114372860 free inodes.

server4 `/home`: 111050752000 available bytes; 93.80% used; 114372860 free inodes.

server4 `/data`: 364124086272 available bytes; 94.97% used; 224767544 free inodes.

server4 `/tmp`: 111050752000 available bytes; 93.80% used; 114372860 free inodes.

server4 `/var/tmp`: 111050752000 available bytes; 93.80% used; 114372860 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
