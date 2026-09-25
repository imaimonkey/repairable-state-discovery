# V2R cluster inventory

2026-09-25T05:30:03.667900+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318860447744 available bytes; 82.21% used; 112480337 free inodes.

server1 `/home`: 318860447744 available bytes; 82.21% used; 112480337 free inodes.

server1 `/tmp`: 318860447744 available bytes; 82.21% used; 112480337 free inodes.

server1 `/var/tmp`: 318860447744 available bytes; 82.21% used; 112480337 free inodes.

server1 `/mnt/raid5`: 408495882240 available bytes; 98.13% used; 337568268 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22921453568 available bytes; 98.72% used; 110410433 free inodes.

server2 `/home`: 22921453568 available bytes; 98.72% used; 110410433 free inodes.

server2 `/tmp`: 22921453568 available bytes; 98.72% used; 110410433 free inodes.

server2 `/var/tmp`: 22921453568 available bytes; 98.72% used; 110410433 free inodes.

server2 `/mnt/raid5`: 444214444032 available bytes; 96.93% used; 445108103 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84312895488 available bytes; 95.30% used; 114156041 free inodes.

server3 `/home`: 84312895488 available bytes; 95.30% used; 114156041 free inodes.

server3 `/data`: 142780846080 available bytes; 98.03% used; 225814815 free inodes.

server3 `/tmp`: 84312895488 available bytes; 95.30% used; 114156041 free inodes.

server3 `/var/tmp`: 84312895488 available bytes; 95.30% used; 114156041 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658404864 available bytes; 94.10% used; 114350392 free inodes.

server4 `/home`: 105658404864 available bytes; 94.10% used; 114350392 free inodes.

server4 `/data`: 26405330944 available bytes; 99.64% used; 224968276 free inodes.

server4 `/tmp`: 105658404864 available bytes; 94.10% used; 114350392 free inodes.

server4 `/var/tmp`: 105658404864 available bytes; 94.10% used; 114350392 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
