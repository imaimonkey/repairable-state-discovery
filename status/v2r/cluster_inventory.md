# V2R cluster inventory

2026-09-24T21:40:40.879407+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323954724864 available bytes; 81.93% used; 112481419 free inodes.

server1 `/home`: 323954724864 available bytes; 81.93% used; 112481419 free inodes.

server1 `/tmp`: 323954724864 available bytes; 81.93% used; 112481419 free inodes.

server1 `/var/tmp`: 323954724864 available bytes; 81.93% used; 112481419 free inodes.

server1 `/mnt/raid5`: 415481520128 available bytes; 98.09% used; 337626234 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 30138085376 available bytes; 98.32% used; 110411316 free inodes.

server2 `/home`: 30138085376 available bytes; 98.32% used; 110411316 free inodes.

server2 `/tmp`: 30138085376 available bytes; 98.32% used; 110411316 free inodes.

server2 `/var/tmp`: 30138085376 available bytes; 98.32% used; 110411316 free inodes.

server2 `/mnt/raid5`: 490074914816 available bytes; 96.61% used; 445154714 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84384927744 available bytes; 95.29% used; 114156093 free inodes.

server3 `/home`: 84384927744 available bytes; 95.29% used; 114156093 free inodes.

server3 `/data`: 150131924992 available bytes; 97.93% used; 225803005 free inodes.

server3 `/tmp`: 84384927744 available bytes; 95.29% used; 114156093 free inodes.

server3 `/var/tmp`: 84384927744 available bytes; 95.29% used; 114156093 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105629814784 available bytes; 94.11% used; 114348347 free inodes.

server4 `/home`: 105629814784 available bytes; 94.11% used; 114348347 free inodes.

server4 `/data`: 81698553856 available bytes; 98.87% used; 225252423 free inodes.

server4 `/tmp`: 105629814784 available bytes; 94.11% used; 114348347 free inodes.

server4 `/var/tmp`: 105629814784 available bytes; 94.11% used; 114348347 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
