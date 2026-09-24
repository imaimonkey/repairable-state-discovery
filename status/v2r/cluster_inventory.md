# V2R cluster inventory

2026-09-24T16:33:13.493526+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324022931456 available bytes; 81.92% used; 112481454 free inodes.

server1 `/home`: 324022931456 available bytes; 81.92% used; 112481454 free inodes.

server1 `/tmp`: 324022931456 available bytes; 81.92% used; 112481454 free inodes.

server1 `/var/tmp`: 324022931456 available bytes; 81.92% used; 112481454 free inodes.

server1 `/mnt/raid5`: 416572940288 available bytes; 98.09% used; 337653023 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57324167168 available bytes; 96.80% used; 110426859 free inodes.

server2 `/home`: 57324167168 available bytes; 96.80% used; 110426859 free inodes.

server2 `/tmp`: 57324167168 available bytes; 96.80% used; 110426859 free inodes.

server2 `/var/tmp`: 57324167168 available bytes; 96.80% used; 110426859 free inodes.

server2 `/mnt/raid5`: 500309962752 available bytes; 96.54% used; 445164449 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84112080896 available bytes; 95.31% used; 114144953 free inodes.

server3 `/home`: 84112080896 available bytes; 95.31% used; 114144953 free inodes.

server3 `/data`: 159335485440 available bytes; 97.80% used; 225787987 free inodes.

server3 `/tmp`: 84112080896 available bytes; 95.31% used; 114144953 free inodes.

server3 `/var/tmp`: 84112080896 available bytes; 95.31% used; 114144953 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105688621056 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105688621056 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89273364480 available bytes; 98.77% used; 225255749 free inodes.

server4 `/tmp`: 105688621056 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105688621056 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
