# V2R cluster inventory

2026-09-27T02:59:15.502346+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315086544896 available bytes; 82.42% used; 112443059 free inodes.

server1 `/home`: 315086544896 available bytes; 82.42% used; 112443059 free inodes.

server1 `/tmp`: 315086544896 available bytes; 82.42% used; 112443059 free inodes.

server1 `/var/tmp`: 315086544896 available bytes; 82.42% used; 112443059 free inodes.

server1 `/mnt/raid5`: 636812431360 available bytes; 97.08% used; 337401386 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17633648640 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17633648640 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17633648640 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17633648640 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 580144508928 available bytes; 95.99% used; 444883765 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78705545216 available bytes; 95.61% used; 114062940 free inodes.

server3 `/home`: 78705545216 available bytes; 95.61% used; 114062940 free inodes.

server3 `/data`: 1336572420096 available bytes; 81.53% used; 225761847 free inodes.

server3 `/tmp`: 78705545216 available bytes; 95.61% used; 114062940 free inodes.

server3 `/var/tmp`: 78705545216 available bytes; 95.61% used; 114062940 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111033077760 available bytes; 93.80% used; 114373144 free inodes.

server4 `/home`: 111033077760 available bytes; 93.80% used; 114373144 free inodes.

server4 `/data`: 396885266432 available bytes; 94.51% used; 224781277 free inodes.

server4 `/tmp`: 111033077760 available bytes; 93.80% used; 114373144 free inodes.

server4 `/var/tmp`: 111033077760 available bytes; 93.80% used; 114373144 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
