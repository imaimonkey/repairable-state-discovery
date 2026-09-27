# V2R cluster inventory

2026-09-27T08:54:51.149253+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314468200448 available bytes; 82.46% used; 112440724 free inodes.

server1 `/home`: 314468200448 available bytes; 82.46% used; 112440724 free inodes.

server1 `/tmp`: 314468200448 available bytes; 82.46% used; 112440724 free inodes.

server1 `/var/tmp`: 314468200448 available bytes; 82.46% used; 112440724 free inodes.

server1 `/mnt/raid5`: 634581573632 available bytes; 97.09% used; 337400191 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17579622400 available bytes; 99.02% used; 110364374 free inodes.

server2 `/home`: 17579622400 available bytes; 99.02% used; 110364374 free inodes.

server2 `/tmp`: 17579622400 available bytes; 99.02% used; 110364374 free inodes.

server2 `/var/tmp`: 17579622400 available bytes; 99.02% used; 110364374 free inodes.

server2 `/mnt/raid5`: 575615246336 available bytes; 96.02% used; 444749411 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78555418624 available bytes; 95.62% used; 114062861 free inodes.

server3 `/home`: 78555418624 available bytes; 95.62% used; 114062861 free inodes.

server3 `/data`: 1332585291776 available bytes; 81.58% used; 225762993 free inodes.

server3 `/tmp`: 78555418624 available bytes; 95.62% used; 114062861 free inodes.

server3 `/var/tmp`: 78555418624 available bytes; 95.62% used; 114062861 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051476992 available bytes; 93.80% used; 114372879 free inodes.

server4 `/home`: 111051476992 available bytes; 93.80% used; 114372879 free inodes.

server4 `/data`: 366089465856 available bytes; 94.94% used; 224769334 free inodes.

server4 `/tmp`: 111051476992 available bytes; 93.80% used; 114372879 free inodes.

server4 `/var/tmp`: 111051476992 available bytes; 93.80% used; 114372879 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
