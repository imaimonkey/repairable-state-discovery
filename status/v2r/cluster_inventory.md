# V2R cluster inventory

2026-09-25T06:52:21.777588+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870331392 available bytes; 82.21% used; 112480366 free inodes.

server1 `/home`: 318870331392 available bytes; 82.21% used; 112480366 free inodes.

server1 `/tmp`: 318870331392 available bytes; 82.21% used; 112480366 free inodes.

server1 `/var/tmp`: 318870331392 available bytes; 82.21% used; 112480366 free inodes.

server1 `/mnt/raid5`: 399722872832 available bytes; 98.17% used; 337560517 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22876311552 available bytes; 98.72% used; 110410524 free inodes.

server2 `/home`: 22876311552 available bytes; 98.72% used; 110410524 free inodes.

server2 `/tmp`: 22876311552 available bytes; 98.72% used; 110410524 free inodes.

server2 `/var/tmp`: 22876311552 available bytes; 98.72% used; 110410524 free inodes.

server2 `/mnt/raid5`: 338088312832 available bytes; 97.66% used; 445098451 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448186368 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84448186368 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142523592704 available bytes; 98.03% used; 225813335 free inodes.

server3 `/tmp`: 84448186368 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84448186368 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639006208 available bytes; 94.10% used; 114350364 free inodes.

server4 `/home`: 105639006208 available bytes; 94.10% used; 114350364 free inodes.

server4 `/data`: 249506566144 available bytes; 96.55% used; 225017682 free inodes.

server4 `/tmp`: 105639006208 available bytes; 94.10% used; 114350364 free inodes.

server4 `/var/tmp`: 105639006208 available bytes; 94.10% used; 114350364 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
