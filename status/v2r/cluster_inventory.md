# V2R cluster inventory

2026-09-27T04:35:18.442461+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314904821760 available bytes; 82.43% used; 112443032 free inodes.

server1 `/home`: 314904821760 available bytes; 82.43% used; 112443032 free inodes.

server1 `/tmp`: 314904821760 available bytes; 82.43% used; 112443032 free inodes.

server1 `/var/tmp`: 314904821760 available bytes; 82.43% used; 112443032 free inodes.

server1 `/mnt/raid5`: 636062650368 available bytes; 97.08% used; 337400322 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17621868544 available bytes; 99.02% used; 110365001 free inodes.

server2 `/home`: 17621868544 available bytes; 99.02% used; 110365001 free inodes.

server2 `/tmp`: 17621868544 available bytes; 99.02% used; 110365001 free inodes.

server2 `/var/tmp`: 17621868544 available bytes; 99.02% used; 110365001 free inodes.

server2 `/mnt/raid5`: 576679899136 available bytes; 96.02% used; 444879299 free inodes.
| server3 | True | ['2'] | [] |

server3 `/`: 78695178240 available bytes; 95.61% used; 114062928 free inodes.

server3 `/home`: 78695178240 available bytes; 95.61% used; 114062928 free inodes.

server3 `/data`: 1335065923584 available bytes; 81.55% used; 225759132 free inodes.

server3 `/tmp`: 78695178240 available bytes; 95.61% used; 114062928 free inodes.

server3 `/var/tmp`: 78695178240 available bytes; 95.61% used; 114062928 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111017234432 available bytes; 93.80% used; 114372932 free inodes.

server4 `/home`: 111017234432 available bytes; 93.80% used; 114372932 free inodes.

server4 `/data`: 382115336192 available bytes; 94.72% used; 224780554 free inodes.

server4 `/tmp`: 111017234432 available bytes; 93.80% used; 114372932 free inodes.

server4 `/var/tmp`: 111017234432 available bytes; 93.80% used; 114372932 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
