# V2R cluster inventory

2026-09-25T20:25:45.910228+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318706057216 available bytes; 82.22% used; 112476327 free inodes.

server1 `/home`: 318706057216 available bytes; 82.22% used; 112476327 free inodes.

server1 `/tmp`: 318706057216 available bytes; 82.22% used; 112476327 free inodes.

server1 `/var/tmp`: 318706057216 available bytes; 82.22% used; 112476327 free inodes.

server1 `/mnt/raid5`: 369625366528 available bytes; 98.30% used; 337540512 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23036710912 available bytes; 98.71% used; 110407157 free inodes.

server2 `/home`: 23036710912 available bytes; 98.71% used; 110407157 free inodes.

server2 `/tmp`: 23036710912 available bytes; 98.71% used; 110407157 free inodes.

server2 `/var/tmp`: 23036710912 available bytes; 98.71% used; 110407157 free inodes.

server2 `/mnt/raid5`: 303436267520 available bytes; 97.90% used; 445057552 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84380270592 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84380270592 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127180451840 available bytes; 98.24% used; 225808115 free inodes.

server3 `/tmp`: 84380270592 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84380270592 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664675840 available bytes; 94.10% used; 114349569 free inodes.

server4 `/home`: 105664675840 available bytes; 94.10% used; 114349569 free inodes.

server4 `/data`: 228739198976 available bytes; 96.84% used; 224928871 free inodes.

server4 `/tmp`: 105664675840 available bytes; 94.10% used; 114349569 free inodes.

server4 `/var/tmp`: 105664675840 available bytes; 94.10% used; 114349569 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
