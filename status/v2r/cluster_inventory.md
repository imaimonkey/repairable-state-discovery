# V2R cluster inventory

2026-09-25T02:43:44.905982+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318958292992 available bytes; 82.21% used; 112480424 free inodes.

server1 `/home`: 318958292992 available bytes; 82.21% used; 112480424 free inodes.

server1 `/tmp`: 318958292992 available bytes; 82.21% used; 112480424 free inodes.

server1 `/var/tmp`: 318958292992 available bytes; 82.21% used; 112480424 free inodes.

server1 `/mnt/raid5`: 416186523648 available bytes; 98.09% used; 337604347 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23006363648 available bytes; 98.72% used; 110410439 free inodes.

server2 `/home`: 23006363648 available bytes; 98.72% used; 110410439 free inodes.

server2 `/tmp`: 23006363648 available bytes; 98.72% used; 110410439 free inodes.

server2 `/var/tmp`: 23006363648 available bytes; 98.72% used; 110410439 free inodes.

server2 `/mnt/raid5`: 482696843264 available bytes; 96.66% used; 445113185 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84350480384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84350480384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145367482368 available bytes; 97.99% used; 225810995 free inodes.

server3 `/tmp`: 84350480384 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84350480384 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 104025485312 available bytes; 94.19% used; 114350984 free inodes.

server4 `/home`: 104025460736 available bytes; 94.19% used; 114350984 free inodes.

server4 `/data`: 1308999680 available bytes; 99.98% used; 224968797 free inodes.

server4 `/tmp`: 104025436160 available bytes; 94.19% used; 114350984 free inodes.

server4 `/var/tmp`: 104025423872 available bytes; 94.19% used; 114350984 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
