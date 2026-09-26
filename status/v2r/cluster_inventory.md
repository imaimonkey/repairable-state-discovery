# V2R cluster inventory

2026-09-26T09:25:13.622061+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318636748800 available bytes; 82.22% used; 112475121 free inodes.

server1 `/home`: 318636748800 available bytes; 82.22% used; 112475121 free inodes.

server1 `/tmp`: 318636748800 available bytes; 82.22% used; 112475121 free inodes.

server1 `/var/tmp`: 318636748800 available bytes; 82.22% used; 112475121 free inodes.

server1 `/mnt/raid5`: 218979655680 available bytes; 99.00% used; 337538677 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22322827264 available bytes; 98.75% used; 110403919 free inodes.

server2 `/home`: 22322827264 available bytes; 98.75% used; 110403919 free inodes.

server2 `/tmp`: 22322827264 available bytes; 98.75% used; 110403919 free inodes.

server2 `/var/tmp`: 22322827264 available bytes; 98.75% used; 110403919 free inodes.

server2 `/mnt/raid5`: 254358773760 available bytes; 98.24% used; 445023207 free inodes.
| server3 | True | [] | [] |

server3 `/`: 82663153664 available bytes; 95.39% used; 114110809 free inodes.

server3 `/home`: 82663153664 available bytes; 95.39% used; 114110809 free inodes.

server3 `/data`: 123662733312 available bytes; 98.29% used; 225827919 free inodes.

server3 `/tmp`: 82663153664 available bytes; 95.39% used; 114110809 free inodes.

server3 `/var/tmp`: 82663153664 available bytes; 95.39% used; 114110809 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106045677568 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106045677568 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89325461504 available bytes; 98.77% used; 224883309 free inodes.

server4 `/tmp`: 106045677568 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106045677568 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
