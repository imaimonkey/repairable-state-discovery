# V2R cluster inventory

2026-09-24T10:57:46.666639+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324378734592 available bytes; 81.90% used; 112489058 free inodes.

server1 `/home`: 324378734592 available bytes; 81.90% used; 112489058 free inodes.

server1 `/tmp`: 324378734592 available bytes; 81.90% used; 112489058 free inodes.

server1 `/var/tmp`: 324378734592 available bytes; 81.90% used; 112489058 free inodes.

server1 `/mnt/raid5`: 493993742336 available bytes; 97.73% used; 337693796 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 57700663296 available bytes; 96.78% used; 110430321 free inodes.

server2 `/home`: 57700663296 available bytes; 96.78% used; 110430321 free inodes.

server2 `/tmp`: 57700663296 available bytes; 96.78% used; 110430321 free inodes.

server2 `/var/tmp`: 57700663296 available bytes; 96.78% used; 110430321 free inodes.

server2 `/mnt/raid5`: 511949328384 available bytes; 96.46% used; 445174713 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85784219648 available bytes; 95.21% used; 114197362 free inodes.

server3 `/home`: 85784219648 available bytes; 95.21% used; 114197362 free inodes.

server3 `/data`: 164042825728 available bytes; 97.73% used; 225817664 free inodes.

server3 `/tmp`: 85784219648 available bytes; 95.21% used; 114197362 free inodes.

server3 `/var/tmp`: 85784219648 available bytes; 95.21% used; 114197362 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105734856704 available bytes; 94.10% used; 114348935 free inodes.

server4 `/home`: 105734856704 available bytes; 94.10% used; 114348935 free inodes.

server4 `/data`: 132776067072 available bytes; 98.16% used; 225258252 free inodes.

server4 `/tmp`: 105734856704 available bytes; 94.10% used; 114348935 free inodes.

server4 `/var/tmp`: 105734856704 available bytes; 94.10% used; 114348935 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
