# V2R cluster inventory

2026-09-24T12:45:58.793960+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039561216 available bytes; 81.92% used; 112481557 free inodes.

server1 `/home`: 324039561216 available bytes; 81.92% used; 112481557 free inodes.

server1 `/tmp`: 324039561216 available bytes; 81.92% used; 112481556 free inodes.

server1 `/var/tmp`: 324039561216 available bytes; 81.92% used; 112481556 free inodes.

server1 `/mnt/raid5`: 403361357824 available bytes; 98.15% used; 337680421 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57579429888 available bytes; 96.79% used; 110429173 free inodes.

server2 `/home`: 57579429888 available bytes; 96.79% used; 110429173 free inodes.

server2 `/tmp`: 57579429888 available bytes; 96.79% used; 110429173 free inodes.

server2 `/var/tmp`: 57579429888 available bytes; 96.79% used; 110429173 free inodes.

server2 `/mnt/raid5`: 508019642368 available bytes; 96.49% used; 445171412 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85701386240 available bytes; 95.22% used; 114197822 free inodes.

server3 `/home`: 85701386240 available bytes; 95.22% used; 114197822 free inodes.

server3 `/data`: 163137912832 available bytes; 97.75% used; 225814419 free inodes.

server3 `/tmp`: 85701386240 available bytes; 95.22% used; 114197822 free inodes.

server3 `/var/tmp`: 85701386240 available bytes; 95.22% used; 114197822 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105780031488 available bytes; 94.10% used; 114348784 free inodes.

server4 `/home`: 105780031488 available bytes; 94.10% used; 114348784 free inodes.

server4 `/data`: 90047811584 available bytes; 98.76% used; 225257236 free inodes.

server4 `/tmp`: 105780031488 available bytes; 94.10% used; 114348784 free inodes.

server4 `/var/tmp`: 105780031488 available bytes; 94.10% used; 114348784 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
