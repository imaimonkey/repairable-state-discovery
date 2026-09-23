# V2R cluster inventory

2026-09-23T21:35:08.186778+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325716795392 available bytes; 81.83% used; 112501430 free inodes.

server1 `/home`: 325716795392 available bytes; 81.83% used; 112501430 free inodes.

server1 `/tmp`: 325716795392 available bytes; 81.83% used; 112501430 free inodes.

server1 `/var/tmp`: 325716795392 available bytes; 81.83% used; 112501430 free inodes.

server1 `/mnt/raid5`: 1388137050112 available bytes; 93.63% used; 337739944 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41120391168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/home`: 41120391168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/tmp`: 41120391168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/var/tmp`: 41120391168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/mnt/raid5`: 538356178944 available bytes; 96.28% used; 445208684 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 293244235776 available bytes; 83.64% used; 114228767 free inodes.

server3 `/home`: 293244235776 available bytes; 83.64% used; 114228767 free inodes.

server3 `/data`: 52275163136 available bytes; 99.28% used; 225848676 free inodes.

server3 `/tmp`: 293244235776 available bytes; 83.64% used; 114228767 free inodes.

server3 `/var/tmp`: 293244235776 available bytes; 83.64% used; 114228767 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106477355008 available bytes; 94.06% used; 114355990 free inodes.

server4 `/home`: 106477355008 available bytes; 94.06% used; 114355990 free inodes.

server4 `/data`: 300283252736 available bytes; 95.85% used; 225449896 free inodes.

server4 `/tmp`: 106477355008 available bytes; 94.06% used; 114355990 free inodes.

server4 `/var/tmp`: 106477355008 available bytes; 94.06% used; 114355990 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
