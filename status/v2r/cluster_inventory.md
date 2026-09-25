# V2R cluster inventory

2026-09-25T16:25:41.506551+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318682415104 available bytes; 82.22% used; 112476346 free inodes.

server1 `/home`: 318682415104 available bytes; 82.22% used; 112476346 free inodes.

server1 `/tmp`: 318682415104 available bytes; 82.22% used; 112476346 free inodes.

server1 `/var/tmp`: 318682415104 available bytes; 82.22% used; 112476346 free inodes.

server1 `/mnt/raid5`: 363883417600 available bytes; 98.33% used; 337544737 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107108864 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23107108864 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23107108864 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23107108864 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 317951504384 available bytes; 97.80% used; 445070428 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84401410048 available bytes; 95.29% used; 114152668 free inodes.

server3 `/home`: 84401410048 available bytes; 95.29% used; 114152668 free inodes.

server3 `/data`: 134857441280 available bytes; 98.14% used; 225805947 free inodes.

server3 `/tmp`: 84401410048 available bytes; 95.29% used; 114152668 free inodes.

server3 `/var/tmp`: 84401410048 available bytes; 95.29% used; 114152668 free inodes.
| server4 | True | ['5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105636257792 available bytes; 94.11% used; 114349648 free inodes.

server4 `/home`: 105636257792 available bytes; 94.11% used; 114349648 free inodes.

server4 `/data`: 230216077312 available bytes; 96.82% used; 224934267 free inodes.

server4 `/tmp`: 105636257792 available bytes; 94.11% used; 114349648 free inodes.

server4 `/var/tmp`: 105636257792 available bytes; 94.11% used; 114349648 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
