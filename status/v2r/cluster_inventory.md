# V2R cluster inventory

2026-09-26T01:35:57.283362+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318650019840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/home`: 318650019840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/tmp`: 318650019840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/var/tmp`: 318650019840 available bytes; 82.22% used; 112476299 free inodes.

server1 `/mnt/raid5`: 345488900096 available bytes; 98.42% used; 337546512 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22941204480 available bytes; 98.72% used; 110406220 free inodes.

server2 `/home`: 22941204480 available bytes; 98.72% used; 110406220 free inodes.

server2 `/tmp`: 22941204480 available bytes; 98.72% used; 110406220 free inodes.

server2 `/var/tmp`: 22941204480 available bytes; 98.72% used; 110406220 free inodes.

server2 `/mnt/raid5`: 290541715456 available bytes; 97.99% used; 445055807 free inodes.
| server3 | True | ['3'] | [] |

server3 `/`: 84335656960 available bytes; 95.29% used; 114152376 free inodes.

server3 `/home`: 84335656960 available bytes; 95.29% used; 114152376 free inodes.

server3 `/data`: 124798898176 available bytes; 98.28% used; 225817902 free inodes.

server3 `/tmp`: 84335656960 available bytes; 95.29% used; 114152376 free inodes.

server3 `/var/tmp`: 84335656960 available bytes; 95.29% used; 114152376 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105196810240 available bytes; 94.13% used; 114346905 free inodes.

server4 `/home`: 105196810240 available bytes; 94.13% used; 114346905 free inodes.

server4 `/data`: 133763031040 available bytes; 98.15% used; 224916652 free inodes.

server4 `/tmp`: 105196810240 available bytes; 94.13% used; 114346905 free inodes.

server4 `/var/tmp`: 105196810240 available bytes; 94.13% used; 114346905 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
