# V2R cluster inventory

2026-09-25T14:46:11.383375+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319160246272 available bytes; 82.20% used; 112476980 free inodes.

server1 `/home`: 319160246272 available bytes; 82.20% used; 112476980 free inodes.

server1 `/tmp`: 319160246272 available bytes; 82.20% used; 112476980 free inodes.

server1 `/var/tmp`: 319160246272 available bytes; 82.20% used; 112476980 free inodes.

server1 `/mnt/raid5`: 364426981376 available bytes; 98.33% used; 337546780 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 12784459776 available bytes; 99.29% used; 110407587 free inodes.

server2 `/home`: 12784459776 available bytes; 99.29% used; 110407587 free inodes.

server2 `/tmp`: 12784459776 available bytes; 99.29% used; 110407587 free inodes.

server2 `/var/tmp`: 12784459776 available bytes; 99.29% used; 110407587 free inodes.

server2 `/mnt/raid5`: 321198116864 available bytes; 97.78% used; 445074451 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84264984576 available bytes; 95.30% used; 114154470 free inodes.

server3 `/home`: 84264984576 available bytes; 95.30% used; 114154470 free inodes.

server3 `/data`: 142196469760 available bytes; 98.03% used; 225808444 free inodes.

server3 `/tmp`: 84264984576 available bytes; 95.30% used; 114154470 free inodes.

server3 `/var/tmp`: 84264984576 available bytes; 95.30% used; 114154470 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105645522944 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105645522944 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231423864832 available bytes; 96.80% used; 224945701 free inodes.

server4 `/tmp`: 105645522944 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105645522944 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
