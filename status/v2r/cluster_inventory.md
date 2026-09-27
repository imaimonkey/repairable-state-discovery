# V2R cluster inventory

2026-09-27T03:41:03.807706+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315085529088 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315085529088 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315085529088 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315085529088 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636784050176 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17632227328 available bytes; 99.02% used; 110365017 free inodes.

server2 `/home`: 17632227328 available bytes; 99.02% used; 110365017 free inodes.

server2 `/tmp`: 17632227328 available bytes; 99.02% used; 110365017 free inodes.

server2 `/var/tmp`: 17632227328 available bytes; 99.02% used; 110365017 free inodes.

server2 `/mnt/raid5`: 578291552256 available bytes; 96.00% used; 444882595 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78699454464 available bytes; 95.61% used; 114062950 free inodes.

server3 `/home`: 78699454464 available bytes; 95.61% used; 114062950 free inodes.

server3 `/data`: 1335363743744 available bytes; 81.54% used; 225761357 free inodes.

server3 `/tmp`: 78699454464 available bytes; 95.61% used; 114062950 free inodes.

server3 `/var/tmp`: 78699454464 available bytes; 95.61% used; 114062950 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111027884032 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111027884032 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385470824448 available bytes; 94.67% used; 224780860 free inodes.

server4 `/tmp`: 111027884032 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111027884032 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
