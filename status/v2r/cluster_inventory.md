# V2R cluster inventory

2026-09-24T15:46:21.293099+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026593280 available bytes; 81.92% used; 112481461 free inodes.

server1 `/home`: 324026593280 available bytes; 81.92% used; 112481461 free inodes.

server1 `/tmp`: 324026593280 available bytes; 81.92% used; 112481461 free inodes.

server1 `/var/tmp`: 324026593280 available bytes; 81.92% used; 112481461 free inodes.

server1 `/mnt/raid5`: 416712396800 available bytes; 98.09% used; 337659286 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57371398144 available bytes; 96.80% used; 110427339 free inodes.

server2 `/home`: 57371398144 available bytes; 96.80% used; 110427339 free inodes.

server2 `/tmp`: 57371398144 available bytes; 96.80% used; 110427339 free inodes.

server2 `/var/tmp`: 57371398144 available bytes; 96.80% used; 110427339 free inodes.

server2 `/mnt/raid5`: 502302216192 available bytes; 96.53% used; 445165507 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84853891072 available bytes; 95.26% used; 114182302 free inodes.

server3 `/home`: 84853891072 available bytes; 95.26% used; 114182302 free inodes.

server3 `/data`: 160182345728 available bytes; 97.79% used; 225806226 free inodes.

server3 `/tmp`: 84853891072 available bytes; 95.26% used; 114182302 free inodes.

server3 `/var/tmp`: 84853891072 available bytes; 95.26% used; 114182302 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105707225088 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105707225088 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89366765568 available bytes; 98.76% used; 225256580 free inodes.

server4 `/tmp`: 105707225088 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105707225088 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
