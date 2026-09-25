# V2R cluster inventory

2026-09-25T09:06:35.815708+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318837080064 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318837080064 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318837080064 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318837080064 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 354709266432 available bytes; 98.37% used; 337556971 free inodes.
| server2 | True | ['5', '6'] | [] | reference_compatible=False |

server2 `/`: 22840905728 available bytes; 98.73% used; 110410494 free inodes.

server2 `/home`: 22840905728 available bytes; 98.73% used; 110410494 free inodes.

server2 `/tmp`: 22840905728 available bytes; 98.73% used; 110410494 free inodes.

server2 `/var/tmp`: 22840905728 available bytes; 98.73% used; 110410494 free inodes.

server2 `/mnt/raid5`: 332373389312 available bytes; 97.70% used; 445092913 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436111360 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84436111360 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142374727680 available bytes; 98.03% used; 225811062 free inodes.

server3 `/tmp`: 84436111360 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84436111360 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105632878592 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105632878592 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 243372666880 available bytes; 96.64% used; 224998787 free inodes.

server4 `/tmp`: 105632878592 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105632878592 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
