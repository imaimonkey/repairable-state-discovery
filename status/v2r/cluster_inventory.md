# V2R cluster inventory

2026-09-24T14:33:21.490923+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324052393984 available bytes; 81.92% used; 112481449 free inodes.

server1 `/home`: 324052393984 available bytes; 81.92% used; 112481449 free inodes.

server1 `/tmp`: 324052393984 available bytes; 81.92% used; 112481449 free inodes.

server1 `/var/tmp`: 324052393984 available bytes; 81.92% used; 112481449 free inodes.

server1 `/mnt/raid5`: 416885383168 available bytes; 98.09% used; 337667821 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57458884608 available bytes; 96.79% used; 110428070 free inodes.

server2 `/home`: 57458884608 available bytes; 96.79% used; 110428070 free inodes.

server2 `/tmp`: 57458884608 available bytes; 96.79% used; 110428070 free inodes.

server2 `/var/tmp`: 57458884608 available bytes; 96.79% used; 110428070 free inodes.

server2 `/mnt/raid5`: 504389050368 available bytes; 96.51% used; 445167850 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84483977216 available bytes; 95.29% used; 114158862 free inodes.

server3 `/home`: 84483977216 available bytes; 95.29% used; 114158862 free inodes.

server3 `/data`: 160862818304 available bytes; 97.78% used; 225808103 free inodes.

server3 `/tmp`: 84483977216 available bytes; 95.29% used; 114158862 free inodes.

server3 `/var/tmp`: 84483977216 available bytes; 95.29% used; 114158862 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105758777344 available bytes; 94.10% used; 114348687 free inodes.

server4 `/home`: 105758777344 available bytes; 94.10% used; 114348687 free inodes.

server4 `/data`: 69177409536 available bytes; 99.04% used; 225257005 free inodes.

server4 `/tmp`: 105758777344 available bytes; 94.10% used; 114348687 free inodes.

server4 `/var/tmp`: 105758777344 available bytes; 94.10% used; 114348687 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
