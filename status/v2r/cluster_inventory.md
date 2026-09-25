# V2R cluster inventory

2026-09-25T13:29:31.610390+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319103340544 available bytes; 82.20% used; 112477545 free inodes.

server1 `/home`: 319103340544 available bytes; 82.20% used; 112477545 free inodes.

server1 `/tmp`: 319103340544 available bytes; 82.20% used; 112477545 free inodes.

server1 `/var/tmp`: 319103340544 available bytes; 82.20% used; 112477545 free inodes.

server1 `/mnt/raid5`: 371036938240 available bytes; 98.30% used; 337547844 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 15494590464 available bytes; 99.14% used; 110408608 free inodes.

server2 `/home`: 15494590464 available bytes; 99.14% used; 110408608 free inodes.

server2 `/tmp`: 15494590464 available bytes; 99.14% used; 110408608 free inodes.

server2 `/var/tmp`: 15494590464 available bytes; 99.14% used; 110408608 free inodes.

server2 `/mnt/raid5`: 323466969088 available bytes; 97.76% used; 445076935 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84201963520 available bytes; 95.30% used; 114154972 free inodes.

server3 `/home`: 84201963520 available bytes; 95.30% used; 114154972 free inodes.

server3 `/data`: 142350434304 available bytes; 98.03% used; 225809703 free inodes.

server3 `/tmp`: 84201963520 available bytes; 95.30% used; 114154972 free inodes.

server3 `/var/tmp`: 84201963520 available bytes; 95.30% used; 114154972 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105655963648 available bytes; 94.10% used; 114349707 free inodes.

server4 `/home`: 105655963648 available bytes; 94.10% used; 114349707 free inodes.

server4 `/data`: 231397220352 available bytes; 96.80% used; 224951868 free inodes.

server4 `/tmp`: 105655963648 available bytes; 94.10% used; 114349707 free inodes.

server4 `/var/tmp`: 105655963648 available bytes; 94.10% used; 114349707 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
