# V2R cluster inventory

2026-09-25T13:40:29.358933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319182626816 available bytes; 82.19% used; 112477035 free inodes.

server1 `/home`: 319182626816 available bytes; 82.19% used; 112477035 free inodes.

server1 `/tmp`: 319182626816 available bytes; 82.19% used; 112477035 free inodes.

server1 `/var/tmp`: 319182626816 available bytes; 82.19% used; 112477035 free inodes.

server1 `/mnt/raid5`: 367398748160 available bytes; 98.31% used; 337547751 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 16531976192 available bytes; 99.08% used; 110408639 free inodes.

server2 `/home`: 16531976192 available bytes; 99.08% used; 110408639 free inodes.

server2 `/tmp`: 16531976192 available bytes; 99.08% used; 110408639 free inodes.

server2 `/var/tmp`: 16531976192 available bytes; 99.08% used; 110408639 free inodes.

server2 `/mnt/raid5`: 323159379968 available bytes; 97.77% used; 445076942 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84282093568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84282093568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142347816960 available bytes; 98.03% used; 225809532 free inodes.

server3 `/tmp`: 84282093568 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84282093568 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655697408 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655697408 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231467470848 available bytes; 96.80% used; 224950450 free inodes.

server4 `/tmp`: 105655697408 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655697408 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
