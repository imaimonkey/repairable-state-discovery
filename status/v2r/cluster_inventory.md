# V2R cluster inventory

2026-09-25T09:00:28.481420+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318838341632 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318838341632 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318838341632 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318838341632 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 364192505856 available bytes; 98.33% used; 337556986 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22830764032 available bytes; 98.73% used; 110410492 free inodes.

server2 `/home`: 22830764032 available bytes; 98.73% used; 110410492 free inodes.

server2 `/tmp`: 22830764032 available bytes; 98.73% used; 110410492 free inodes.

server2 `/var/tmp`: 22830764032 available bytes; 98.73% used; 110410492 free inodes.

server2 `/mnt/raid5`: 332545196032 available bytes; 97.70% used; 445093021 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436942848 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84436942848 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142374428672 available bytes; 98.03% used; 225811152 free inodes.

server3 `/tmp`: 84436942848 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84436942848 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105633071104 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105633071104 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243386413056 available bytes; 96.64% used; 224999767 free inodes.

server4 `/tmp`: 105633071104 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105633071104 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
