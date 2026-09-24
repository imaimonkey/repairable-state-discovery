# V2R cluster inventory

2026-09-24T15:44:48.058671+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324018741248 available bytes; 81.92% used; 112481447 free inodes.

server1 `/home`: 324018741248 available bytes; 81.92% used; 112481447 free inodes.

server1 `/tmp`: 324018741248 available bytes; 81.92% used; 112481447 free inodes.

server1 `/var/tmp`: 324018741248 available bytes; 81.92% used; 112481447 free inodes.

server1 `/mnt/raid5`: 416716451840 available bytes; 98.09% used; 337659466 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57373986816 available bytes; 96.80% used; 110427357 free inodes.

server2 `/home`: 57373986816 available bytes; 96.80% used; 110427357 free inodes.

server2 `/tmp`: 57373986816 available bytes; 96.80% used; 110427357 free inodes.

server2 `/var/tmp`: 57373986816 available bytes; 96.80% used; 110427357 free inodes.

server2 `/mnt/raid5`: 489277353984 available bytes; 96.62% used; 445165582 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84872384512 available bytes; 95.26% used; 114184727 free inodes.

server3 `/home`: 84872384512 available bytes; 95.26% used; 114184727 free inodes.

server3 `/data`: 160192331776 available bytes; 97.79% used; 225806259 free inodes.

server3 `/tmp`: 84872384512 available bytes; 95.26% used; 114184727 free inodes.

server3 `/var/tmp`: 84872384512 available bytes; 95.26% used; 114184727 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105707286528 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105707286528 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89374576640 available bytes; 98.76% used; 225256586 free inodes.

server4 `/tmp`: 105707286528 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105707286528 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
