# V2R cluster inventory

2026-09-24T13:07:50.137260+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324039122944 available bytes; 81.92% used; 112481547 free inodes.

server1 `/home`: 324039122944 available bytes; 81.92% used; 112481547 free inodes.

server1 `/tmp`: 324039122944 available bytes; 81.92% used; 112481547 free inodes.

server1 `/var/tmp`: 324039122944 available bytes; 81.92% used; 112481547 free inodes.

server1 `/mnt/raid5`: 417072365568 available bytes; 98.09% used; 337677819 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57553047552 available bytes; 96.79% used; 110428963 free inodes.

server2 `/home`: 57553047552 available bytes; 96.79% used; 110428963 free inodes.

server2 `/tmp`: 57553047552 available bytes; 96.79% used; 110428963 free inodes.

server2 `/var/tmp`: 57553047552 available bytes; 96.79% used; 110428963 free inodes.

server2 `/mnt/raid5`: 507314741248 available bytes; 96.49% used; 445170603 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85062041600 available bytes; 95.25% used; 114186379 free inodes.

server3 `/home`: 85062041600 available bytes; 95.25% used; 114186379 free inodes.

server3 `/data`: 161504055296 available bytes; 97.77% used; 225809762 free inodes.

server3 `/tmp`: 85062041600 available bytes; 95.25% used; 114186379 free inodes.

server3 `/var/tmp`: 85062041600 available bytes; 95.25% used; 114186379 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770647552 available bytes; 94.10% used; 114348757 free inodes.

server4 `/home`: 105770647552 available bytes; 94.10% used; 114348757 free inodes.

server4 `/data`: 90036924416 available bytes; 98.76% used; 225257181 free inodes.

server4 `/tmp`: 105770647552 available bytes; 94.10% used; 114348757 free inodes.

server4 `/var/tmp`: 105770647552 available bytes; 94.10% used; 114348757 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
