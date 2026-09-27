# V2R cluster inventory

2026-09-27T08:59:25.680176+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314466885632 available bytes; 82.46% used; 112440730 free inodes.

server1 `/home`: 314466885632 available bytes; 82.46% used; 112440730 free inodes.

server1 `/tmp`: 314466885632 available bytes; 82.46% used; 112440730 free inodes.

server1 `/var/tmp`: 314466885632 available bytes; 82.46% used; 112440730 free inodes.

server1 `/mnt/raid5`: 634582028288 available bytes; 97.09% used; 337400193 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 17253281792 available bytes; 99.04% used; 110357998 free inodes.

server2 `/home`: 17253281792 available bytes; 99.04% used; 110357998 free inodes.

server2 `/tmp`: 17253281792 available bytes; 99.04% used; 110357998 free inodes.

server2 `/var/tmp`: 17253281792 available bytes; 99.04% used; 110357998 free inodes.

server2 `/mnt/raid5`: 575182082048 available bytes; 96.03% used; 444744135 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78554992640 available bytes; 95.62% used; 114062864 free inodes.

server3 `/home`: 78554992640 available bytes; 95.62% used; 114062864 free inodes.

server3 `/data`: 1332579659776 available bytes; 81.58% used; 225762957 free inodes.

server3 `/tmp`: 78554992640 available bytes; 95.62% used; 114062864 free inodes.

server3 `/var/tmp`: 78554992640 available bytes; 95.62% used; 114062864 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051317248 available bytes; 93.80% used; 114372862 free inodes.

server4 `/home`: 111051317248 available bytes; 93.80% used; 114372862 free inodes.

server4 `/data`: 365795860480 available bytes; 94.94% used; 224768866 free inodes.

server4 `/tmp`: 111051317248 available bytes; 93.80% used; 114372862 free inodes.

server4 `/var/tmp`: 111051317248 available bytes; 93.80% used; 114372862 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
