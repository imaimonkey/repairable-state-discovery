# V2R cluster inventory

2026-09-27T03:37:22.458976+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086348288 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315086348288 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315086348288 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315086348288 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636783497216 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17632219136 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17632219136 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17632219136 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17632219136 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 578384556032 available bytes; 96.00% used; 444882560 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78708924416 available bytes; 95.61% used; 114062952 free inodes.

server3 `/home`: 78708924416 available bytes; 95.61% used; 114062952 free inodes.

server3 `/data`: 1335375233024 available bytes; 81.54% used; 225761395 free inodes.

server3 `/tmp`: 78708924416 available bytes; 95.61% used; 114062952 free inodes.

server3 `/var/tmp`: 78708924416 available bytes; 95.61% used; 114062952 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111027994624 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111027994624 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385471598592 available bytes; 94.67% used; 224780869 free inodes.

server4 `/tmp`: 111027994624 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111027994624 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
