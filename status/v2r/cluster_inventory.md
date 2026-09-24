# V2R cluster inventory

2026-09-24T07:52:31.714016+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324418863104 available bytes; 81.90% used; 112490830 free inodes.

server1 `/home`: 324418863104 available bytes; 81.90% used; 112490830 free inodes.

server1 `/tmp`: 324418863104 available bytes; 81.90% used; 112490830 free inodes.

server1 `/var/tmp`: 324418863104 available bytes; 81.90% used; 112490830 free inodes.

server1 `/mnt/raid5`: 509732876288 available bytes; 97.66% used; 337722412 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57830592512 available bytes; 96.77% used; 110431092 free inodes.

server2 `/home`: 57830592512 available bytes; 96.77% used; 110431092 free inodes.

server2 `/tmp`: 57830592512 available bytes; 96.77% used; 110431092 free inodes.

server2 `/var/tmp`: 57830592512 available bytes; 96.77% used; 110431092 free inodes.

server2 `/mnt/raid5`: 517595041792 available bytes; 96.42% used; 445180811 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 106546921472 available bytes; 94.05% used; 114200201 free inodes.

server3 `/home`: 106546921472 available bytes; 94.05% used; 114200201 free inodes.

server3 `/data`: 136601595904 available bytes; 98.11% used; 225839169 free inodes.

server3 `/tmp`: 106546921472 available bytes; 94.05% used; 114200201 free inodes.

server3 `/var/tmp`: 106546921472 available bytes; 94.05% used; 114200201 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105779695616 available bytes; 94.10% used; 114349173 free inodes.

server4 `/home`: 105779695616 available bytes; 94.10% used; 114349173 free inodes.

server4 `/data`: 284352655360 available bytes; 96.07% used; 225366624 free inodes.

server4 `/tmp`: 105779695616 available bytes; 94.10% used; 114349173 free inodes.

server4 `/var/tmp`: 105779695616 available bytes; 94.10% used; 114349173 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
