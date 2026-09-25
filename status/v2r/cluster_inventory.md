# V2R cluster inventory

2026-09-25T02:30:25.041549+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318970425344 available bytes; 82.21% used; 112480498 free inodes.

server1 `/home`: 318970425344 available bytes; 82.21% used; 112480498 free inodes.

server1 `/tmp`: 318970425344 available bytes; 82.21% used; 112480498 free inodes.

server1 `/var/tmp`: 318970425344 available bytes; 82.21% used; 112480498 free inodes.

server1 `/mnt/raid5`: 416213008384 available bytes; 98.09% used; 337605900 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23016120320 available bytes; 98.72% used; 110410437 free inodes.

server2 `/home`: 23016120320 available bytes; 98.72% used; 110410437 free inodes.

server2 `/tmp`: 23016120320 available bytes; 98.72% used; 110410437 free inodes.

server2 `/var/tmp`: 23016120320 available bytes; 98.72% used; 110410437 free inodes.

server2 `/mnt/raid5`: 483111952384 available bytes; 96.66% used; 445113745 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84351307776 available bytes; 95.29% used; 114156073 free inodes.

server3 `/home`: 84351307776 available bytes; 95.29% used; 114156073 free inodes.

server3 `/data`: 145592131584 available bytes; 97.99% used; 225811043 free inodes.

server3 `/tmp`: 84351307776 available bytes; 95.29% used; 114156073 free inodes.

server3 `/var/tmp`: 84351307776 available bytes; 95.29% used; 114156073 free inodes.
| server4 | True | ['0', '1', '3', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105895780352 available bytes; 94.09% used; 114350971 free inodes.

server4 `/home`: 105895780352 available bytes; 94.09% used; 114350971 free inodes.

server4 `/data`: 19853459456 available bytes; 99.73% used; 224969123 free inodes.

server4 `/tmp`: 105895780352 available bytes; 94.09% used; 114350971 free inodes.

server4 `/var/tmp`: 105895780352 available bytes; 94.09% used; 114350971 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
