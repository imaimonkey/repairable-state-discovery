# V2R cluster inventory

2026-09-24T17:46:05.861360+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324007333888 available bytes; 81.92% used; 112481433 free inodes.

server1 `/home`: 324007333888 available bytes; 81.92% used; 112481433 free inodes.

server1 `/tmp`: 324007333888 available bytes; 81.92% used; 112481433 free inodes.

server1 `/var/tmp`: 324007333888 available bytes; 81.92% used; 112481433 free inodes.

server1 `/mnt/raid5`: 416414478336 available bytes; 98.09% used; 337644519 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 56902631424 available bytes; 96.83% used; 110412363 free inodes.

server2 `/home`: 56902631424 available bytes; 96.83% used; 110412363 free inodes.

server2 `/tmp`: 56902631424 available bytes; 96.83% used; 110412363 free inodes.

server2 `/var/tmp`: 56902631424 available bytes; 96.83% used; 110412363 free inodes.

server2 `/mnt/raid5`: 498294358016 available bytes; 96.56% used; 445161844 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408635392 available bytes; 95.29% used; 114156138 free inodes.

server3 `/home`: 84408635392 available bytes; 95.29% used; 114156138 free inodes.

server3 `/data`: 151948173312 available bytes; 97.90% used; 225786497 free inodes.

server3 `/tmp`: 84408635392 available bytes; 95.29% used; 114156138 free inodes.

server3 `/var/tmp`: 84408635392 available bytes; 95.29% used; 114156138 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672531968 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105672531968 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89059524608 available bytes; 98.77% used; 225253755 free inodes.

server4 `/tmp`: 105672531968 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105672531968 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
