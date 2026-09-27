# V2R cluster inventory

2026-09-27T03:39:32.421558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315085586432 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315085586432 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315085586432 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315085586432 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636782682112 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17631744000 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17631744000 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17631744000 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17631744000 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 578322071552 available bytes; 96.00% used; 444882371 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78699749376 available bytes; 95.61% used; 114062950 free inodes.

server3 `/home`: 78699749376 available bytes; 95.61% used; 114062950 free inodes.

server3 `/data`: 1335375241216 available bytes; 81.54% used; 225761377 free inodes.

server3 `/tmp`: 78699749376 available bytes; 95.61% used; 114062950 free inodes.

server3 `/var/tmp`: 78699749376 available bytes; 95.61% used; 114062950 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027933184 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111027933184 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385467858944 available bytes; 94.67% used; 224780860 free inodes.

server4 `/tmp`: 111027933184 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111027933184 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
