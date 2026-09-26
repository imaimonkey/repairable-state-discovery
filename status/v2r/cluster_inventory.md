# V2R cluster inventory

2026-09-26T04:01:09.394669+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318416670720 available bytes; 82.24% used; 112476270 free inodes.

server1 `/home`: 318416670720 available bytes; 82.24% used; 112476270 free inodes.

server1 `/tmp`: 318416670720 available bytes; 82.24% used; 112476270 free inodes.

server1 `/var/tmp`: 318416670720 available bytes; 82.24% used; 112476270 free inodes.

server1 `/mnt/raid5`: 330953482240 available bytes; 98.48% used; 337545665 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22931410944 available bytes; 98.72% used; 110406198 free inodes.

server2 `/home`: 22931410944 available bytes; 98.72% used; 110406198 free inodes.

server2 `/tmp`: 22931410944 available bytes; 98.72% used; 110406198 free inodes.

server2 `/var/tmp`: 22931410944 available bytes; 98.72% used; 110406198 free inodes.

server2 `/mnt/raid5`: 286322257920 available bytes; 98.02% used; 445051580 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84525703168 available bytes; 95.28% used; 114173537 free inodes.

server3 `/home`: 84525703168 available bytes; 95.28% used; 114173537 free inodes.

server3 `/data`: 124588953600 available bytes; 98.28% used; 225820084 free inodes.

server3 `/tmp`: 84525703168 available bytes; 95.28% used; 114173537 free inodes.

server3 `/var/tmp`: 84525703168 available bytes; 95.28% used; 114173537 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003357696 available bytes; 94.08% used; 114348225 free inodes.

server4 `/home`: 106003357696 available bytes; 94.08% used; 114348225 free inodes.

server4 `/data`: 109764079616 available bytes; 98.48% used; 224929439 free inodes.

server4 `/tmp`: 106003357696 available bytes; 94.08% used; 114348225 free inodes.

server4 `/var/tmp`: 106003357696 available bytes; 94.08% used; 114348225 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
