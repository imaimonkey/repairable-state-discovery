# V2R cluster inventory

2026-09-27T09:09:46.722264+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 314456313856 available bytes; 82.46% used; 112440733 free inodes.

server1 `/home`: 314456313856 available bytes; 82.46% used; 112440733 free inodes.

server1 `/tmp`: 314456313856 available bytes; 82.46% used; 112440733 free inodes.

server1 `/var/tmp`: 314456313856 available bytes; 82.46% used; 112440733 free inodes.

server1 `/mnt/raid5`: 634582913024 available bytes; 97.09% used; 337400199 free inodes.
| server2 | True | ['1', '2', '7'] | [] |

server2 `/`: 16516227072 available bytes; 99.08% used; 110356972 free inodes.

server2 `/home`: 16516227072 available bytes; 99.08% used; 110356972 free inodes.

server2 `/tmp`: 16516227072 available bytes; 99.08% used; 110356972 free inodes.

server2 `/var/tmp`: 16516227072 available bytes; 99.08% used; 110356972 free inodes.

server2 `/mnt/raid5`: 574267187200 available bytes; 96.03% used; 444742425 free inodes.
| server3 | True | ['0'] | [] |

server3 `/`: 78556143616 available bytes; 95.62% used; 114062917 free inodes.

server3 `/home`: 78556143616 available bytes; 95.62% used; 114062917 free inodes.

server3 `/data`: 1332581109760 available bytes; 81.58% used; 225762835 free inodes.

server3 `/tmp`: 78556143616 available bytes; 95.62% used; 114062917 free inodes.

server3 `/var/tmp`: 78556143616 available bytes; 95.62% used; 114062917 free inodes.
| server4 | True | ['4', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111051030528 available bytes; 93.80% used; 114372863 free inodes.

server4 `/home`: 111051030528 available bytes; 93.80% used; 114372863 free inodes.

server4 `/data`: 364249247744 available bytes; 94.97% used; 224767985 free inodes.

server4 `/tmp`: 111051030528 available bytes; 93.80% used; 114372863 free inodes.

server4 `/var/tmp`: 111051030528 available bytes; 93.80% used; 114372863 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
