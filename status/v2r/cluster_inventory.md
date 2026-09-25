# V2R cluster inventory

2026-09-25T05:45:28.485704+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318879653888 available bytes; 82.21% used; 112480341 free inodes.

server1 `/home`: 318879653888 available bytes; 82.21% used; 112480341 free inodes.

server1 `/tmp`: 318879653888 available bytes; 82.21% used; 112480341 free inodes.

server1 `/var/tmp`: 318879653888 available bytes; 82.21% used; 112480341 free inodes.

server1 `/mnt/raid5`: 408454799360 available bytes; 98.13% used; 337566440 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22914035712 available bytes; 98.72% used; 110410470 free inodes.

server2 `/home`: 22914035712 available bytes; 98.72% used; 110410470 free inodes.

server2 `/tmp`: 22914035712 available bytes; 98.72% used; 110410470 free inodes.

server2 `/var/tmp`: 22914035712 available bytes; 98.72% used; 110410470 free inodes.

server2 `/mnt/raid5`: 420353114112 available bytes; 97.10% used; 445102197 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84313157632 available bytes; 95.30% used; 114156041 free inodes.

server3 `/home`: 84313157632 available bytes; 95.30% used; 114156041 free inodes.

server3 `/data`: 142778748928 available bytes; 98.03% used; 225814579 free inodes.

server3 `/tmp`: 84313157632 available bytes; 95.30% used; 114156041 free inodes.

server3 `/var/tmp`: 84313157632 available bytes; 95.30% used; 114156041 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649553408 available bytes; 94.10% used; 114350388 free inodes.

server4 `/home`: 105649553408 available bytes; 94.10% used; 114350388 free inodes.

server4 `/data`: 24757694464 available bytes; 99.66% used; 224965594 free inodes.

server4 `/tmp`: 105649553408 available bytes; 94.10% used; 114350388 free inodes.

server4 `/var/tmp`: 105649553408 available bytes; 94.10% used; 114350388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
