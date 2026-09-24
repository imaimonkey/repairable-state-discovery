# V2R cluster inventory

2026-09-24T05:42:05.290292+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324529123328 available bytes; 81.90% used; 112492144 free inodes.

server1 `/home`: 324529123328 available bytes; 81.90% used; 112492144 free inodes.

server1 `/tmp`: 324529123328 available bytes; 81.90% used; 112492144 free inodes.

server1 `/var/tmp`: 324529123328 available bytes; 81.90% used; 112492144 free inodes.

server1 `/mnt/raid5`: 517629157376 available bytes; 97.63% used; 337723940 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57915469824 available bytes; 96.77% used; 110431340 free inodes.

server2 `/home`: 57915469824 available bytes; 96.77% used; 110431340 free inodes.

server2 `/tmp`: 57915469824 available bytes; 96.77% used; 110431340 free inodes.

server2 `/var/tmp`: 57915469824 available bytes; 96.77% used; 110431340 free inodes.

server2 `/mnt/raid5`: 522006573056 available bytes; 96.39% used; 445193652 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127191707648 available bytes; 92.90% used; 114198483 free inodes.

server3 `/home`: 127191707648 available bytes; 92.90% used; 114198483 free inodes.

server3 `/data`: 185247944704 available bytes; 97.44% used; 225839152 free inodes.

server3 `/tmp`: 127191707648 available bytes; 92.90% used; 114198483 free inodes.

server3 `/var/tmp`: 127191707648 available bytes; 92.90% used; 114198483 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105816363008 available bytes; 94.10% used; 114349351 free inodes.

server4 `/home`: 105816363008 available bytes; 94.10% used; 114349351 free inodes.

server4 `/data`: 251475222528 available bytes; 96.52% used; 225358018 free inodes.

server4 `/tmp`: 105816363008 available bytes; 94.10% used; 114349351 free inodes.

server4 `/var/tmp`: 105816363008 available bytes; 94.10% used; 114349351 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
