# V2R cluster inventory

2026-09-25T21:58:39.503284+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318695313408 available bytes; 82.22% used; 112476292 free inodes.

server1 `/home`: 318695313408 available bytes; 82.22% used; 112476292 free inodes.

server1 `/tmp`: 318695313408 available bytes; 82.22% used; 112476292 free inodes.

server1 `/var/tmp`: 318695313408 available bytes; 82.22% used; 112476292 free inodes.

server1 `/mnt/raid5`: 360305590272 available bytes; 98.35% used; 337539086 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22904979456 available bytes; 98.72% used; 110405686 free inodes.

server2 `/home`: 22904979456 available bytes; 98.72% used; 110405686 free inodes.

server2 `/tmp`: 22904979456 available bytes; 98.72% used; 110405686 free inodes.

server2 `/var/tmp`: 22904979456 available bytes; 98.72% used; 110405686 free inodes.

server2 `/mnt/raid5`: 300307374080 available bytes; 97.92% used; 445053609 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84366184448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84366184448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 125883310080 available bytes; 98.26% used; 225806525 free inodes.

server3 `/tmp`: 84366184448 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84366184448 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105320984576 available bytes; 94.12% used; 114347146 free inodes.

server4 `/home`: 105320984576 available bytes; 94.12% used; 114347146 free inodes.

server4 `/data`: 208821284864 available bytes; 97.11% used; 224919165 free inodes.

server4 `/tmp`: 105320984576 available bytes; 94.12% used; 114347146 free inodes.

server4 `/var/tmp`: 105320984576 available bytes; 94.12% used; 114347146 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
