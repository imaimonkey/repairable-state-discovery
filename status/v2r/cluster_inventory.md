# V2R cluster inventory

2026-09-25T13:54:13.609769+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319147859968 available bytes; 82.20% used; 112476961 free inodes.

server1 `/home`: 319147859968 available bytes; 82.20% used; 112476961 free inodes.

server1 `/tmp`: 319147859968 available bytes; 82.20% used; 112476961 free inodes.

server1 `/var/tmp`: 319147859968 available bytes; 82.20% used; 112476961 free inodes.

server1 `/mnt/raid5`: 364090482688 available bytes; 98.33% used; 337547522 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4725465088 available bytes; 99.74% used; 110407473 free inodes.

server2 `/home`: 4725465088 available bytes; 99.74% used; 110407473 free inodes.

server2 `/tmp`: 4725465088 available bytes; 99.74% used; 110407473 free inodes.

server2 `/var/tmp`: 4725465088 available bytes; 99.74% used; 110407473 free inodes.

server2 `/mnt/raid5`: 322486439936 available bytes; 97.77% used; 445076481 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280438784 available bytes; 95.30% used; 114154462 free inodes.

server3 `/home`: 84280438784 available bytes; 95.30% used; 114154462 free inodes.

server3 `/data`: 142290132992 available bytes; 98.03% used; 225809313 free inodes.

server3 `/tmp`: 84280438784 available bytes; 95.30% used; 114154462 free inodes.

server3 `/var/tmp`: 84280438784 available bytes; 95.30% used; 114154462 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655316480 available bytes; 94.10% used; 114349713 free inodes.

server4 `/home`: 105655316480 available bytes; 94.10% used; 114349713 free inodes.

server4 `/data`: 231434625024 available bytes; 96.80% used; 224949445 free inodes.

server4 `/tmp`: 105655316480 available bytes; 94.10% used; 114349713 free inodes.

server4 `/var/tmp`: 105655316480 available bytes; 94.10% used; 114349713 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
