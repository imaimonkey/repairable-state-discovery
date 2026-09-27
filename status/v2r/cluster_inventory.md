# V2R cluster inventory

2026-09-27T03:35:50.881415+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086372864 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315086372864 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315086372864 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315086372864 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636783128576 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17632243712 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17632243712 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17632243712 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17632243712 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 578430619648 available bytes; 96.00% used; 444882604 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78709178368 available bytes; 95.61% used; 114062952 free inodes.

server3 `/home`: 78709178368 available bytes; 95.61% used; 114062952 free inodes.

server3 `/data`: 1335375679488 available bytes; 81.54% used; 225761415 free inodes.

server3 `/tmp`: 78709178368 available bytes; 95.61% used; 114062952 free inodes.

server3 `/var/tmp`: 78709178368 available bytes; 95.61% used; 114062952 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111028035584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028035584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385472487424 available bytes; 94.67% used; 224780874 free inodes.

server4 `/tmp`: 111028035584 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028035584 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
