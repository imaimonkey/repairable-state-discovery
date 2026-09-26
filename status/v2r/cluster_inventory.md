# V2R cluster inventory

2026-09-26T05:52:47.098796+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318780420096 available bytes; 82.22% used; 112476282 free inodes.

server1 `/home`: 318780420096 available bytes; 82.22% used; 112476282 free inodes.

server1 `/tmp`: 318780420096 available bytes; 82.22% used; 112476282 free inodes.

server1 `/var/tmp`: 318780420096 available bytes; 82.22% used; 112476282 free inodes.

server1 `/mnt/raid5`: 235005128704 available bytes; 98.92% used; 337540024 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22738067456 available bytes; 98.73% used; 110405657 free inodes.

server2 `/home`: 22738067456 available bytes; 98.73% used; 110405657 free inodes.

server2 `/tmp`: 22738067456 available bytes; 98.73% used; 110405657 free inodes.

server2 `/var/tmp`: 22738067456 available bytes; 98.73% used; 110405657 free inodes.

server2 `/mnt/raid5`: 274863280128 available bytes; 98.10% used; 445033842 free inodes.
| server3 | True | [] | [] |

server3 `/`: 83020926976 available bytes; 95.37% used; 114143382 free inodes.

server3 `/home`: 83020926976 available bytes; 95.37% used; 114143382 free inodes.

server3 `/data`: 124201127936 available bytes; 98.28% used; 225823792 free inodes.

server3 `/tmp`: 83020926976 available bytes; 95.37% used; 114143382 free inodes.

server3 `/var/tmp`: 83020926976 available bytes; 95.37% used; 114143382 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106094280704 available bytes; 94.08% used; 114348210 free inodes.

server4 `/home`: 106094280704 available bytes; 94.08% used; 114348210 free inodes.

server4 `/data`: 106987741184 available bytes; 98.52% used; 224929126 free inodes.

server4 `/tmp`: 106094280704 available bytes; 94.08% used; 114348210 free inodes.

server4 `/var/tmp`: 106094280704 available bytes; 94.08% used; 114348210 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
