# V2R cluster inventory

2026-09-25T05:43:55.527330+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318871478272 available bytes; 82.21% used; 112480333 free inodes.

server1 `/home`: 318871478272 available bytes; 82.21% used; 112480333 free inodes.

server1 `/tmp`: 318871478272 available bytes; 82.21% used; 112480333 free inodes.

server1 `/var/tmp`: 318871478272 available bytes; 82.21% used; 112480333 free inodes.

server1 `/mnt/raid5`: 408453570560 available bytes; 98.13% used; 337566616 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22914355200 available bytes; 98.72% used; 110410490 free inodes.

server2 `/home`: 22914355200 available bytes; 98.72% used; 110410490 free inodes.

server2 `/tmp`: 22914355200 available bytes; 98.72% used; 110410490 free inodes.

server2 `/var/tmp`: 22914355200 available bytes; 98.72% used; 110410490 free inodes.

server2 `/mnt/raid5`: 425989423104 available bytes; 97.06% used; 445102377 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84313112576 available bytes; 95.30% used; 114156039 free inodes.

server3 `/home`: 84313112576 available bytes; 95.30% used; 114156039 free inodes.

server3 `/data`: 142775324672 available bytes; 98.03% used; 225814595 free inodes.

server3 `/tmp`: 84313112576 available bytes; 95.30% used; 114156039 free inodes.

server3 `/var/tmp`: 84313112576 available bytes; 95.30% used; 114156039 free inodes.
| server4 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105649590272 available bytes; 94.10% used; 114350389 free inodes.

server4 `/home`: 105649590272 available bytes; 94.10% used; 114350389 free inodes.

server4 `/data`: 24758464512 available bytes; 99.66% used; 224965875 free inodes.

server4 `/tmp`: 105649590272 available bytes; 94.10% used; 114350389 free inodes.

server4 `/var/tmp`: 105649590272 available bytes; 94.10% used; 114350389 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
