# V2R cluster inventory

2026-09-27T03:31:16.553460+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315085127680 available bytes; 82.42% used; 112443051 free inodes.

server1 `/home`: 315085127680 available bytes; 82.42% used; 112443051 free inodes.

server1 `/tmp`: 315085127680 available bytes; 82.42% used; 112443051 free inodes.

server1 `/var/tmp`: 315085127680 available bytes; 82.42% used; 112443051 free inodes.

server1 `/mnt/raid5`: 636785004544 available bytes; 97.08% used; 337401379 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17633480704 available bytes; 99.02% used; 110365015 free inodes.

server2 `/home`: 17633480704 available bytes; 99.02% used; 110365015 free inodes.

server2 `/tmp`: 17633480704 available bytes; 99.02% used; 110365015 free inodes.

server2 `/var/tmp`: 17633480704 available bytes; 99.02% used; 110365015 free inodes.

server2 `/mnt/raid5`: 578553663488 available bytes; 96.00% used; 444882729 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78708817920 available bytes; 95.61% used; 114062950 free inodes.

server3 `/home`: 78708817920 available bytes; 95.61% used; 114062950 free inodes.

server3 `/data`: 1336441479168 available bytes; 81.53% used; 225761468 free inodes.

server3 `/tmp`: 78708817920 available bytes; 95.61% used; 114062950 free inodes.

server3 `/var/tmp`: 78708817920 available bytes; 95.61% used; 114062950 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111028125696 available bytes; 93.80% used; 114372980 free inodes.

server4 `/home`: 111028125696 available bytes; 93.80% used; 114372980 free inodes.

server4 `/data`: 385483399168 available bytes; 94.67% used; 224780884 free inodes.

server4 `/tmp`: 111028125696 available bytes; 93.80% used; 114372980 free inodes.

server4 `/var/tmp`: 111028125696 available bytes; 93.80% used; 114372980 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
