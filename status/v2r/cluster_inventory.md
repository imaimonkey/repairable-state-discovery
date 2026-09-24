# V2R cluster inventory

2026-09-24T18:13:53.491749+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324009582592 available bytes; 81.92% used; 112481441 free inodes.

server1 `/home`: 324009582592 available bytes; 81.92% used; 112481441 free inodes.

server1 `/tmp`: 324009582592 available bytes; 81.92% used; 112481441 free inodes.

server1 `/var/tmp`: 324009582592 available bytes; 81.92% used; 112481441 free inodes.

server1 `/mnt/raid5`: 416354811904 available bytes; 98.09% used; 337641272 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 54504681472 available bytes; 96.96% used; 110412069 free inodes.

server2 `/home`: 54504681472 available bytes; 96.96% used; 110412069 free inodes.

server2 `/tmp`: 54504681472 available bytes; 96.96% used; 110412069 free inodes.

server2 `/var/tmp`: 54504681472 available bytes; 96.96% used; 110412069 free inodes.

server2 `/mnt/raid5`: 496689893376 available bytes; 96.57% used; 445161106 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84408127488 available bytes; 95.29% used; 114156129 free inodes.

server3 `/home`: 84408127488 available bytes; 95.29% used; 114156129 free inodes.

server3 `/data`: 153085046784 available bytes; 97.88% used; 225800822 free inodes.

server3 `/tmp`: 84408127488 available bytes; 95.29% used; 114156129 free inodes.

server3 `/var/tmp`: 84408127488 available bytes; 95.29% used; 114156129 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105663094784 available bytes; 94.10% used; 114348526 free inodes.

server4 `/home`: 105663094784 available bytes; 94.10% used; 114348526 free inodes.

server4 `/data`: 90074701824 available bytes; 98.76% used; 225268179 free inodes.

server4 `/tmp`: 105663094784 available bytes; 94.10% used; 114348526 free inodes.

server4 `/var/tmp`: 105663094784 available bytes; 94.10% used; 114348526 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
