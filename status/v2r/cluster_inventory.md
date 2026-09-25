# V2R cluster inventory

2026-09-25T06:44:04.597367+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872956928 available bytes; 82.21% used; 112480357 free inodes.

server1 `/home`: 318872956928 available bytes; 82.21% used; 112480357 free inodes.

server1 `/tmp`: 318872956928 available bytes; 82.21% used; 112480357 free inodes.

server1 `/var/tmp`: 318872956928 available bytes; 82.21% used; 112480357 free inodes.

server1 `/mnt/raid5`: 399787180032 available bytes; 98.17% used; 337561371 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22884917248 available bytes; 98.72% used; 110410542 free inodes.

server2 `/home`: 22884917248 available bytes; 98.72% used; 110410542 free inodes.

server2 `/tmp`: 22884917248 available bytes; 98.72% used; 110410542 free inodes.

server2 `/var/tmp`: 22884917248 available bytes; 98.72% used; 110410542 free inodes.

server2 `/mnt/raid5`: 353581469696 available bytes; 97.56% used; 445098813 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84449624064 available bytes; 95.29% used; 114156029 free inodes.

server3 `/home`: 84449624064 available bytes; 95.29% used; 114156029 free inodes.

server3 `/data`: 142528487424 available bytes; 98.03% used; 225813529 free inodes.

server3 `/tmp`: 84449624064 available bytes; 95.29% used; 114156029 free inodes.

server3 `/var/tmp`: 84449624064 available bytes; 95.29% used; 114156029 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105639354368 available bytes; 94.10% used; 114350382 free inodes.

server4 `/home`: 105639354368 available bytes; 94.10% used; 114350382 free inodes.

server4 `/data`: 251118088192 available bytes; 96.53% used; 225018630 free inodes.

server4 `/tmp`: 105639354368 available bytes; 94.10% used; 114350382 free inodes.

server4 `/var/tmp`: 105639354368 available bytes; 94.10% used; 114350382 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
