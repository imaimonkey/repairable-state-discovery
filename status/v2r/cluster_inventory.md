# V2R cluster inventory

2026-09-24T00:44:51.486710+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 325539270656 available bytes; 81.84% used; 112500441 free inodes.

server1 `/home`: 325539270656 available bytes; 81.84% used; 112500441 free inodes.

server1 `/tmp`: 325539270656 available bytes; 81.84% used; 112500441 free inodes.

server1 `/var/tmp`: 325539270656 available bytes; 81.84% used; 112500441 free inodes.

server1 `/mnt/raid5`: 1082400247808 available bytes; 95.03% used; 337734996 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40982462464 available bytes; 97.71% used; 110432284 free inodes.

server2 `/home`: 40982462464 available bytes; 97.71% used; 110432284 free inodes.

server2 `/tmp`: 40982462464 available bytes; 97.71% used; 110432284 free inodes.

server2 `/var/tmp`: 40982462464 available bytes; 97.71% used; 110432284 free inodes.

server2 `/mnt/raid5`: 532316299264 available bytes; 96.32% used; 445202689 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292342812672 available bytes; 83.69% used; 114188827 free inodes.

server3 `/home`: 292342812672 available bytes; 83.69% used; 114188827 free inodes.

server3 `/data`: 82218598400 available bytes; 98.86% used; 225843595 free inodes.

server3 `/tmp`: 292342812672 available bytes; 83.69% used; 114188827 free inodes.

server3 `/var/tmp`: 292342812672 available bytes; 83.69% used; 114188827 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106055012352 available bytes; 94.08% used; 114349958 free inodes.

server4 `/home`: 106055012352 available bytes; 94.08% used; 114349958 free inodes.

server4 `/data`: 292915183616 available bytes; 95.95% used; 225414576 free inodes.

server4 `/tmp`: 106055012352 available bytes; 94.08% used; 114349958 free inodes.

server4 `/var/tmp`: 106055012352 available bytes; 94.08% used; 114349958 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
