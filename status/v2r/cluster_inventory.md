# V2R cluster inventory

2026-09-25T03:25:17.438669+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318941462528 available bytes; 82.21% used; 112480367 free inodes.

server1 `/home`: 318941462528 available bytes; 82.21% used; 112480367 free inodes.

server1 `/tmp`: 318941462528 available bytes; 82.21% used; 112480367 free inodes.

server1 `/var/tmp`: 318941462528 available bytes; 82.21% used; 112480367 free inodes.

server1 `/mnt/raid5`: 416099946496 available bytes; 98.09% used; 337599494 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22982791168 available bytes; 98.72% used; 110410452 free inodes.

server2 `/home`: 22982791168 available bytes; 98.72% used; 110410452 free inodes.

server2 `/tmp`: 22982791168 available bytes; 98.72% used; 110410452 free inodes.

server2 `/var/tmp`: 22982791168 available bytes; 98.72% used; 110410452 free inodes.

server2 `/mnt/raid5`: 465072529408 available bytes; 96.79% used; 445112300 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84346015744 available bytes; 95.29% used; 114156075 free inodes.

server3 `/home`: 84346015744 available bytes; 95.29% used; 114156075 free inodes.

server3 `/data`: 144601362432 available bytes; 98.00% used; 225809982 free inodes.

server3 `/tmp`: 84346015744 available bytes; 95.29% used; 114156075 free inodes.

server3 `/var/tmp`: 84346015744 available bytes; 95.29% used; 114156075 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105692430336 available bytes; 94.10% used; 114350898 free inodes.

server4 `/home`: 105692430336 available bytes; 94.10% used; 114350898 free inodes.

server4 `/data`: 45413400576 available bytes; 99.37% used; 224966721 free inodes.

server4 `/tmp`: 105692430336 available bytes; 94.10% used; 114350898 free inodes.

server4 `/var/tmp`: 105692430336 available bytes; 94.10% used; 114350898 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
