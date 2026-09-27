# V2R cluster inventory

2026-09-27T05:39:52.176438+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314490638336 available bytes; 82.46% used; 112440821 free inodes.

server1 `/home`: 314490638336 available bytes; 82.46% used; 112440821 free inodes.

server1 `/tmp`: 314490638336 available bytes; 82.46% used; 112440821 free inodes.

server1 `/var/tmp`: 314490638336 available bytes; 82.46% used; 112440821 free inodes.

server1 `/mnt/raid5`: 634735661056 available bytes; 97.09% used; 337400017 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17622847488 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17622847488 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17622847488 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17622847488 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 574814130176 available bytes; 96.03% used; 444877316 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78576160768 available bytes; 95.62% used; 114062908 free inodes.

server3 `/home`: 78576160768 available bytes; 95.62% used; 114062908 free inodes.

server3 `/data`: 1333394833408 available bytes; 81.57% used; 225766169 free inodes.

server3 `/tmp`: 78576160768 available bytes; 95.62% used; 114062908 free inodes.

server3 `/var/tmp`: 78576160768 available bytes; 95.62% used; 114062908 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110999420928 available bytes; 93.81% used; 114372900 free inodes.

server4 `/home`: 110999420928 available bytes; 93.81% used; 114372900 free inodes.

server4 `/data`: 374575468544 available bytes; 94.82% used; 224771221 free inodes.

server4 `/tmp`: 110999420928 available bytes; 93.81% used; 114372900 free inodes.

server4 `/var/tmp`: 110999420928 available bytes; 93.81% used; 114372900 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
