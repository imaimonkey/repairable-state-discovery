# V2R cluster inventory

2026-09-25T03:22:41.687441+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318939705344 available bytes; 82.21% used; 112480365 free inodes.

server1 `/home`: 318939705344 available bytes; 82.21% used; 112480365 free inodes.

server1 `/tmp`: 318939705344 available bytes; 82.21% used; 112480365 free inodes.

server1 `/var/tmp`: 318939705344 available bytes; 82.21% used; 112480365 free inodes.

server1 `/mnt/raid5`: 416102174720 available bytes; 98.09% used; 337599793 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22987587584 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22987587584 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22987587584 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22987587584 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 464599621632 available bytes; 96.79% used; 445111998 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84343525376 available bytes; 95.29% used; 114156077 free inodes.

server3 `/home`: 84343525376 available bytes; 95.29% used; 114156077 free inodes.

server3 `/data`: 144649568256 available bytes; 98.00% used; 225810022 free inodes.

server3 `/tmp`: 84343525376 available bytes; 95.29% used; 114156077 free inodes.

server3 `/var/tmp`: 84343525376 available bytes; 95.29% used; 114156077 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105692512256 available bytes; 94.10% used; 114350897 free inodes.

server4 `/home`: 105692512256 available bytes; 94.10% used; 114350897 free inodes.

server4 `/data`: 45417177088 available bytes; 99.37% used; 224966812 free inodes.

server4 `/tmp`: 105692512256 available bytes; 94.10% used; 114350897 free inodes.

server4 `/var/tmp`: 105692512256 available bytes; 94.10% used; 114350897 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
