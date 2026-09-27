# V2R cluster inventory

2026-09-27T00:33:41.819140+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315154116608 available bytes; 82.42% used; 112443466 free inodes.

server1 `/home`: 315154116608 available bytes; 82.42% used; 112443466 free inodes.

server1 `/tmp`: 315154116608 available bytes; 82.42% used; 112443466 free inodes.

server1 `/var/tmp`: 315154116608 available bytes; 82.42% used; 112443466 free inodes.

server1 `/mnt/raid5`: 637681405952 available bytes; 97.07% used; 337407663 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17631145984 available bytes; 99.02% used; 110365010 free inodes.

server2 `/home`: 17631145984 available bytes; 99.02% used; 110365010 free inodes.

server2 `/tmp`: 17631145984 available bytes; 99.02% used; 110365010 free inodes.

server2 `/var/tmp`: 17631145984 available bytes; 99.02% used; 110365010 free inodes.

server2 `/mnt/raid5`: 593099407360 available bytes; 95.90% used; 444957035 free inodes.
| server3 | True | ['3'] | [] | reference_compatible=True |

server3 `/`: 78863855616 available bytes; 95.60% used; 114068621 free inodes.

server3 `/home`: 78863851520 available bytes; 95.60% used; 114068621 free inodes.

server3 `/data`: 1349105065984 available bytes; 81.35% used; 225825527 free inodes.

server3 `/tmp`: 78863851520 available bytes; 95.60% used; 114068621 free inodes.

server3 `/var/tmp`: 78863851520 available bytes; 95.60% used; 114068621 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879228416 available bytes; 94.09% used; 114347836 free inodes.

server4 `/home`: 105879228416 available bytes; 94.09% used; 114347836 free inodes.

server4 `/data`: 409211600896 available bytes; 94.34% used; 224820613 free inodes.

server4 `/tmp`: 105879228416 available bytes; 94.09% used; 114347836 free inodes.

server4 `/var/tmp`: 105879228416 available bytes; 94.09% used; 114347836 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
