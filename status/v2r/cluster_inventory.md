# V2R cluster inventory

2026-09-24T02:55:40.775143+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325380128768 available bytes; 81.85% used; 112498642 free inodes.

server1 `/home`: 325380128768 available bytes; 81.85% used; 112498642 free inodes.

server1 `/tmp`: 325380128768 available bytes; 81.85% used; 112498642 free inodes.

server1 `/var/tmp`: 325380128768 available bytes; 81.85% used; 112498642 free inodes.

server1 `/mnt/raid5`: 538399191040 available bytes; 97.53% used; 337732328 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40865374208 available bytes; 97.72% used; 110431356 free inodes.

server2 `/home`: 40865374208 available bytes; 97.72% used; 110431356 free inodes.

server2 `/tmp`: 40865374208 available bytes; 97.72% used; 110431356 free inodes.

server2 `/var/tmp`: 40865374208 available bytes; 97.72% used; 110431356 free inodes.

server2 `/mnt/raid5`: 528228061184 available bytes; 96.35% used; 445198846 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292287590400 available bytes; 83.69% used; 114186960 free inodes.

server3 `/home`: 292287590400 available bytes; 83.69% used; 114186960 free inodes.

server3 `/data`: 39714709504 available bytes; 99.45% used; 225845447 free inodes.

server3 `/tmp`: 292287590400 available bytes; 83.69% used; 114186960 free inodes.

server3 `/var/tmp`: 292287590400 available bytes; 83.69% used; 114186960 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106002485248 available bytes; 94.08% used; 114349810 free inodes.

server4 `/home`: 106002485248 available bytes; 94.08% used; 114349810 free inodes.

server4 `/data`: 289716842496 available bytes; 96.00% used; 225386882 free inodes.

server4 `/tmp`: 106002485248 available bytes; 94.08% used; 114349810 free inodes.

server4 `/var/tmp`: 106002485248 available bytes; 94.08% used; 114349810 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
