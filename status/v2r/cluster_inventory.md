# V2R cluster inventory

2026-09-25T01:44:13.377840+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319075414016 available bytes; 82.20% used; 112480769 free inodes.

server1 `/home`: 319075414016 available bytes; 82.20% used; 112480769 free inodes.

server1 `/tmp`: 319075414016 available bytes; 82.20% used; 112480769 free inodes.

server1 `/var/tmp`: 319075414016 available bytes; 82.20% used; 112480769 free inodes.

server1 `/mnt/raid5`: 416456130560 available bytes; 98.09% used; 337611300 free inodes.
| server2 | True | ['2', '3', '6'] | [] |

server2 `/`: 23041069056 available bytes; 98.71% used; 110410776 free inodes.

server2 `/home`: 23041069056 available bytes; 98.71% used; 110410776 free inodes.

server2 `/tmp`: 23041069056 available bytes; 98.71% used; 110410776 free inodes.

server2 `/var/tmp`: 23041069056 available bytes; 98.71% used; 110410776 free inodes.

server2 `/mnt/raid5`: 490658590720 available bytes; 96.61% used; 445160836 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84352544768 available bytes; 95.29% used; 114156078 free inodes.

server3 `/home`: 84352544768 available bytes; 95.29% used; 114156078 free inodes.

server3 `/data`: 146450771968 available bytes; 97.98% used; 225812053 free inodes.

server3 `/tmp`: 84352544768 available bytes; 95.29% used; 114156078 free inodes.

server3 `/var/tmp`: 84352544768 available bytes; 95.29% used; 114156078 free inodes.
| server4 | True | ['0', '1', '4', '5', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105770090496 available bytes; 94.10% used; 114348280 free inodes.

server4 `/home`: 105770090496 available bytes; 94.10% used; 114348280 free inodes.

server4 `/data`: 53309235200 available bytes; 99.26% used; 225030581 free inodes.

server4 `/tmp`: 105770090496 available bytes; 94.10% used; 114348280 free inodes.

server4 `/var/tmp`: 105770090496 available bytes; 94.10% used; 114348280 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
