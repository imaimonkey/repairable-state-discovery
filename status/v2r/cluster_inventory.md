# V2R cluster inventory

2026-09-25T14:47:43.039996+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319160041472 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319160041472 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319160041472 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319160041472 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 370971430912 available bytes; 98.30% used; 337546820 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14821634048 available bytes; 99.17% used; 110407692 free inodes.

server2 `/home`: 14821634048 available bytes; 99.17% used; 110407692 free inodes.

server2 `/tmp`: 14821634048 available bytes; 99.17% used; 110407692 free inodes.

server2 `/var/tmp`: 14821634048 available bytes; 99.17% used; 110407692 free inodes.

server2 `/mnt/raid5`: 321148477440 available bytes; 97.78% used; 445074379 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84264615936 available bytes; 95.30% used; 114154468 free inodes.

server3 `/home`: 84264615936 available bytes; 95.30% used; 114154468 free inodes.

server3 `/data`: 142194925568 available bytes; 98.03% used; 225808413 free inodes.

server3 `/tmp`: 84264615936 available bytes; 95.30% used; 114154468 free inodes.

server3 `/var/tmp`: 84264615936 available bytes; 95.30% used; 114154468 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105645481984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105645481984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231422767104 available bytes; 96.80% used; 224945630 free inodes.

server4 `/tmp`: 105645481984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105645481984 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
