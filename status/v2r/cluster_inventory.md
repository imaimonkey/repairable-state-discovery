# V2R cluster inventory

2026-09-24T16:56:28.998579+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324022956032 available bytes; 81.92% used; 112481444 free inodes.

server1 `/home`: 324022956032 available bytes; 81.92% used; 112481444 free inodes.

server1 `/tmp`: 324022956032 available bytes; 81.92% used; 112481444 free inodes.

server1 `/var/tmp`: 324022956032 available bytes; 81.92% used; 112481444 free inodes.

server1 `/mnt/raid5`: 416517976064 available bytes; 98.09% used; 337650293 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57069740032 available bytes; 96.82% used; 110418063 free inodes.

server2 `/home`: 57069740032 available bytes; 96.82% used; 110418063 free inodes.

server2 `/tmp`: 57069740032 available bytes; 96.82% used; 110418063 free inodes.

server2 `/var/tmp`: 57069740032 available bytes; 96.82% used; 110418063 free inodes.

server2 `/mnt/raid5`: 500136071168 available bytes; 96.54% used; 445163521 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84417216512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84417216512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 159172784128 available bytes; 97.80% used; 225787469 free inodes.

server3 `/tmp`: 84417216512 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84417216512 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105682644992 available bytes; 94.10% used; 114348574 free inodes.

server4 `/home`: 105682644992 available bytes; 94.10% used; 114348574 free inodes.

server4 `/data`: 89181724672 available bytes; 98.77% used; 225255046 free inodes.

server4 `/tmp`: 105682644992 available bytes; 94.10% used; 114348574 free inodes.

server4 `/var/tmp`: 105682644992 available bytes; 94.10% used; 114348574 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
