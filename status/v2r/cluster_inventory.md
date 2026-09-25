# V2R cluster inventory

2026-09-25T21:47:58.365793+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318698258432 available bytes; 82.22% used; 112476298 free inodes.

server1 `/home`: 318698258432 available bytes; 82.22% used; 112476298 free inodes.

server1 `/tmp`: 318698258432 available bytes; 82.22% used; 112476298 free inodes.

server1 `/var/tmp`: 318698258432 available bytes; 82.22% used; 112476298 free inodes.

server1 `/mnt/raid5`: 360319549440 available bytes; 98.35% used; 337539149 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22898634752 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22898634752 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22898634752 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22898634752 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 300734222336 available bytes; 97.92% used; 445053941 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84368404480 available bytes; 95.29% used; 114152634 free inodes.

server3 `/home`: 84368404480 available bytes; 95.29% used; 114152634 free inodes.

server3 `/data`: 125886922752 available bytes; 98.26% used; 225806695 free inodes.

server3 `/tmp`: 84368404480 available bytes; 95.29% used; 114152634 free inodes.

server3 `/var/tmp`: 84368404480 available bytes; 95.29% used; 114152634 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105388494848 available bytes; 94.12% used; 114347329 free inodes.

server4 `/home`: 105388494848 available bytes; 94.12% used; 114347329 free inodes.

server4 `/data`: 215789031424 available bytes; 97.02% used; 224919244 free inodes.

server4 `/tmp`: 105388494848 available bytes; 94.12% used; 114347329 free inodes.

server4 `/var/tmp`: 105388494848 available bytes; 94.12% used; 114347329 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
