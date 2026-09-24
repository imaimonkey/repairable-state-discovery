# V2R cluster inventory

2026-09-24T00:58:46.342268+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325525807104 available bytes; 81.84% used; 112500284 free inodes.

server1 `/home`: 325525807104 available bytes; 81.84% used; 112500284 free inodes.

server1 `/tmp`: 325525807104 available bytes; 81.84% used; 112500284 free inodes.

server1 `/var/tmp`: 325525807104 available bytes; 81.84% used; 112500284 free inodes.

server1 `/mnt/raid5`: 1025336254464 available bytes; 95.30% used; 337734804 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40972009472 available bytes; 97.71% used; 110432220 free inodes.

server2 `/home`: 40972009472 available bytes; 97.71% used; 110432220 free inodes.

server2 `/tmp`: 40972009472 available bytes; 97.71% used; 110432220 free inodes.

server2 `/var/tmp`: 40972009472 available bytes; 97.71% used; 110432220 free inodes.

server2 `/mnt/raid5`: 531899625472 available bytes; 96.32% used; 445202319 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292746461184 available bytes; 83.66% used; 114212041 free inodes.

server3 `/home`: 292746461184 available bytes; 83.66% used; 114212041 free inodes.

server3 `/data`: 82156814336 available bytes; 98.86% used; 225843274 free inodes.

server3 `/tmp`: 292746461184 available bytes; 83.66% used; 114212041 free inodes.

server3 `/var/tmp`: 292746461184 available bytes; 83.66% used; 114212041 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106022801408 available bytes; 94.08% used; 114349581 free inodes.

server4 `/home`: 106022801408 available bytes; 94.08% used; 114349581 free inodes.

server4 `/data`: 292874571776 available bytes; 95.95% used; 225414557 free inodes.

server4 `/tmp`: 106022801408 available bytes; 94.08% used; 114349581 free inodes.

server4 `/var/tmp`: 106022801408 available bytes; 94.08% used; 114349581 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
