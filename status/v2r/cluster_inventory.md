# V2R cluster inventory

2026-09-25T07:15:20.234766+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872637440 available bytes; 82.21% used; 112480373 free inodes.

server1 `/home`: 318872637440 available bytes; 82.21% used; 112480373 free inodes.

server1 `/tmp`: 318872637440 available bytes; 82.21% used; 112480373 free inodes.

server1 `/var/tmp`: 318872637440 available bytes; 82.21% used; 112480373 free inodes.

server1 `/mnt/raid5`: 385929060352 available bytes; 98.23% used; 337558516 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22868103168 available bytes; 98.72% used; 110410502 free inodes.

server2 `/home`: 22868103168 available bytes; 98.72% used; 110410502 free inodes.

server2 `/tmp`: 22868103168 available bytes; 98.72% used; 110410502 free inodes.

server2 `/var/tmp`: 22868103168 available bytes; 98.72% used; 110410502 free inodes.

server2 `/mnt/raid5`: 329854808064 available bytes; 97.72% used; 445097926 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84447735808 available bytes; 95.29% used; 114156017 free inodes.

server3 `/home`: 84447735808 available bytes; 95.29% used; 114156017 free inodes.

server3 `/data`: 142455668736 available bytes; 98.03% used; 225812980 free inodes.

server3 `/tmp`: 84447735808 available bytes; 95.29% used; 114156017 free inodes.

server3 `/var/tmp`: 84447735808 available bytes; 95.29% used; 114156017 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105638334464 available bytes; 94.10% used; 114350361 free inodes.

server4 `/home`: 105638334464 available bytes; 94.10% used; 114350361 free inodes.

server4 `/data`: 249485656064 available bytes; 96.55% used; 225016010 free inodes.

server4 `/tmp`: 105638334464 available bytes; 94.10% used; 114350361 free inodes.

server4 `/var/tmp`: 105638334464 available bytes; 94.10% used; 114350361 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
