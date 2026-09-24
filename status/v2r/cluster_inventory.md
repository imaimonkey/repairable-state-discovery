# V2R cluster inventory

2026-09-24T12:05:13.685973+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324269645824 available bytes; 81.91% used; 112488331 free inodes.

server1 `/home`: 324269645824 available bytes; 81.91% used; 112488331 free inodes.

server1 `/tmp`: 324269645824 available bytes; 81.91% used; 112488331 free inodes.

server1 `/var/tmp`: 324269645824 available bytes; 81.91% used; 112488331 free inodes.

server1 `/mnt/raid5`: 405264650240 available bytes; 98.14% used; 337685321 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57624023040 available bytes; 96.79% used; 110429650 free inodes.

server2 `/home`: 57624023040 available bytes; 96.79% used; 110429650 free inodes.

server2 `/tmp`: 57624023040 available bytes; 96.79% used; 110429650 free inodes.

server2 `/var/tmp`: 57624023040 available bytes; 96.79% used; 110429650 free inodes.

server2 `/mnt/raid5`: 509275717632 available bytes; 96.48% used; 445172772 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85385064448 available bytes; 95.24% used; 114182179 free inodes.

server3 `/home`: 85385064448 available bytes; 95.24% used; 114182179 free inodes.

server3 `/data`: 163555991552 available bytes; 97.74% used; 225815588 free inodes.

server3 `/tmp`: 85385064448 available bytes; 95.24% used; 114182179 free inodes.

server3 `/var/tmp`: 85385064448 available bytes; 95.24% used; 114182179 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105718472704 available bytes; 94.10% used; 114348821 free inodes.

server4 `/home`: 105718472704 available bytes; 94.10% used; 114348821 free inodes.

server4 `/data`: 90433355776 available bytes; 98.75% used; 225257318 free inodes.

server4 `/tmp`: 105718472704 available bytes; 94.10% used; 114348821 free inodes.

server4 `/var/tmp`: 105718472704 available bytes; 94.10% used; 114348821 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
