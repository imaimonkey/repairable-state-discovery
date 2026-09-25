# V2R cluster inventory

2026-09-25T05:33:08.348958+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318872580096 available bytes; 82.21% used; 112480345 free inodes.

server1 `/home`: 318872580096 available bytes; 82.21% used; 112480345 free inodes.

server1 `/tmp`: 318872580096 available bytes; 82.21% used; 112480345 free inodes.

server1 `/var/tmp`: 318872580096 available bytes; 82.21% used; 112480345 free inodes.

server1 `/mnt/raid5`: 408485650432 available bytes; 98.13% used; 337567897 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22920667136 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22920667136 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22920667136 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22920667136 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 474231529472 available bytes; 96.72% used; 445103584 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84314193920 available bytes; 95.29% used; 114156043 free inodes.

server3 `/home`: 84314193920 available bytes; 95.29% used; 114156043 free inodes.

server3 `/data`: 142780596224 available bytes; 98.03% used; 225814767 free inodes.

server3 `/tmp`: 84314193920 available bytes; 95.29% used; 114156043 free inodes.

server3 `/var/tmp`: 84314193920 available bytes; 95.29% used; 114156043 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658318848 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105658318848 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 26391949312 available bytes; 99.64% used; 224967900 free inodes.

server4 `/tmp`: 105658318848 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105658318848 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
