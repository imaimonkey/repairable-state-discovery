# V2R cluster inventory

2026-09-25T08:44:28.561908+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318833737728 available bytes; 82.21% used; 112480385 free inodes.

server1 `/home`: 318833737728 available bytes; 82.21% used; 112480385 free inodes.

server1 `/tmp`: 318833737728 available bytes; 82.21% used; 112480385 free inodes.

server1 `/var/tmp`: 318833737728 available bytes; 82.21% used; 112480385 free inodes.

server1 `/mnt/raid5`: 364212723712 available bytes; 98.33% used; 337557053 free inodes.
| server2 | True | ['5', '6'] | [] |

server2 `/`: 22839148544 available bytes; 98.73% used; 110410486 free inodes.

server2 `/home`: 22839148544 available bytes; 98.73% used; 110410486 free inodes.

server2 `/tmp`: 22839148544 available bytes; 98.73% used; 110410486 free inodes.

server2 `/var/tmp`: 22839148544 available bytes; 98.73% used; 110410486 free inodes.

server2 `/mnt/raid5`: 332791844864 available bytes; 97.70% used; 445093545 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84435202048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84435202048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142379171840 available bytes; 98.03% used; 225811436 free inodes.

server3 `/tmp`: 84435202048 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84435202048 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105633574912 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633574912 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 245019836416 available bytes; 96.61% used; 225002151 free inodes.

server4 `/tmp`: 105633574912 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633574912 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
