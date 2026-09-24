# V2R cluster inventory

2026-09-24T02:57:14.247497+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325378744320 available bytes; 81.85% used; 112498626 free inodes.

server1 `/home`: 325378744320 available bytes; 81.85% used; 112498626 free inodes.

server1 `/tmp`: 325378744320 available bytes; 81.85% used; 112498626 free inodes.

server1 `/var/tmp`: 325378744320 available bytes; 81.85% used; 112498626 free inodes.

server1 `/mnt/raid5`: 531732004864 available bytes; 97.56% used; 337732323 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40864256000 available bytes; 97.72% used; 110431344 free inodes.

server2 `/home`: 40864256000 available bytes; 97.72% used; 110431344 free inodes.

server2 `/tmp`: 40864256000 available bytes; 97.72% used; 110431344 free inodes.

server2 `/var/tmp`: 40864256000 available bytes; 97.72% used; 110431344 free inodes.

server2 `/mnt/raid5`: 528170430464 available bytes; 96.35% used; 445198788 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292287311872 available bytes; 83.69% used; 114186960 free inodes.

server3 `/home`: 292287311872 available bytes; 83.69% used; 114186960 free inodes.

server3 `/data`: 39709974528 available bytes; 99.45% used; 225845396 free inodes.

server3 `/tmp`: 292287311872 available bytes; 83.69% used; 114186960 free inodes.

server3 `/var/tmp`: 292287311872 available bytes; 83.69% used; 114186960 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105996959744 available bytes; 94.08% used; 114349633 free inodes.

server4 `/home`: 105996959744 available bytes; 94.08% used; 114349633 free inodes.

server4 `/data`: 289717104640 available bytes; 96.00% used; 225386880 free inodes.

server4 `/tmp`: 105996959744 available bytes; 94.08% used; 114349633 free inodes.

server4 `/var/tmp`: 105996959744 available bytes; 94.08% used; 114349633 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
