# V2R cluster inventory

2026-09-24T23:48:39.814262+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319017676800 available bytes; 82.20% used; 112480777 free inodes.

server1 `/home`: 319017676800 available bytes; 82.20% used; 112480777 free inodes.

server1 `/tmp`: 319017676800 available bytes; 82.20% used; 112480777 free inodes.

server1 `/var/tmp`: 319017676800 available bytes; 82.20% used; 112480777 free inodes.

server1 `/mnt/raid5`: 415186100224 available bytes; 98.10% used; 337611044 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23101931520 available bytes; 98.71% used; 110410794 free inodes.

server2 `/home`: 23101931520 available bytes; 98.71% used; 110410794 free inodes.

server2 `/tmp`: 23101931520 available bytes; 98.71% used; 110410794 free inodes.

server2 `/var/tmp`: 23101931520 available bytes; 98.71% used; 110410794 free inodes.

server2 `/mnt/raid5`: 485896626176 available bytes; 96.64% used; 445150658 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84365164544 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84365164544 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147890630656 available bytes; 97.96% used; 225800540 free inodes.

server3 `/tmp`: 84365164544 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84365164544 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799061504 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105799061504 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60943048704 available bytes; 99.16% used; 225120289 free inodes.

server4 `/tmp`: 105799061504 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105799061504 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
