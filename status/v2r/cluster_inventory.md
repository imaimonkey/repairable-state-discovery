# V2R cluster inventory

2026-09-25T16:18:01.792101+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318671319040 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318671319040 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318671319040 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318671319040 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 369331736576 available bytes; 98.31% used; 337544970 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107895296 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23107895296 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23107895296 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23107895296 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 318183374848 available bytes; 97.80% used; 445070813 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84403007488 available bytes; 95.29% used; 114152676 free inodes.

server3 `/home`: 84403007488 available bytes; 95.29% used; 114152676 free inodes.

server3 `/data`: 134926827520 available bytes; 98.14% used; 225806119 free inodes.

server3 `/tmp`: 84403007488 available bytes; 95.29% used; 114152676 free inodes.

server3 `/var/tmp`: 84403007488 available bytes; 95.29% used; 114152676 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636470784 available bytes; 94.11% used; 114349647 free inodes.

server4 `/home`: 105636470784 available bytes; 94.11% used; 114349647 free inodes.

server4 `/data`: 230236434432 available bytes; 96.82% used; 224934437 free inodes.

server4 `/tmp`: 105636470784 available bytes; 94.11% used; 114349647 free inodes.

server4 `/var/tmp`: 105636470784 available bytes; 94.11% used; 114349647 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
