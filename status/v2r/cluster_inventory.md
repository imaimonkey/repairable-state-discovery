# V2R cluster inventory

2026-09-27T02:51:38.050632+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315082915840 available bytes; 82.42% used; 112443417 free inodes.

server1 `/home`: 315082915840 available bytes; 82.42% used; 112443417 free inodes.

server1 `/tmp`: 315082915840 available bytes; 82.42% used; 112443417 free inodes.

server1 `/var/tmp`: 315082915840 available bytes; 82.42% used; 112443417 free inodes.

server1 `/mnt/raid5`: 636843503616 available bytes; 97.08% used; 337401537 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17627033600 available bytes; 99.02% used; 110365006 free inodes.

server2 `/home`: 17627033600 available bytes; 99.02% used; 110365006 free inodes.

server2 `/tmp`: 17627033600 available bytes; 99.02% used; 110365006 free inodes.

server2 `/var/tmp`: 17627033600 available bytes; 99.02% used; 110365006 free inodes.

server2 `/mnt/raid5`: 579812958208 available bytes; 95.99% used; 444883726 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78709555200 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78709555200 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1336593510400 available bytes; 81.53% used; 225762037 free inodes.

server3 `/tmp`: 78709555200 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78709555200 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111035777024 available bytes; 93.80% used; 114373255 free inodes.

server4 `/home`: 111035777024 available bytes; 93.80% used; 114373255 free inodes.

server4 `/data`: 396940267520 available bytes; 94.51% used; 224781443 free inodes.

server4 `/tmp`: 111035777024 available bytes; 93.80% used; 114373255 free inodes.

server4 `/var/tmp`: 111035777024 available bytes; 93.80% used; 114373255 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
