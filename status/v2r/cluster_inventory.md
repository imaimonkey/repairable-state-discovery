# V2R cluster inventory

2026-09-27T00:21:30.755294+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315166748672 available bytes; 82.42% used; 112443486 free inodes.

server1 `/home`: 315166748672 available bytes; 82.42% used; 112443486 free inodes.

server1 `/tmp`: 315166748672 available bytes; 82.42% used; 112443486 free inodes.

server1 `/var/tmp`: 315166748672 available bytes; 82.42% used; 112443486 free inodes.

server1 `/mnt/raid5`: 637712224256 available bytes; 97.07% used; 337407990 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17647742976 available bytes; 99.02% used; 110365156 free inodes.

server2 `/home`: 17647742976 available bytes; 99.02% used; 110365156 free inodes.

server2 `/tmp`: 17647742976 available bytes; 99.02% used; 110365156 free inodes.

server2 `/var/tmp`: 17647742976 available bytes; 99.02% used; 110365156 free inodes.

server2 `/mnt/raid5`: 593467961344 available bytes; 95.90% used; 444957595 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78634344448 available bytes; 95.61% used; 114068761 free inodes.

server3 `/home`: 78634344448 available bytes; 95.61% used; 114068761 free inodes.

server3 `/data`: 1349110816768 available bytes; 81.35% used; 225825728 free inodes.

server3 `/tmp`: 78634344448 available bytes; 95.61% used; 114068761 free inodes.

server3 `/var/tmp`: 78634344448 available bytes; 95.61% used; 114068761 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879560192 available bytes; 94.09% used; 114347847 free inodes.

server4 `/home`: 105879560192 available bytes; 94.09% used; 114347847 free inodes.

server4 `/data`: 409332776960 available bytes; 94.34% used; 224821781 free inodes.

server4 `/tmp`: 105879560192 available bytes; 94.09% used; 114347847 free inodes.

server4 `/var/tmp`: 105879560192 available bytes; 94.09% used; 114347847 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
