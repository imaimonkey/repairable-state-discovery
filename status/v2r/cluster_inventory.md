# V2R cluster inventory

2026-09-25T03:24:13.879759+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318940905472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318940905472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318940905472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318940905472 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 416102031360 available bytes; 98.09% used; 337599618 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22983147520 available bytes; 98.72% used; 110410454 free inodes.

server2 `/home`: 22983147520 available bytes; 98.72% used; 110410454 free inodes.

server2 `/tmp`: 22983147520 available bytes; 98.72% used; 110410454 free inodes.

server2 `/var/tmp`: 22983147520 available bytes; 98.72% used; 110410454 free inodes.

server2 `/mnt/raid5`: 465081458688 available bytes; 96.79% used; 445111895 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84346568704 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84346568704 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 144623022080 available bytes; 98.00% used; 225810002 free inodes.

server3 `/tmp`: 84346568704 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84346568704 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692471296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692471296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45414608896 available bytes; 99.37% used; 224966752 free inodes.

server4 `/tmp`: 105692471296 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692471296 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
