# V2R cluster inventory

2026-09-25T06:50:49.966063+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870945792 available bytes; 82.21% used; 112480368 free inodes.

server1 `/home`: 318870945792 available bytes; 82.21% used; 112480368 free inodes.

server1 `/tmp`: 318870945792 available bytes; 82.21% used; 112480368 free inodes.

server1 `/var/tmp`: 318870945792 available bytes; 82.21% used; 112480368 free inodes.

server1 `/mnt/raid5`: 399726673920 available bytes; 98.17% used; 337560529 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22876835840 available bytes; 98.72% used; 110410524 free inodes.

server2 `/home`: 22876835840 available bytes; 98.72% used; 110410524 free inodes.

server2 `/tmp`: 22876835840 available bytes; 98.72% used; 110410524 free inodes.

server2 `/var/tmp`: 22876835840 available bytes; 98.72% used; 110410524 free inodes.

server2 `/mnt/raid5`: 338138193920 available bytes; 97.66% used; 445098574 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84448206848 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84448206848 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142523994112 available bytes; 98.03% used; 225813395 free inodes.

server3 `/tmp`: 84448206848 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84448206848 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639063552 available bytes; 94.10% used; 114350364 free inodes.

server4 `/home`: 105639063552 available bytes; 94.10% used; 114350364 free inodes.

server4 `/data`: 249508622336 available bytes; 96.55% used; 225017853 free inodes.

server4 `/tmp`: 105639063552 available bytes; 94.10% used; 114350364 free inodes.

server4 `/var/tmp`: 105639063552 available bytes; 94.10% used; 114350364 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
