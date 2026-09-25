# V2R cluster inventory

2026-09-25T15:10:42.770489+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319116328960 available bytes; 82.20% used; 112476962 free inodes.

server1 `/home`: 319116328960 available bytes; 82.20% used; 112476962 free inodes.

server1 `/tmp`: 319116328960 available bytes; 82.20% used; 112476962 free inodes.

server1 `/var/tmp`: 319116328960 available bytes; 82.20% used; 112476962 free inodes.

server1 `/mnt/raid5`: 365697277952 available bytes; 98.32% used; 337545983 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23110664192 available bytes; 98.71% used; 110407926 free inodes.

server2 `/home`: 23110664192 available bytes; 98.71% used; 110407926 free inodes.

server2 `/tmp`: 23110664192 available bytes; 98.71% used; 110407926 free inodes.

server2 `/var/tmp`: 23110664192 available bytes; 98.71% used; 110407926 free inodes.

server2 `/mnt/raid5`: 319982288896 available bytes; 97.79% used; 445073722 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84425887744 available bytes; 95.29% used; 114153454 free inodes.

server3 `/home`: 84425887744 available bytes; 95.29% used; 114153454 free inodes.

server3 `/data`: 142187003904 available bytes; 98.03% used; 225808038 free inodes.

server3 `/tmp`: 84425887744 available bytes; 95.29% used; 114153454 free inodes.

server3 `/var/tmp`: 84425887744 available bytes; 95.29% used; 114153454 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105638494208 available bytes; 94.10% used; 114349692 free inodes.

server4 `/home`: 105638494208 available bytes; 94.10% used; 114349692 free inodes.

server4 `/data`: 231350964224 available bytes; 96.80% used; 224944797 free inodes.

server4 `/tmp`: 105638494208 available bytes; 94.10% used; 114349692 free inodes.

server4 `/var/tmp`: 105638494208 available bytes; 94.10% used; 114349692 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
