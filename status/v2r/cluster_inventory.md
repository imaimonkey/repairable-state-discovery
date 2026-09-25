# V2R cluster inventory

2026-09-25T04:09:50.406001+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318931202048 available bytes; 82.21% used; 112480381 free inodes.

server1 `/home`: 318931202048 available bytes; 82.21% used; 112480381 free inodes.

server1 `/tmp`: 318931202048 available bytes; 82.21% used; 112480381 free inodes.

server1 `/var/tmp`: 318931202048 available bytes; 82.21% used; 112480381 free inodes.

server1 `/mnt/raid5`: 395026489344 available bytes; 98.19% used; 337594156 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22966001664 available bytes; 98.72% used; 110410446 free inodes.

server2 `/home`: 22966001664 available bytes; 98.72% used; 110410446 free inodes.

server2 `/tmp`: 22966001664 available bytes; 98.72% used; 110410446 free inodes.

server2 `/var/tmp`: 22966001664 available bytes; 98.72% used; 110410446 free inodes.

server2 `/mnt/raid5`: 463128629248 available bytes; 96.80% used; 445110679 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84341227520 available bytes; 95.29% used; 114156072 free inodes.

server3 `/home`: 84341227520 available bytes; 95.29% used; 114156072 free inodes.

server3 `/data`: 143937150976 available bytes; 98.01% used; 225816570 free inodes.

server3 `/tmp`: 84341227520 available bytes; 95.29% used; 114156072 free inodes.

server3 `/var/tmp`: 84341227520 available bytes; 95.29% used; 114156072 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105674199040 available bytes; 94.10% used; 114350881 free inodes.

server4 `/home`: 105674199040 available bytes; 94.10% used; 114350881 free inodes.

server4 `/data`: 33699983360 available bytes; 99.53% used; 224964033 free inodes.

server4 `/tmp`: 105674199040 available bytes; 94.10% used; 114350881 free inodes.

server4 `/var/tmp`: 105674199040 available bytes; 94.10% used; 114350881 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
