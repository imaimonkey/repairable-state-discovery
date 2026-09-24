# V2R cluster inventory

2026-09-24T11:38:35.122335+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324345520128 available bytes; 81.91% used; 112488836 free inodes.

server1 `/home`: 324345520128 available bytes; 81.91% used; 112488836 free inodes.

server1 `/tmp`: 324345520128 available bytes; 81.91% used; 112488836 free inodes.

server1 `/var/tmp`: 324345520128 available bytes; 81.91% used; 112488836 free inodes.

server1 `/mnt/raid5`: 414386737152 available bytes; 98.10% used; 337688431 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57657917440 available bytes; 96.78% used; 110429920 free inodes.

server2 `/home`: 57657917440 available bytes; 96.78% used; 110429920 free inodes.

server2 `/tmp`: 57657917440 available bytes; 96.78% used; 110429920 free inodes.

server2 `/var/tmp`: 57657917440 available bytes; 96.78% used; 110429920 free inodes.

server2 `/mnt/raid5`: 510376411136 available bytes; 96.47% used; 445173097 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84982575104 available bytes; 95.26% used; 114157067 free inodes.

server3 `/home`: 84982575104 available bytes; 95.26% used; 114157067 free inodes.

server3 `/data`: 163740979200 available bytes; 97.74% used; 225816469 free inodes.

server3 `/tmp`: 84982575104 available bytes; 95.26% used; 114157067 free inodes.

server3 `/var/tmp`: 84982575104 available bytes; 95.26% used; 114157067 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730551808 available bytes; 94.10% used; 114348868 free inodes.

server4 `/home`: 105730551808 available bytes; 94.10% used; 114348868 free inodes.

server4 `/data`: 115438026752 available bytes; 98.40% used; 225258009 free inodes.

server4 `/tmp`: 105730551808 available bytes; 94.10% used; 114348868 free inodes.

server4 `/var/tmp`: 105730551808 available bytes; 94.10% used; 114348868 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
