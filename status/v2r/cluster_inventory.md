# V2R cluster inventory

2026-09-25T21:45:14.343669+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318702039040 available bytes; 82.22% used; 112476304 free inodes.

server1 `/home`: 318702039040 available bytes; 82.22% used; 112476304 free inodes.

server1 `/tmp`: 318702039040 available bytes; 82.22% used; 112476304 free inodes.

server1 `/var/tmp`: 318702039040 available bytes; 82.22% used; 112476304 free inodes.

server1 `/mnt/raid5`: 360330596352 available bytes; 98.35% used; 337539182 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22899453952 available bytes; 98.72% used; 110405684 free inodes.

server2 `/home`: 22899453952 available bytes; 98.72% used; 110405684 free inodes.

server2 `/tmp`: 22899453952 available bytes; 98.72% used; 110405684 free inodes.

server2 `/var/tmp`: 22899453952 available bytes; 98.72% used; 110405684 free inodes.

server2 `/mnt/raid5`: 300811476992 available bytes; 97.92% used; 445054145 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84367585280 available bytes; 95.29% used; 114152634 free inodes.

server3 `/home`: 84367585280 available bytes; 95.29% used; 114152634 free inodes.

server3 `/data`: 125889241088 available bytes; 98.26% used; 225806729 free inodes.

server3 `/tmp`: 84367585280 available bytes; 95.29% used; 114152634 free inodes.

server3 `/var/tmp`: 84367585280 available bytes; 95.29% used; 114152634 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105388552192 available bytes; 94.12% used; 114347330 free inodes.

server4 `/home`: 105388552192 available bytes; 94.12% used; 114347330 free inodes.

server4 `/data`: 215896997888 available bytes; 97.02% used; 224919372 free inodes.

server4 `/tmp`: 105388552192 available bytes; 94.12% used; 114347330 free inodes.

server4 `/var/tmp`: 105388552192 available bytes; 94.12% used; 114347330 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
