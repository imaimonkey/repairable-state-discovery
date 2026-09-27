# V2R cluster inventory

2026-09-27T04:05:26.978279+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315076722688 available bytes; 82.42% used; 112443050 free inodes.

server1 `/home`: 315076722688 available bytes; 82.42% used; 112443050 free inodes.

server1 `/tmp`: 315076722688 available bytes; 82.42% used; 112443050 free inodes.

server1 `/var/tmp`: 315076722688 available bytes; 82.42% used; 112443050 free inodes.

server1 `/mnt/raid5`: 636757606400 available bytes; 97.08% used; 337401269 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17631309824 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17631309824 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17631309824 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17631309824 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 577675882496 available bytes; 96.01% used; 444882602 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78696878080 available bytes; 95.61% used; 114062930 free inodes.

server3 `/home`: 78696878080 available bytes; 95.61% used; 114062930 free inodes.

server3 `/data`: 1335180951552 available bytes; 81.55% used; 225759655 free inodes.

server3 `/tmp`: 78696878080 available bytes; 95.61% used; 114062930 free inodes.

server3 `/var/tmp`: 78696878080 available bytes; 95.61% used; 114062930 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111018737664 available bytes; 93.80% used; 114372943 free inodes.

server4 `/home`: 111018737664 available bytes; 93.80% used; 114372943 free inodes.

server4 `/data`: 382180007936 available bytes; 94.72% used; 224780781 free inodes.

server4 `/tmp`: 111018737664 available bytes; 93.80% used; 114372943 free inodes.

server4 `/var/tmp`: 111018737664 available bytes; 93.80% used; 114372943 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
