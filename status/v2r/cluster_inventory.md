# V2R cluster inventory

2026-09-25T21:42:11.010925+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318698491904 available bytes; 82.22% used; 112476298 free inodes.

server1 `/home`: 318698491904 available bytes; 82.22% used; 112476298 free inodes.

server1 `/tmp`: 318698491904 available bytes; 82.22% used; 112476298 free inodes.

server1 `/var/tmp`: 318698491904 available bytes; 82.22% used; 112476298 free inodes.

server1 `/mnt/raid5`: 360334725120 available bytes; 98.35% used; 337539185 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22899822592 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22899822592 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22899822592 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22899822592 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 300900753408 available bytes; 97.92% used; 445054256 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367134720 available bytes; 95.29% used; 114152628 free inodes.

server3 `/home`: 84367134720 available bytes; 95.29% used; 114152628 free inodes.

server3 `/data`: 125890965504 available bytes; 98.26% used; 225806783 free inodes.

server3 `/tmp`: 84367134720 available bytes; 95.29% used; 114152628 free inodes.

server3 `/var/tmp`: 84367134720 available bytes; 95.29% used; 114152628 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388642304 available bytes; 94.12% used; 114347330 free inodes.

server4 `/home`: 105388642304 available bytes; 94.12% used; 114347330 free inodes.

server4 `/data`: 216671268864 available bytes; 97.01% used; 224919828 free inodes.

server4 `/tmp`: 105388642304 available bytes; 94.12% used; 114347330 free inodes.

server4 `/var/tmp`: 105388642304 available bytes; 94.12% used; 114347330 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
