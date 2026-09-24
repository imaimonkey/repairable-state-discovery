# V2R cluster inventory

2026-09-24T15:49:29.823987+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324025540608 available bytes; 81.92% used; 112481450 free inodes.

server1 `/home`: 324025540608 available bytes; 81.92% used; 112481450 free inodes.

server1 `/tmp`: 324025540608 available bytes; 81.92% used; 112481450 free inodes.

server1 `/var/tmp`: 324025540608 available bytes; 81.92% used; 112481450 free inodes.

server1 `/mnt/raid5`: 416707477504 available bytes; 98.09% used; 337658924 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57368604672 available bytes; 96.80% used; 110427307 free inodes.

server2 `/home`: 57368604672 available bytes; 96.80% used; 110427307 free inodes.

server2 `/tmp`: 57368604672 available bytes; 96.80% used; 110427307 free inodes.

server2 `/var/tmp`: 57368604672 available bytes; 96.80% used; 110427307 free inodes.

server2 `/mnt/raid5`: 502204297216 available bytes; 96.53% used; 445165535 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84470210560 available bytes; 95.29% used; 114156861 free inodes.

server3 `/home`: 84470210560 available bytes; 95.29% used; 114156861 free inodes.

server3 `/data`: 160156368896 available bytes; 97.79% used; 225806166 free inodes.

server3 `/tmp`: 84470210560 available bytes; 95.29% used; 114156861 free inodes.

server3 `/var/tmp`: 84470210560 available bytes; 95.29% used; 114156861 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105707114496 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105707114496 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89363021824 available bytes; 98.76% used; 225256577 free inodes.

server4 `/tmp`: 105707114496 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105707114496 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
