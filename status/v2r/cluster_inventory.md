# V2R cluster inventory

2026-09-25T01:14:39.736348+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319079251968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/home`: 319079251968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/tmp`: 319079251968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/var/tmp`: 319079251968 available bytes; 82.20% used; 112480774 free inodes.

server1 `/mnt/raid5`: 416519450624 available bytes; 98.09% used; 337614754 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 23058812928 available bytes; 98.71% used; 110410772 free inodes.

server2 `/home`: 23058812928 available bytes; 98.71% used; 110410772 free inodes.

server2 `/tmp`: 23058812928 available bytes; 98.71% used; 110410772 free inodes.

server2 `/var/tmp`: 23058812928 available bytes; 98.71% used; 110410772 free inodes.

server2 `/mnt/raid5`: 498034774016 available bytes; 96.56% used; 445161859 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84353728512 available bytes; 95.29% used; 114156087 free inodes.

server3 `/home`: 84353728512 available bytes; 95.29% used; 114156087 free inodes.

server3 `/data`: 146959278080 available bytes; 97.97% used; 225812615 free inodes.

server3 `/tmp`: 84353728512 available bytes; 95.29% used; 114156087 free inodes.

server3 `/var/tmp`: 84353728512 available bytes; 95.29% used; 114156087 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779355648 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105779355648 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 53328449536 available bytes; 99.26% used; 225030764 free inodes.

server4 `/tmp`: 105779355648 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105779355648 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
