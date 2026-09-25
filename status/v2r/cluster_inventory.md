# V2R cluster inventory

2026-09-25T12:45:21.592006+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319124606976 available bytes; 82.20% used; 112477600 free inodes.

server1 `/home`: 319124606976 available bytes; 82.20% used; 112477600 free inodes.

server1 `/tmp`: 319124606976 available bytes; 82.20% used; 112477600 free inodes.

server1 `/var/tmp`: 319124606976 available bytes; 82.20% used; 112477600 free inodes.

server1 `/mnt/raid5`: 364249735168 available bytes; 98.33% used; 337548044 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 20256120832 available bytes; 98.87% used; 110409427 free inodes.

server2 `/home`: 20256120832 available bytes; 98.87% used; 110409427 free inodes.

server2 `/tmp`: 20256120832 available bytes; 98.87% used; 110409427 free inodes.

server2 `/var/tmp`: 20256120832 available bytes; 98.87% used; 110409427 free inodes.

server2 `/mnt/raid5`: 324156485632 available bytes; 97.76% used; 445079148 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84208267264 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84208267264 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142275772416 available bytes; 98.03% used; 225810966 free inodes.

server3 `/tmp`: 84208267264 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84208267264 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105665622016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105665622016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 232025612288 available bytes; 96.79% used; 224962042 free inodes.

server4 `/tmp`: 105665622016 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105665622016 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
