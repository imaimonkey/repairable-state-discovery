# V2R cluster inventory

2026-09-27T03:49:34.101427+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315075731456 available bytes; 82.42% used; 112443037 free inodes.

server1 `/home`: 315075731456 available bytes; 82.42% used; 112443037 free inodes.

server1 `/tmp`: 315075731456 available bytes; 82.42% used; 112443037 free inodes.

server1 `/var/tmp`: 315075731456 available bytes; 82.42% used; 112443037 free inodes.

server1 `/mnt/raid5`: 636788224000 available bytes; 97.08% used; 337401381 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17624182784 available bytes; 99.02% used; 110365007 free inodes.

server2 `/home`: 17624182784 available bytes; 99.02% used; 110365007 free inodes.

server2 `/tmp`: 17624182784 available bytes; 99.02% used; 110365007 free inodes.

server2 `/var/tmp`: 17624182784 available bytes; 99.02% used; 110365007 free inodes.

server2 `/mnt/raid5`: 578118193152 available bytes; 96.01% used; 444882232 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78700032000 available bytes; 95.61% used; 114062938 free inodes.

server3 `/home`: 78700032000 available bytes; 95.61% used; 114062938 free inodes.

server3 `/data`: 1335358537728 available bytes; 81.54% used; 225761256 free inodes.

server3 `/tmp`: 78700032000 available bytes; 95.61% used; 114062938 free inodes.

server3 `/var/tmp`: 78700032000 available bytes; 95.61% used; 114062938 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111027613696 available bytes; 93.80% used; 114372963 free inodes.

server4 `/home`: 111027613696 available bytes; 93.80% used; 114372963 free inodes.

server4 `/data`: 383852355584 available bytes; 94.70% used; 224780820 free inodes.

server4 `/tmp`: 111027613696 available bytes; 93.80% used; 114372963 free inodes.

server4 `/var/tmp`: 111027613696 available bytes; 93.80% used; 114372963 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
