# V2R cluster inventory

2026-09-25T01:25:25.057138+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319078543360 available bytes; 82.20% used; 112480770 free inodes.

server1 `/home`: 319078543360 available bytes; 82.20% used; 112480770 free inodes.

server1 `/tmp`: 319078543360 available bytes; 82.20% used; 112480770 free inodes.

server1 `/var/tmp`: 319078543360 available bytes; 82.20% used; 112480770 free inodes.

server1 `/mnt/raid5`: 416496291840 available bytes; 98.09% used; 337613502 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 23051083776 available bytes; 98.71% used; 110410770 free inodes.

server2 `/home`: 23051083776 available bytes; 98.71% used; 110410770 free inodes.

server2 `/tmp`: 23051083776 available bytes; 98.71% used; 110410770 free inodes.

server2 `/var/tmp`: 23051083776 available bytes; 98.71% used; 110410770 free inodes.

server2 `/mnt/raid5`: 490738376704 available bytes; 96.61% used; 445161766 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84356268032 available bytes; 95.29% used; 114156079 free inodes.

server3 `/home`: 84356268032 available bytes; 95.29% used; 114156079 free inodes.

server3 `/data`: 146763812864 available bytes; 97.97% used; 225812393 free inodes.

server3 `/tmp`: 84356268032 available bytes; 95.29% used; 114156079 free inodes.

server3 `/var/tmp`: 84356268032 available bytes; 95.29% used; 114156079 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779007488 available bytes; 94.10% used; 114348291 free inodes.

server4 `/home`: 105779007488 available bytes; 94.10% used; 114348291 free inodes.

server4 `/data`: 53321457664 available bytes; 99.26% used; 225030693 free inodes.

server4 `/tmp`: 105779007488 available bytes; 94.10% used; 114348291 free inodes.

server4 `/var/tmp`: 105779007488 available bytes; 94.10% used; 114348291 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
