# V2R cluster inventory

2026-09-24T15:32:26.626606+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324019552256 available bytes; 81.92% used; 112481439 free inodes.

server1 `/home`: 324019552256 available bytes; 81.92% used; 112481439 free inodes.

server1 `/tmp`: 324019552256 available bytes; 81.92% used; 112481439 free inodes.

server1 `/var/tmp`: 324019552256 available bytes; 81.92% used; 112481439 free inodes.

server1 `/mnt/raid5`: 416760250368 available bytes; 98.09% used; 337660906 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57389240320 available bytes; 96.80% used; 110427479 free inodes.

server2 `/home`: 57389240320 available bytes; 96.80% used; 110427479 free inodes.

server2 `/tmp`: 57389240320 available bytes; 96.80% used; 110427479 free inodes.

server2 `/var/tmp`: 57389240320 available bytes; 96.80% used; 110427479 free inodes.

server2 `/mnt/raid5`: 502703882240 available bytes; 96.53% used; 445165849 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84474417152 available bytes; 95.29% used; 114157054 free inodes.

server3 `/home`: 84474417152 available bytes; 95.29% used; 114157054 free inodes.

server3 `/data`: 160352542720 available bytes; 97.78% used; 225806511 free inodes.

server3 `/tmp`: 84474417152 available bytes; 95.29% used; 114157054 free inodes.

server3 `/var/tmp`: 84474417152 available bytes; 95.29% used; 114157054 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105716125696 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105716125696 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89392119808 available bytes; 98.76% used; 225256715 free inodes.

server4 `/tmp`: 105716125696 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105716125696 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
