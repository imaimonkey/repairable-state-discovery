# V2R cluster inventory

2026-09-24T23:57:56.126410+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319091003392 available bytes; 82.20% used; 112480778 free inodes.

server1 `/home`: 319091003392 available bytes; 82.20% used; 112480778 free inodes.

server1 `/tmp`: 319091003392 available bytes; 82.20% used; 112480778 free inodes.

server1 `/var/tmp`: 319091003392 available bytes; 82.20% used; 112480778 free inodes.

server1 `/mnt/raid5`: 416916455424 available bytes; 98.09% used; 337623622 free inodes.
| server2 | True | [] | [] |

server2 `/`: 23099203584 available bytes; 98.71% used; 110410788 free inodes.

server2 `/home`: 23099203584 available bytes; 98.71% used; 110410788 free inodes.

server2 `/tmp`: 23099203584 available bytes; 98.71% used; 110410788 free inodes.

server2 `/var/tmp`: 23099203584 available bytes; 98.71% used; 110410788 free inodes.

server2 `/mnt/raid5`: 487445688320 available bytes; 96.63% used; 445164269 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84353966080 available bytes; 95.29% used; 114156084 free inodes.

server3 `/home`: 84353966080 available bytes; 95.29% used; 114156084 free inodes.

server3 `/data`: 128845393920 available bytes; 98.22% used; 225814041 free inodes.

server3 `/tmp`: 84353966080 available bytes; 95.29% used; 114156084 free inodes.

server3 `/var/tmp`: 84353966080 available bytes; 95.29% used; 114156084 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105798795264 available bytes; 94.10% used; 114348295 free inodes.

server4 `/home`: 105798795264 available bytes; 94.10% used; 114348295 free inodes.

server4 `/data`: 60782272512 available bytes; 99.16% used; 225105983 free inodes.

server4 `/tmp`: 105798795264 available bytes; 94.10% used; 114348295 free inodes.

server4 `/var/tmp`: 105798795264 available bytes; 94.10% used; 114348295 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
