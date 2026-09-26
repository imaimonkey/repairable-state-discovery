# V2R cluster inventory

2026-09-26T09:10:17.257066+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318735728640 available bytes; 82.22% used; 112475795 free inodes.

server1 `/home`: 318735728640 available bytes; 82.22% used; 112475795 free inodes.

server1 `/tmp`: 318735728640 available bytes; 82.22% used; 112475795 free inodes.

server1 `/var/tmp`: 318735728640 available bytes; 82.22% used; 112475795 free inodes.

server1 `/mnt/raid5`: 219011182592 available bytes; 99.00% used; 337538748 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22319194112 available bytes; 98.75% used; 110403909 free inodes.

server2 `/home`: 22319194112 available bytes; 98.75% used; 110403909 free inodes.

server2 `/tmp`: 22319194112 available bytes; 98.75% used; 110403909 free inodes.

server2 `/var/tmp`: 22319194112 available bytes; 98.75% used; 110403909 free inodes.

server2 `/mnt/raid5`: 254242414592 available bytes; 98.24% used; 445023557 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661154816 available bytes; 95.39% used; 114110813 free inodes.

server3 `/home`: 82661154816 available bytes; 95.39% used; 114110813 free inodes.

server3 `/data`: 123659227136 available bytes; 98.29% used; 225828157 free inodes.

server3 `/tmp`: 82661154816 available bytes; 95.39% used; 114110813 free inodes.

server3 `/var/tmp`: 82661154816 available bytes; 95.39% used; 114110813 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106046111744 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106046111744 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89330298880 available bytes; 98.77% used; 224883327 free inodes.

server4 `/tmp`: 106046111744 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106046111744 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
