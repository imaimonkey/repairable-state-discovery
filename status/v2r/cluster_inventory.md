# V2R cluster inventory

2026-09-24T16:15:58.390703+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324025532416 available bytes; 81.92% used; 112481453 free inodes.

server1 `/home`: 324025532416 available bytes; 81.92% used; 112481453 free inodes.

server1 `/tmp`: 324025532416 available bytes; 81.92% used; 112481453 free inodes.

server1 `/var/tmp`: 324025532416 available bytes; 81.92% used; 112481453 free inodes.

server1 `/mnt/raid5`: 416601870336 available bytes; 98.09% used; 337655022 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57343209472 available bytes; 96.80% used; 110427033 free inodes.

server2 `/home`: 57343209472 available bytes; 96.80% used; 110427033 free inodes.

server2 `/tmp`: 57343209472 available bytes; 96.80% used; 110427033 free inodes.

server2 `/var/tmp`: 57343209472 available bytes; 96.80% used; 110427033 free inodes.

server2 `/mnt/raid5`: 501393006592 available bytes; 96.54% used; 445165109 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 84457353216 available bytes; 95.29% used; 114167414 free inodes.

server3 `/home`: 84457353216 available bytes; 95.29% used; 114167414 free inodes.

server3 `/data`: 159977431040 available bytes; 97.79% used; 225805523 free inodes.

server3 `/tmp`: 84457353216 available bytes; 95.29% used; 114167414 free inodes.

server3 `/var/tmp`: 84457353216 available bytes; 95.29% used; 114167414 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105697570816 available bytes; 94.10% used; 114348602 free inodes.

server4 `/home`: 105697570816 available bytes; 94.10% used; 114348602 free inodes.

server4 `/data`: 89300746240 available bytes; 98.77% used; 225256021 free inodes.

server4 `/tmp`: 105697570816 available bytes; 94.10% used; 114348602 free inodes.

server4 `/var/tmp`: 105697570816 available bytes; 94.10% used; 114348602 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
