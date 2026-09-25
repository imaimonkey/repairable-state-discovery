# V2R cluster inventory

2026-09-25T17:19:13.521696+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318679867392 available bytes; 82.22% used; 112476346 free inodes.

server1 `/home`: 318679867392 available bytes; 82.22% used; 112476346 free inodes.

server1 `/tmp`: 318679867392 available bytes; 82.22% used; 112476346 free inodes.

server1 `/var/tmp`: 318679867392 available bytes; 82.22% used; 112476346 free inodes.

server1 `/mnt/raid5`: 363854172160 available bytes; 98.33% used; 337543388 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 23107977216 available bytes; 98.71% used; 110407940 free inodes.

server2 `/home`: 23107977216 available bytes; 98.71% used; 110407940 free inodes.

server2 `/tmp`: 23107977216 available bytes; 98.71% used; 110407940 free inodes.

server2 `/var/tmp`: 23107977216 available bytes; 98.71% used; 110407940 free inodes.

server2 `/mnt/raid5`: 316355825664 available bytes; 97.81% used; 445068664 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84392542208 available bytes; 95.29% used; 114152610 free inodes.

server3 `/home`: 84392542208 available bytes; 95.29% used; 114152610 free inodes.

server3 `/data`: 132792045568 available bytes; 98.16% used; 225811530 free inodes.

server3 `/tmp`: 84392542208 available bytes; 95.29% used; 114152610 free inodes.

server3 `/var/tmp`: 84392542208 available bytes; 95.29% used; 114152610 free inodes.
| server4 | True | ['3', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105618014208 available bytes; 94.11% used; 114349644 free inodes.

server4 `/home`: 105618014208 available bytes; 94.11% used; 114349644 free inodes.

server4 `/data`: 229879836672 available bytes; 96.82% used; 224933030 free inodes.

server4 `/tmp`: 105618014208 available bytes; 94.11% used; 114349644 free inodes.

server4 `/var/tmp`: 105618014208 available bytes; 94.11% used; 114349644 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
