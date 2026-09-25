# V2R cluster inventory

2026-09-25T13:38:55.722098+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319183441920 available bytes; 82.19% used; 112477032 free inodes.

server1 `/home`: 319183441920 available bytes; 82.19% used; 112477032 free inodes.

server1 `/tmp`: 319183441920 available bytes; 82.19% used; 112477032 free inodes.

server1 `/var/tmp`: 319183441920 available bytes; 82.19% used; 112477032 free inodes.

server1 `/mnt/raid5`: 371500412928 available bytes; 98.30% used; 337547794 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 16533475328 available bytes; 99.08% used; 110408642 free inodes.

server2 `/home`: 16533475328 available bytes; 99.08% used; 110408642 free inodes.

server2 `/tmp`: 16533475328 available bytes; 99.08% used; 110408642 free inodes.

server2 `/var/tmp`: 16533475328 available bytes; 99.08% used; 110408642 free inodes.

server2 `/mnt/raid5`: 323203125248 available bytes; 97.77% used; 445077070 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84282179584 available bytes; 95.30% used; 114154464 free inodes.

server3 `/home`: 84282179584 available bytes; 95.30% used; 114154464 free inodes.

server3 `/data`: 142349041664 available bytes; 98.03% used; 225809551 free inodes.

server3 `/tmp`: 84282179584 available bytes; 95.30% used; 114154464 free inodes.

server3 `/var/tmp`: 84282179584 available bytes; 95.30% used; 114154464 free inodes.
| server4 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105655750656 available bytes; 94.10% used; 114349714 free inodes.

server4 `/home`: 105655750656 available bytes; 94.10% used; 114349714 free inodes.

server4 `/data`: 231388434432 available bytes; 96.80% used; 224951057 free inodes.

server4 `/tmp`: 105655750656 available bytes; 94.10% used; 114349714 free inodes.

server4 `/var/tmp`: 105655750656 available bytes; 94.10% used; 114349714 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
