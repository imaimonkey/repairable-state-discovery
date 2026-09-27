# V2R cluster inventory

2026-09-27T00:27:36.229466+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315060117504 available bytes; 82.42% used; 112443436 free inodes.

server1 `/home`: 315060117504 available bytes; 82.42% used; 112443436 free inodes.

server1 `/tmp`: 315060117504 available bytes; 82.42% used; 112443436 free inodes.

server1 `/var/tmp`: 315060117504 available bytes; 82.42% used; 112443436 free inodes.

server1 `/mnt/raid5`: 637698441216 available bytes; 97.07% used; 337407760 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 17640054784 available bytes; 99.02% used; 110365088 free inodes.

server2 `/home`: 17640054784 available bytes; 99.02% used; 110365088 free inodes.

server2 `/tmp`: 17640054784 available bytes; 99.02% used; 110365088 free inodes.

server2 `/var/tmp`: 17640054784 available bytes; 99.02% used; 110365088 free inodes.

server2 `/mnt/raid5`: 593280692224 available bytes; 95.90% used; 444957078 free inodes.
| server3 | True | ['2', '3'] | [] | reference_compatible=True |

server3 `/`: 79499137024 available bytes; 95.56% used; 114068709 free inodes.

server3 `/home`: 79499137024 available bytes; 95.56% used; 114068709 free inodes.

server3 `/data`: 1349105614848 available bytes; 81.35% used; 225825590 free inodes.

server3 `/tmp`: 79499137024 available bytes; 95.56% used; 114068709 free inodes.

server3 `/var/tmp`: 79499137024 available bytes; 95.56% used; 114068709 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879392256 available bytes; 94.09% used; 114347839 free inodes.

server4 `/home`: 105879392256 available bytes; 94.09% used; 114347839 free inodes.

server4 `/data`: 409236049920 available bytes; 94.34% used; 224820704 free inodes.

server4 `/tmp`: 105879392256 available bytes; 94.09% used; 114347839 free inodes.

server4 `/var/tmp`: 105879392256 available bytes; 94.09% used; 114347839 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
