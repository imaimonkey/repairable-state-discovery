# V2R cluster inventory

2026-09-24T15:51:09.334589+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324026228736 available bytes; 81.92% used; 112481462 free inodes.

server1 `/home`: 324026228736 available bytes; 81.92% used; 112481462 free inodes.

server1 `/tmp`: 324026228736 available bytes; 81.92% used; 112481462 free inodes.

server1 `/var/tmp`: 324026228736 available bytes; 81.92% used; 112481462 free inodes.

server1 `/mnt/raid5`: 416703852544 available bytes; 98.09% used; 337658730 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57368485888 available bytes; 96.80% used; 110427293 free inodes.

server2 `/home`: 57368485888 available bytes; 96.80% used; 110427293 free inodes.

server2 `/tmp`: 57368485888 available bytes; 96.80% used; 110427293 free inodes.

server2 `/var/tmp`: 57368485888 available bytes; 96.80% used; 110427293 free inodes.

server2 `/mnt/raid5`: 502151892992 available bytes; 96.53% used; 445165358 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84470063104 available bytes; 95.29% used; 114156861 free inodes.

server3 `/home`: 84470063104 available bytes; 95.29% used; 114156861 free inodes.

server3 `/data`: 160145227776 available bytes; 97.79% used; 225806143 free inodes.

server3 `/tmp`: 84470063104 available bytes; 95.29% used; 114156861 free inodes.

server3 `/var/tmp`: 84470063104 available bytes; 95.29% used; 114156861 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105707044864 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105707044864 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89350037504 available bytes; 98.77% used; 225256452 free inodes.

server4 `/tmp`: 105707044864 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105707044864 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
