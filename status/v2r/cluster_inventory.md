# V2R cluster inventory

2026-09-24T23:51:26.417647+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319016325120 available bytes; 82.20% used; 112480779 free inodes.

server1 `/home`: 319016325120 available bytes; 82.20% used; 112480779 free inodes.

server1 `/tmp`: 319016325120 available bytes; 82.20% used; 112480779 free inodes.

server1 `/var/tmp`: 319016325120 available bytes; 82.20% used; 112480779 free inodes.

server1 `/mnt/raid5`: 415177867264 available bytes; 98.10% used; 337610723 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23100375040 available bytes; 98.71% used; 110410799 free inodes.

server2 `/home`: 23100375040 available bytes; 98.71% used; 110410799 free inodes.

server2 `/tmp`: 23100375040 available bytes; 98.71% used; 110410799 free inodes.

server2 `/var/tmp`: 23100375040 available bytes; 98.71% used; 110410799 free inodes.

server2 `/mnt/raid5`: 485813620736 available bytes; 96.64% used; 445150644 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84363882496 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84363882496 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 147839447040 available bytes; 97.96% used; 225800500 free inodes.

server3 `/tmp`: 84363882496 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84363882496 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105798983680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/home`: 105798983680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/data`: 60900843520 available bytes; 99.16% used; 225115971 free inodes.

server4 `/tmp`: 105798983680 available bytes; 94.10% used; 114348296 free inodes.

server4 `/var/tmp`: 105798983680 available bytes; 94.10% used; 114348296 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
