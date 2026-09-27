# V2R cluster inventory

2026-09-27T08:33:29.690312+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314466152448 available bytes; 82.46% used; 112440720 free inodes.

server1 `/home`: 314466152448 available bytes; 82.46% used; 112440720 free inodes.

server1 `/tmp`: 314466152448 available bytes; 82.46% used; 112440720 free inodes.

server1 `/var/tmp`: 314466152448 available bytes; 82.46% used; 112440720 free inodes.

server1 `/mnt/raid5`: 634588971008 available bytes; 97.09% used; 337400003 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17605492736 available bytes; 99.02% used; 110364878 free inodes.

server2 `/home`: 17605492736 available bytes; 99.02% used; 110364878 free inodes.

server2 `/tmp`: 17605492736 available bytes; 99.02% used; 110364878 free inodes.

server2 `/var/tmp`: 17605492736 available bytes; 99.02% used; 110364878 free inodes.

server2 `/mnt/raid5`: 575978651648 available bytes; 96.02% used; 444751586 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78572756992 available bytes; 95.62% used; 114062868 free inodes.

server3 `/home`: 78572756992 available bytes; 95.62% used; 114062868 free inodes.

server3 `/data`: 1332704530432 available bytes; 81.58% used; 225763323 free inodes.

server3 `/tmp`: 78572756992 available bytes; 95.62% used; 114062868 free inodes.

server3 `/var/tmp`: 78572756992 available bytes; 95.62% used; 114062868 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111052062720 available bytes; 93.80% used; 114372882 free inodes.

server4 `/home`: 111052062720 available bytes; 93.80% used; 114372882 free inodes.

server4 `/data`: 367895740416 available bytes; 94.92% used; 224770755 free inodes.

server4 `/tmp`: 111052062720 available bytes; 93.80% used; 114372882 free inodes.

server4 `/var/tmp`: 111052062720 available bytes; 93.80% used; 114372882 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
