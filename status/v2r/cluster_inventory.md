# V2R cluster inventory

2026-09-24T14:13:11.894578+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324058079232 available bytes; 81.92% used; 112481455 free inodes.

server1 `/home`: 324058079232 available bytes; 81.92% used; 112481455 free inodes.

server1 `/tmp`: 324058079232 available bytes; 81.92% used; 112481455 free inodes.

server1 `/var/tmp`: 324058079232 available bytes; 81.92% used; 112481455 free inodes.

server1 `/mnt/raid5`: 416936284160 available bytes; 98.09% used; 337670187 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57476833280 available bytes; 96.79% used; 110428285 free inodes.

server2 `/home`: 57476833280 available bytes; 96.79% used; 110428285 free inodes.

server2 `/tmp`: 57476833280 available bytes; 96.79% used; 110428285 free inodes.

server2 `/var/tmp`: 57476833280 available bytes; 96.79% used; 110428285 free inodes.

server2 `/mnt/raid5`: 504765825024 available bytes; 96.51% used; 445168722 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85062262784 available bytes; 95.25% used; 114189121 free inodes.

server3 `/home`: 85062262784 available bytes; 95.25% used; 114189121 free inodes.

server3 `/data`: 161031008256 available bytes; 97.77% used; 225809026 free inodes.

server3 `/tmp`: 85062262784 available bytes; 95.25% used; 114189121 free inodes.

server3 `/var/tmp`: 85062262784 available bytes; 95.25% used; 114189121 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105759596544 available bytes; 94.10% used; 114348703 free inodes.

server4 `/home`: 105759596544 available bytes; 94.10% used; 114348703 free inodes.

server4 `/data`: 69371965440 available bytes; 99.04% used; 225257078 free inodes.

server4 `/tmp`: 105759596544 available bytes; 94.10% used; 114348703 free inodes.

server4 `/var/tmp`: 105759596544 available bytes; 94.10% used; 114348703 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
