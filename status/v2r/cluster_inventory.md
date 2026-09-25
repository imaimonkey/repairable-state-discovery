# V2R cluster inventory

2026-09-25T08:24:29.330828+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318826962944 available bytes; 82.21% used; 112480363 free inodes.

server1 `/home`: 318826962944 available bytes; 82.21% used; 112480363 free inodes.

server1 `/tmp`: 318826962944 available bytes; 82.21% used; 112480363 free inodes.

server1 `/var/tmp`: 318826962944 available bytes; 82.21% used; 112480363 free inodes.

server1 `/mnt/raid5`: 364237414400 available bytes; 98.33% used; 337557123 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22832369664 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22832369664 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22832369664 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22832369664 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 333454528512 available bytes; 97.70% used; 445094539 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84437172224 available bytes; 95.29% used; 114156046 free inodes.

server3 `/home`: 84437172224 available bytes; 95.29% used; 114156046 free inodes.

server3 `/data`: 142382813184 available bytes; 98.03% used; 225811767 free inodes.

server3 `/tmp`: 84437172224 available bytes; 95.29% used; 114156046 free inodes.

server3 `/var/tmp`: 84437172224 available bytes; 95.29% used; 114156046 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105685716992 available bytes; 94.10% used; 114350335 free inodes.

server4 `/home`: 105685716992 available bytes; 94.10% used; 114350335 free inodes.

server4 `/data`: 246767054848 available bytes; 96.59% used; 225005723 free inodes.

server4 `/tmp`: 105685716992 available bytes; 94.10% used; 114350335 free inodes.

server4 `/var/tmp`: 105685716992 available bytes; 94.10% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
