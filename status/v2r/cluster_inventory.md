# V2R cluster inventory

2026-09-25T13:55:45.182571+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319153848320 available bytes; 82.20% used; 112476964 free inodes.

server1 `/home`: 319153848320 available bytes; 82.20% used; 112476964 free inodes.

server1 `/tmp`: 319153848320 available bytes; 82.20% used; 112476964 free inodes.

server1 `/var/tmp`: 319153848320 available bytes; 82.20% used; 112476964 free inodes.

server1 `/mnt/raid5`: 364090826752 available bytes; 98.33% used; 337547520 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4735172608 available bytes; 99.74% used; 110407474 free inodes.

server2 `/home`: 4735172608 available bytes; 99.74% used; 110407474 free inodes.

server2 `/tmp`: 4735172608 available bytes; 99.74% used; 110407474 free inodes.

server2 `/var/tmp`: 4735172608 available bytes; 99.74% used; 110407474 free inodes.

server2 `/mnt/raid5`: 322448408576 available bytes; 97.77% used; 445076426 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84280553472 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84280553472 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142289735680 available bytes; 98.03% used; 225809254 free inodes.

server3 `/tmp`: 84280553472 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84280553472 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655287808 available bytes; 94.10% used; 114349713 free inodes.

server4 `/home`: 105655287808 available bytes; 94.10% used; 114349713 free inodes.

server4 `/data`: 231433826304 available bytes; 96.80% used; 224949337 free inodes.

server4 `/tmp`: 105655287808 available bytes; 94.10% used; 114349713 free inodes.

server4 `/var/tmp`: 105655287808 available bytes; 94.10% used; 114349713 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
