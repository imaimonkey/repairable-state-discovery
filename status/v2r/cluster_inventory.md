# V2R cluster inventory

2026-09-25T20:27:17.578097+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318705745920 available bytes; 82.22% used; 112476309 free inodes.

server1 `/home`: 318705745920 available bytes; 82.22% used; 112476309 free inodes.

server1 `/tmp`: 318705745920 available bytes; 82.22% used; 112476309 free inodes.

server1 `/var/tmp`: 318705745920 available bytes; 82.22% used; 112476309 free inodes.

server1 `/mnt/raid5`: 369624117248 available bytes; 98.30% used; 337540510 free inodes.
| server2 | True | ['4', '5', '6'] | [] |

server2 `/`: 23042953216 available bytes; 98.71% used; 110407152 free inodes.

server2 `/home`: 23042953216 available bytes; 98.71% used; 110407152 free inodes.

server2 `/tmp`: 23042953216 available bytes; 98.71% used; 110407152 free inodes.

server2 `/var/tmp`: 23042953216 available bytes; 98.71% used; 110407152 free inodes.

server2 `/mnt/raid5`: 303393820672 available bytes; 97.90% used; 445057386 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84379807744 available bytes; 95.29% used; 114152622 free inodes.

server3 `/home`: 84379807744 available bytes; 95.29% used; 114152622 free inodes.

server3 `/data`: 127179776000 available bytes; 98.24% used; 225808100 free inodes.

server3 `/tmp`: 84379807744 available bytes; 95.29% used; 114152622 free inodes.

server3 `/var/tmp`: 84379807744 available bytes; 95.29% used; 114152622 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105664634880 available bytes; 94.10% used; 114349568 free inodes.

server4 `/home`: 105664634880 available bytes; 94.10% used; 114349568 free inodes.

server4 `/data`: 228731359232 available bytes; 96.84% used; 224928833 free inodes.

server4 `/tmp`: 105664634880 available bytes; 94.10% used; 114349568 free inodes.

server4 `/var/tmp`: 105664634880 available bytes; 94.10% used; 114349568 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
