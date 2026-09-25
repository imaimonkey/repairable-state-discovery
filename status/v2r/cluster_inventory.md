# V2R cluster inventory

2026-09-25T06:51:51.629029+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318870790144 available bytes; 82.21% used; 112480368 free inodes.

server1 `/home`: 318870790144 available bytes; 82.21% used; 112480368 free inodes.

server1 `/tmp`: 318870790144 available bytes; 82.21% used; 112480368 free inodes.

server1 `/var/tmp`: 318870790144 available bytes; 82.21% used; 112480368 free inodes.

server1 `/mnt/raid5`: 399723778048 available bytes; 98.17% used; 337560520 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22876569600 available bytes; 98.72% used; 110410524 free inodes.

server2 `/home`: 22876569600 available bytes; 98.72% used; 110410524 free inodes.

server2 `/tmp`: 22876569600 available bytes; 98.72% used; 110410524 free inodes.

server2 `/var/tmp`: 22876569600 available bytes; 98.72% used; 110410524 free inodes.

server2 `/mnt/raid5`: 338108686336 available bytes; 97.66% used; 445098525 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84448190464 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84448190464 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142523916288 available bytes; 98.03% used; 225813353 free inodes.

server3 `/tmp`: 84448190464 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84448190464 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639034880 available bytes; 94.10% used; 114350365 free inodes.

server4 `/home`: 105639034880 available bytes; 94.10% used; 114350365 free inodes.

server4 `/data`: 249507213312 available bytes; 96.55% used; 225017747 free inodes.

server4 `/tmp`: 105639034880 available bytes; 94.10% used; 114350365 free inodes.

server4 `/var/tmp`: 105639034880 available bytes; 94.10% used; 114350365 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
