# V2R cluster inventory

2026-09-27T09:00:57.163874+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314466213888 available bytes; 82.46% used; 112440730 free inodes.

server1 `/home`: 314466213888 available bytes; 82.46% used; 112440730 free inodes.

server1 `/tmp`: 314466213888 available bytes; 82.46% used; 112440730 free inodes.

server1 `/var/tmp`: 314466213888 available bytes; 82.46% used; 112440730 free inodes.

server1 `/mnt/raid5`: 634580889600 available bytes; 97.09% used; 337400193 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16652267520 available bytes; 99.07% used; 110357853 free inodes.

server2 `/home`: 16652267520 available bytes; 99.07% used; 110357853 free inodes.

server2 `/tmp`: 16652267520 available bytes; 99.07% used; 110357853 free inodes.

server2 `/var/tmp`: 16652267520 available bytes; 99.07% used; 110357853 free inodes.

server2 `/mnt/raid5`: 575119343616 available bytes; 96.03% used; 444744030 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78554886144 available bytes; 95.62% used; 114062864 free inodes.

server3 `/home`: 78554886144 available bytes; 95.62% used; 114062864 free inodes.

server3 `/data`: 1332578836480 available bytes; 81.58% used; 225762937 free inodes.

server3 `/tmp`: 78554886144 available bytes; 95.62% used; 114062864 free inodes.

server3 `/var/tmp`: 78554886144 available bytes; 95.62% used; 114062864 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111051255808 available bytes; 93.80% used; 114372862 free inodes.

server4 `/home`: 111051255808 available bytes; 93.80% used; 114372862 free inodes.

server4 `/data`: 364346347520 available bytes; 94.96% used; 224768834 free inodes.

server4 `/tmp`: 111051255808 available bytes; 93.80% used; 114372862 free inodes.

server4 `/var/tmp`: 111051255808 available bytes; 93.80% used; 114372862 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
