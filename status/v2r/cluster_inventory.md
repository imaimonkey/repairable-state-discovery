# V2R cluster inventory

2026-09-24T02:12:42.526603+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325444849664 available bytes; 81.84% used; 112499221 free inodes.

server1 `/home`: 325444849664 available bytes; 81.84% used; 112499221 free inodes.

server1 `/tmp`: 325444849664 available bytes; 81.84% used; 112499221 free inodes.

server1 `/var/tmp`: 325444849664 available bytes; 81.84% used; 112499221 free inodes.

server1 `/mnt/raid5`: 721410404352 available bytes; 96.69% used; 337733503 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40906018816 available bytes; 97.72% used; 110431660 free inodes.

server2 `/home`: 40906018816 available bytes; 97.72% used; 110431660 free inodes.

server2 `/tmp`: 40906018816 available bytes; 97.72% used; 110431660 free inodes.

server2 `/var/tmp`: 40906018816 available bytes; 97.72% used; 110431660 free inodes.

server2 `/mnt/raid5`: 529010323456 available bytes; 96.34% used; 445199953 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292684804096 available bytes; 83.67% used; 114210523 free inodes.

server3 `/home`: 292684804096 available bytes; 83.67% used; 114210523 free inodes.

server3 `/data`: 18080436224 available bytes; 99.75% used; 225841281 free inodes.

server3 `/tmp`: 292684804096 available bytes; 83.67% used; 114210523 free inodes.

server3 `/var/tmp`: 292684804096 available bytes; 83.67% used; 114210523 free inodes.
| server4 | True | ['2', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105932394496 available bytes; 94.09% used; 114348278 free inodes.

server4 `/home`: 105932394496 available bytes; 94.09% used; 114348278 free inodes.

server4 `/data`: 289760759808 available bytes; 96.00% used; 225388462 free inodes.

server4 `/tmp`: 105932394496 available bytes; 94.09% used; 114348278 free inodes.

server4 `/var/tmp`: 105932394496 available bytes; 94.09% used; 114348278 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
