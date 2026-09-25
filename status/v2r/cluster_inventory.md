# V2R cluster inventory

2026-09-25T03:27:23.602189+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318940532736 available bytes; 82.21% used; 112480371 free inodes.

server1 `/home`: 318940532736 available bytes; 82.21% used; 112480371 free inodes.

server1 `/tmp`: 318940532736 available bytes; 82.21% used; 112480371 free inodes.

server1 `/var/tmp`: 318940532736 available bytes; 82.21% used; 112480371 free inodes.

server1 `/mnt/raid5`: 416092839936 available bytes; 98.09% used; 337599248 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22980849664 available bytes; 98.72% used; 110410444 free inodes.

server2 `/home`: 22980849664 available bytes; 98.72% used; 110410444 free inodes.

server2 `/tmp`: 22980849664 available bytes; 98.72% used; 110410444 free inodes.

server2 `/var/tmp`: 22980849664 available bytes; 98.72% used; 110410444 free inodes.

server2 `/mnt/raid5`: 464993234944 available bytes; 96.79% used; 445112098 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84342382592 available bytes; 95.29% used; 114156067 free inodes.

server3 `/home`: 84342382592 available bytes; 95.29% used; 114156067 free inodes.

server3 `/data`: 144569692160 available bytes; 98.00% used; 225809941 free inodes.

server3 `/tmp`: 84342382592 available bytes; 95.29% used; 114156067 free inodes.

server3 `/var/tmp`: 84342382592 available bytes; 95.29% used; 114156067 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692368896 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105692368896 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 45412306944 available bytes; 99.37% used; 224966611 free inodes.

server4 `/tmp`: 105692368896 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105692368896 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
