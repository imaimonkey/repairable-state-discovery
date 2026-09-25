# V2R cluster inventory

2026-09-25T13:03:42.218311+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319110524928 available bytes; 82.20% used; 112477582 free inodes.

server1 `/home`: 319110524928 available bytes; 82.20% used; 112477582 free inodes.

server1 `/tmp`: 319110524928 available bytes; 82.20% used; 112477582 free inodes.

server1 `/var/tmp`: 319110524928 available bytes; 82.20% used; 112477582 free inodes.

server1 `/mnt/raid5`: 364240134144 available bytes; 98.33% used; 337547904 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 8296226816 available bytes; 99.54% used; 110408780 free inodes.

server2 `/home`: 8296226816 available bytes; 99.54% used; 110408780 free inodes.

server2 `/tmp`: 8296226816 available bytes; 99.54% used; 110408780 free inodes.

server2 `/var/tmp`: 8296226816 available bytes; 99.54% used; 110408780 free inodes.

server2 `/mnt/raid5`: 324217438208 available bytes; 97.76% used; 445077970 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84207157248 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84207157248 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142354755584 available bytes; 98.03% used; 225810140 free inodes.

server3 `/tmp`: 84207157248 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84207157248 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105656676352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105656676352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231997435904 available bytes; 96.79% used; 224959743 free inodes.

server4 `/tmp`: 105656676352 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105656676352 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
