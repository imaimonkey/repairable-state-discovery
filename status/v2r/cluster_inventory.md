# V2R cluster inventory

2026-09-24T23:31:41.023852+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319012560896 available bytes; 82.20% used; 112480781 free inodes.

server1 `/home`: 319012560896 available bytes; 82.20% used; 112480781 free inodes.

server1 `/tmp`: 319012560896 available bytes; 82.20% used; 112480781 free inodes.

server1 `/var/tmp`: 319012560896 available bytes; 82.20% used; 112480781 free inodes.

server1 `/mnt/raid5`: 415226384384 available bytes; 98.10% used; 337613037 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23114940416 available bytes; 98.71% used; 110410808 free inodes.

server2 `/home`: 23114940416 available bytes; 98.71% used; 110410808 free inodes.

server2 `/tmp`: 23114940416 available bytes; 98.71% used; 110410808 free inodes.

server2 `/var/tmp`: 23114940416 available bytes; 98.71% used; 110410808 free inodes.

server2 `/mnt/raid5`: 486345285632 available bytes; 96.64% used; 445151126 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84369231872 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84369231872 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148180869120 available bytes; 97.95% used; 225800882 free inodes.

server3 `/tmp`: 84369231872 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84369231872 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105799520256 available bytes; 94.10% used; 114348305 free inodes.

server4 `/home`: 105799520256 available bytes; 94.10% used; 114348305 free inodes.

server4 `/data`: 61315063808 available bytes; 99.15% used; 225145187 free inodes.

server4 `/tmp`: 105799520256 available bytes; 94.10% used; 114348305 free inodes.

server4 `/var/tmp`: 105799520256 available bytes; 94.10% used; 114348305 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
