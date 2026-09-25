# V2R cluster inventory

2026-09-25T06:47:44.857936+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318872014848 available bytes; 82.21% used; 112480377 free inodes.

server1 `/home`: 318872014848 available bytes; 82.21% used; 112480377 free inodes.

server1 `/tmp`: 318872014848 available bytes; 82.21% used; 112480377 free inodes.

server1 `/var/tmp`: 318872014848 available bytes; 82.21% used; 112480377 free inodes.

server1 `/mnt/raid5`: 399780548608 available bytes; 98.17% used; 337561340 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22878142464 available bytes; 98.72% used; 110410526 free inodes.

server2 `/home`: 22878142464 available bytes; 98.72% used; 110410526 free inodes.

server2 `/tmp`: 22878142464 available bytes; 98.72% used; 110410526 free inodes.

server2 `/var/tmp`: 22878142464 available bytes; 98.72% used; 110410526 free inodes.

server2 `/mnt/raid5`: 353468338176 available bytes; 97.56% used; 445098776 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84449099776 available bytes; 95.29% used; 114156031 free inodes.

server3 `/home`: 84449099776 available bytes; 95.29% used; 114156031 free inodes.

server3 `/data`: 142527795200 available bytes; 98.03% used; 225813452 free inodes.

server3 `/tmp`: 84449099776 available bytes; 95.29% used; 114156031 free inodes.

server3 `/var/tmp`: 84449099776 available bytes; 95.29% used; 114156031 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105639231488 available bytes; 94.10% used; 114350381 free inodes.

server4 `/home`: 105639231488 available bytes; 94.10% used; 114350381 free inodes.

server4 `/data`: 251115499520 available bytes; 96.53% used; 225018197 free inodes.

server4 `/tmp`: 105639231488 available bytes; 94.10% used; 114350381 free inodes.

server4 `/var/tmp`: 105639231488 available bytes; 94.10% used; 114350381 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
