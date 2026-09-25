# V2R cluster inventory

2026-09-25T07:12:16.454761+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318873432064 available bytes; 82.21% used; 112480375 free inodes.

server1 `/home`: 318873432064 available bytes; 82.21% used; 112480375 free inodes.

server1 `/tmp`: 318873432064 available bytes; 82.21% used; 112480375 free inodes.

server1 `/var/tmp`: 318873432064 available bytes; 82.21% used; 112480375 free inodes.

server1 `/mnt/raid5`: 379057479680 available bytes; 98.26% used; 337558540 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22868987904 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22868987904 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22868987904 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22868987904 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 329943891968 available bytes; 97.72% used; 445098052 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448428032 available bytes; 95.29% used; 114156033 free inodes.

server3 `/home`: 84448428032 available bytes; 95.29% used; 114156033 free inodes.

server3 `/data`: 142456868864 available bytes; 98.03% used; 225813031 free inodes.

server3 `/tmp`: 84448428032 available bytes; 95.29% used; 114156033 free inodes.

server3 `/var/tmp`: 84448428032 available bytes; 95.29% used; 114156033 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638416384 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638416384 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249481228288 available bytes; 96.55% used; 225016304 free inodes.

server4 `/tmp`: 105638416384 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638416384 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
