# V2R cluster inventory

2026-09-24T15:30:54.085739+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324017991680 available bytes; 81.92% used; 112481437 free inodes.

server1 `/home`: 324017991680 available bytes; 81.92% used; 112481437 free inodes.

server1 `/tmp`: 324017991680 available bytes; 81.92% used; 112481437 free inodes.

server1 `/var/tmp`: 324017991680 available bytes; 81.92% used; 112481437 free inodes.

server1 `/mnt/raid5`: 416762646528 available bytes; 98.09% used; 337661083 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57390419968 available bytes; 96.80% used; 110427495 free inodes.

server2 `/home`: 57390419968 available bytes; 96.80% used; 110427495 free inodes.

server2 `/tmp`: 57390419968 available bytes; 96.80% used; 110427495 free inodes.

server2 `/var/tmp`: 57390419968 available bytes; 96.80% used; 110427495 free inodes.

server2 `/mnt/raid5`: 502687952896 available bytes; 96.53% used; 445165988 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84474646528 available bytes; 95.29% used; 114157054 free inodes.

server3 `/home`: 84474646528 available bytes; 95.29% used; 114157054 free inodes.

server3 `/data`: 160365096960 available bytes; 97.78% used; 225806546 free inodes.

server3 `/tmp`: 84474646528 available bytes; 95.29% used; 114157054 free inodes.

server3 `/var/tmp`: 84474646528 available bytes; 95.29% used; 114157054 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716289536 available bytes; 94.10% used; 114348626 free inodes.

server4 `/home`: 105716289536 available bytes; 94.10% used; 114348626 free inodes.

server4 `/data`: 89398607872 available bytes; 98.76% used; 225256823 free inodes.

server4 `/tmp`: 105716289536 available bytes; 94.10% used; 114348626 free inodes.

server4 `/var/tmp`: 105716289536 available bytes; 94.10% used; 114348626 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
