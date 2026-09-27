# V2R cluster inventory

2026-09-27T02:33:20.254285+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 315079155712 available bytes; 82.42% used; 112443392 free inodes.

server1 `/home`: 315079155712 available bytes; 82.42% used; 112443392 free inodes.

server1 `/tmp`: 315079155712 available bytes; 82.42% used; 112443392 free inodes.

server1 `/var/tmp`: 315079155712 available bytes; 82.42% used; 112443392 free inodes.

server1 `/mnt/raid5`: 637261377536 available bytes; 97.08% used; 337401576 free inodes.
| server2 | True | [] | [] |

server2 `/`: 17635246080 available bytes; 99.02% used; 110365004 free inodes.

server2 `/home`: 17635246080 available bytes; 99.02% used; 110365004 free inodes.

server2 `/tmp`: 17635246080 available bytes; 99.02% used; 110365004 free inodes.

server2 `/var/tmp`: 17635246080 available bytes; 99.02% used; 110365004 free inodes.

server2 `/mnt/raid5`: 580331974656 available bytes; 95.99% used; 444884511 free inodes.
| server3 | True | [] | [] |

server3 `/`: 78708465664 available bytes; 95.61% used; 114062953 free inodes.

server3 `/home`: 78708465664 available bytes; 95.61% used; 114062953 free inodes.

server3 `/data`: 1337684590592 available bytes; 81.51% used; 225762282 free inodes.

server3 `/tmp`: 78708465664 available bytes; 95.61% used; 114062953 free inodes.

server3 `/var/tmp`: 78708465664 available bytes; 95.61% used; 114062953 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 111036321792 available bytes; 93.80% used; 114373258 free inodes.

server4 `/home`: 111036321792 available bytes; 93.80% used; 114373258 free inodes.

server4 `/data`: 400231194624 available bytes; 94.47% used; 224781502 free inodes.

server4 `/tmp`: 111036321792 available bytes; 93.80% used; 114373258 free inodes.

server4 `/var/tmp`: 111036321792 available bytes; 93.80% used; 114373258 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
