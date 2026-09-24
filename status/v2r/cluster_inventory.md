# V2R cluster inventory

2026-09-24T01:01:51.819347+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325524353024 available bytes; 81.84% used; 112500255 free inodes.

server1 `/home`: 325524353024 available bytes; 81.84% used; 112500255 free inodes.

server1 `/tmp`: 325524353024 available bytes; 81.84% used; 112500255 free inodes.

server1 `/var/tmp`: 325524353024 available bytes; 81.84% used; 112500255 free inodes.

server1 `/mnt/raid5`: 1012688334848 available bytes; 95.35% used; 337734871 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40970412032 available bytes; 97.71% used; 110432205 free inodes.

server2 `/home`: 40970412032 available bytes; 97.71% used; 110432205 free inodes.

server2 `/tmp`: 40970412032 available bytes; 97.71% used; 110432205 free inodes.

server2 `/var/tmp`: 40970412032 available bytes; 97.71% used; 110432205 free inodes.

server2 `/mnt/raid5`: 531801608192 available bytes; 96.33% used; 445202464 free inodes.
| server3 | True | ['2'] | ['/tmp', '/var/tmp'] |

server3 `/`: 292735528960 available bytes; 83.66% used; 114211289 free inodes.

server3 `/home`: 292735528960 available bytes; 83.66% used; 114211289 free inodes.

server3 `/data`: 82087624704 available bytes; 98.87% used; 225843219 free inodes.

server3 `/tmp`: 292735528960 available bytes; 83.66% used; 114211289 free inodes.

server3 `/var/tmp`: 292735528960 available bytes; 83.66% used; 114211289 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106017386496 available bytes; 94.08% used; 114349497 free inodes.

server4 `/home`: 106017386496 available bytes; 94.08% used; 114349497 free inodes.

server4 `/data`: 292724137984 available bytes; 95.95% used; 225405429 free inodes.

server4 `/tmp`: 106017386496 available bytes; 94.08% used; 114349497 free inodes.

server4 `/var/tmp`: 106017386496 available bytes; 94.08% used; 114349497 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
