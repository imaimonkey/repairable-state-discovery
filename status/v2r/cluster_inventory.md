# V2R cluster inventory

2026-09-25T08:00:43.033223+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318859681792 available bytes; 82.21% used; 112480369 free inodes.

server1 `/home`: 318859681792 available bytes; 82.21% used; 112480369 free inodes.

server1 `/tmp`: 318859681792 available bytes; 82.21% used; 112480369 free inodes.

server1 `/var/tmp`: 318859681792 available bytes; 82.21% used; 112480369 free inodes.

server1 `/mnt/raid5`: 386617049088 available bytes; 98.23% used; 337557921 free inodes.
| server2 | True | ['0'] | [] | reference_compatible=False |

server2 `/`: 22845034496 available bytes; 98.73% used; 110410483 free inodes.

server2 `/home`: 22845034496 available bytes; 98.73% used; 110410483 free inodes.

server2 `/tmp`: 22845034496 available bytes; 98.73% used; 110410483 free inodes.

server2 `/var/tmp`: 22845034496 available bytes; 98.73% used; 110410483 free inodes.

server2 `/mnt/raid5`: 334173757440 available bytes; 97.69% used; 445095280 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84437458944 available bytes; 95.29% used; 114156047 free inodes.

server3 `/home`: 84437458944 available bytes; 95.29% used; 114156047 free inodes.

server3 `/data`: 142388424704 available bytes; 98.03% used; 225812188 free inodes.

server3 `/tmp`: 84437458944 available bytes; 95.29% used; 114156047 free inodes.

server3 `/var/tmp`: 84437458944 available bytes; 95.29% used; 114156047 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625534464 available bytes; 94.11% used; 114350336 free inodes.

server4 `/home`: 105625534464 available bytes; 94.11% used; 114350336 free inodes.

server4 `/data`: 249041612800 available bytes; 96.56% used; 225009751 free inodes.

server4 `/tmp`: 105625534464 available bytes; 94.11% used; 114350336 free inodes.

server4 `/var/tmp`: 105625534464 available bytes; 94.11% used; 114350336 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
