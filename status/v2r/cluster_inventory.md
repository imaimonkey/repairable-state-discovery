# V2R cluster inventory

2026-09-25T13:48:07.341133+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319159730176 available bytes; 82.20% used; 112476970 free inodes.

server1 `/home`: 319159730176 available bytes; 82.20% used; 112476970 free inodes.

server1 `/tmp`: 319159730176 available bytes; 82.20% used; 112476970 free inodes.

server1 `/var/tmp`: 319159730176 available bytes; 82.20% used; 112476970 free inodes.

server1 `/mnt/raid5`: 364125401088 available bytes; 98.33% used; 337547585 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 18780962816 available bytes; 98.95% used; 110408216 free inodes.

server2 `/home`: 18780962816 available bytes; 98.95% used; 110408216 free inodes.

server2 `/tmp`: 18780962816 available bytes; 98.95% used; 110408216 free inodes.

server2 `/var/tmp`: 18780962816 available bytes; 98.95% used; 110408216 free inodes.

server2 `/mnt/raid5`: 322656194560 available bytes; 97.77% used; 445076584 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142347673600 available bytes; 98.03% used; 225809404 free inodes.

server3 `/tmp`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84281057280 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655468032 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655468032 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231460962304 available bytes; 96.80% used; 224949888 free inodes.

server4 `/tmp`: 105655468032 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655468032 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
