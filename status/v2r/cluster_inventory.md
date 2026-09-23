# V2R cluster inventory

2026-09-23T23:56:54.369475+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325582348288 available bytes; 81.84% used; 112500948 free inodes.

server1 `/home`: 325582348288 available bytes; 81.84% used; 112500948 free inodes.

server1 `/tmp`: 325582348288 available bytes; 81.84% used; 112500948 free inodes.

server1 `/var/tmp`: 325582348288 available bytes; 81.84% used; 112500948 free inodes.

server1 `/mnt/raid5`: 1280343097344 available bytes; 94.13% used; 337735428 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41020948480 available bytes; 97.71% used; 110432461 free inodes.

server2 `/home`: 41020948480 available bytes; 97.71% used; 110432461 free inodes.

server2 `/tmp`: 41020948480 available bytes; 97.71% used; 110432461 free inodes.

server2 `/var/tmp`: 41020948480 available bytes; 97.71% used; 110432461 free inodes.

server2 `/mnt/raid5`: 533633265664 available bytes; 96.31% used; 445204295 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292780810240 available bytes; 83.66% used; 114205926 free inodes.

server3 `/home`: 292780810240 available bytes; 83.66% used; 114205926 free inodes.

server3 `/data`: 82273964032 available bytes; 98.86% used; 225844893 free inodes.

server3 `/tmp`: 292780810240 available bytes; 83.66% used; 114205926 free inodes.

server3 `/var/tmp`: 292780810240 available bytes; 83.66% used; 114205926 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106145775616 available bytes; 94.08% used; 114351387 free inodes.

server4 `/home`: 106145775616 available bytes; 94.08% used; 114351387 free inodes.

server4 `/data`: 292944293888 available bytes; 95.95% used; 225416009 free inodes.

server4 `/tmp`: 106145775616 available bytes; 94.08% used; 114351387 free inodes.

server4 `/var/tmp`: 106145775616 available bytes; 94.08% used; 114351387 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
